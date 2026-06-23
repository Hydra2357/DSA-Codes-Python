import pygame
import random
import sys

# Initialize pygame
pygame.init()

# --- Constants ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Colors
SKY_BLUE    = (113, 197, 207)
GROUND_COLOR = (222, 216, 149)
PIPE_COLOR  = (111, 196, 69)
PIPE_DARK   = (82, 160, 50)
BIRD_YELLOW = (255, 214, 0)
BIRD_ORANGE = (255, 140, 0)
BIRD_WHITE  = (255, 255, 255)
BIRD_EYE    = (30, 30, 30)
WHITE       = (255, 255, 255)
BLACK       = (0, 0, 0)
RED         = (220, 50, 50)
DARK_GREEN  = (60, 120, 40)

# Game settings
GRAVITY         = 0.5
FLAP_STRENGTH   = -9
PIPE_SPEED      = 3
PIPE_GAP        = 160
PIPE_INTERVAL   = 1500   # ms between pipes
GROUND_HEIGHT   = 80
BIRD_X          = 80

# --- Helper: draw rounded rectangle ---
def draw_rounded_rect(surface, color, rect, radius=8):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

# --- Bird class ---
class Bird:
    WIDTH  = 40
    HEIGHT = 30

    def __init__(self):
        self.x = BIRD_X
        self.y = SCREEN_HEIGHT // 2
        self.vel = 0
        self.angle = 0
        self.alive = True
        self.flap_frame = 0  # wing animation

    def flap(self):
        self.vel = FLAP_STRENGTH
        self.flap_frame = 10

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel
        # Tilt: nose up when going up, nose down when falling fast
        target_angle = max(-30, min(90, self.vel * 5))
        self.angle += (target_angle - self.angle) * 0.2
        if self.flap_frame > 0:
            self.flap_frame -= 1

    def draw(self, surface):
        # Draw bird as a rotated surface
        bird_surf = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        self._draw_bird_shape(bird_surf)
        rotated = pygame.transform.rotate(bird_surf, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(rotated, rect)

    def _draw_bird_shape(self, surf):
        # Body
        pygame.draw.ellipse(surf, BIRD_YELLOW, (2, 5, 36, 22))
        pygame.draw.ellipse(surf, BIRD_ORANGE, (2, 5, 36, 22), 2)
        # Wing (animated)
        wing_y = 8 if self.flap_frame > 5 else 14
        pygame.draw.ellipse(surf, BIRD_ORANGE, (8, wing_y, 20, 10))
        # Eye
        pygame.draw.circle(surf, BIRD_WHITE, (28, 10), 6)
        pygame.draw.circle(surf, BIRD_EYE,   (30, 10), 3)
        pygame.draw.circle(surf, WHITE,       (31, 9),  1)
        # Beak
        pygame.draw.polygon(surf, BIRD_ORANGE, [(35, 12), (40, 10), (35, 15)])

    def get_rect(self):
        return pygame.Rect(self.x - 18, self.y - 13, 36, 26)

    def is_out_of_bounds(self):
        return self.y + 15 >= SCREEN_HEIGHT - GROUND_HEIGHT or self.y - 15 <= 0


# --- Pipe class ---
class Pipe:
    WIDTH = 64

    def __init__(self, x):
        self.x = x
        gap_center = random.randint(180, SCREEN_HEIGHT - GROUND_HEIGHT - 180)
        self.top    = gap_center - PIPE_GAP // 2
        self.bottom = gap_center + PIPE_GAP // 2
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self, surface):
        cap_h = 24
        cap_w = self.WIDTH + 10

        # Top pipe body
        if self.top > 0:
            draw_rounded_rect(surface, PIPE_COLOR,
                              pygame.Rect(self.x, 0, self.WIDTH, self.top - cap_h), radius=0)
            # Top pipe cap
            draw_rounded_rect(surface, PIPE_COLOR,
                              pygame.Rect(self.x - 5, self.top - cap_h, cap_w, cap_h), radius=4)
            # Shine
            pygame.draw.rect(surface, PIPE_DARK,
                             pygame.Rect(self.x + self.WIDTH - 10, 0, 8, max(0, self.top - cap_h)))

        # Bottom pipe body
        bottom_body_top = self.bottom + cap_h
        bottom_body_h = SCREEN_HEIGHT - GROUND_HEIGHT - bottom_body_top
        if bottom_body_h > 0:
            draw_rounded_rect(surface, PIPE_COLOR,
                              pygame.Rect(self.x, bottom_body_top, self.WIDTH, bottom_body_h), radius=0)
            # Bottom pipe cap
            draw_rounded_rect(surface, PIPE_COLOR,
                              pygame.Rect(self.x - 5, self.bottom, cap_w, cap_h), radius=4)
            # Shine
            pygame.draw.rect(surface, PIPE_DARK,
                             pygame.Rect(self.x + self.WIDTH - 10, bottom_body_top, 8, bottom_body_h))

    def collides_with(self, bird_rect):
        cap_w = self.WIDTH + 10
        top_rect    = pygame.Rect(self.x - 5, 0, cap_w, self.top)
        bottom_rect = pygame.Rect(self.x - 5, self.bottom, cap_w,
                                  SCREEN_HEIGHT - GROUND_HEIGHT - self.bottom)
        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)

    def is_off_screen(self):
        return self.x + self.WIDTH < 0


# --- Cloud class ---
class Cloud:
    def __init__(self, x=None):
        self.x = x if x else random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)
        self.y = random.randint(30, 200)
        self.speed = random.uniform(0.3, 0.8)
        self.scale = random.uniform(0.6, 1.2)

    def update(self):
        self.x -= self.speed

    def draw(self, surface):
        s = self.scale
        cx, cy = int(self.x), int(self.y)
        pygame.draw.ellipse(surface, WHITE, (cx,       cy + int(10*s), int(60*s), int(30*s)))
        pygame.draw.ellipse(surface, WHITE, (cx+int(10*s), cy,           int(40*s), int(30*s)))
        pygame.draw.ellipse(surface, WHITE, (cx+int(30*s), cy + int(5*s), int(35*s), int(28*s)))

    def is_off_screen(self):
        return self.x + 100 < 0


# --- Game ---
class FlappyBird:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.font_big   = pygame.font.SysFont("Arial", 52, bold=True)
        self.font_med   = pygame.font.SysFont("Arial", 30, bold=True)
        self.font_small = pygame.font.SysFont("Arial", 22)
        self.reset()

    def reset(self):
        self.bird  = Bird()
        self.pipes = []
        self.clouds = [Cloud(random.randint(0, SCREEN_WIDTH)) for _ in range(4)]
        self.score = 0
        self.high_score = getattr(self, 'high_score', 0)
        self.state = "start"   # start | playing | dead
        self.last_pipe_time = pygame.time.get_ticks()
        self.ground_offset = 0
        self.flash_alpha = 0

    # --- Drawing helpers ---
    def draw_background(self):
        self.screen.fill(SKY_BLUE)
        for cloud in self.clouds:
            cloud.draw(self.screen)

    def draw_ground(self):
        ground_y = SCREEN_HEIGHT - GROUND_HEIGHT
        pygame.draw.rect(self.screen, GROUND_COLOR,
                         (0, ground_y, SCREEN_WIDTH, GROUND_HEIGHT))
        pygame.draw.rect(self.screen, (180, 160, 100),
                         (0, ground_y, SCREEN_WIDTH, 8))
        # Scrolling grass blades
        blade_spacing = 20
        for i in range(-1, SCREEN_WIDTH // blade_spacing + 2):
            bx = (i * blade_spacing - self.ground_offset % blade_spacing)
            pygame.draw.rect(self.screen, (90, 160, 60),
                             (bx, ground_y - 6, 8, 10), border_radius=3)

    def draw_score(self):
        score_text = self.font_big.render(str(self.score), True, WHITE)
        shadow     = self.font_big.render(str(self.score), True, (0,0,0,150))
        x = SCREEN_WIDTH // 2 - score_text.get_width() // 2
        self.screen.blit(shadow, (x + 2, 42))
        self.screen.blit(score_text, (x, 40))

    def draw_start_screen(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 80))
        self.screen.blit(overlay, (0, 0))

        # Title
        title = self.font_big.render("FLAPPY BIRD", True, BIRD_YELLOW)
        shadow = self.font_big.render("FLAPPY BIRD", True, BIRD_ORANGE)
        tx = SCREEN_WIDTH // 2 - title.get_width() // 2
        self.screen.blit(shadow, (tx + 3, 173))
        self.screen.blit(title,  (tx, 170))

        # Instruction
        t = pygame.time.get_ticks()
        alpha = int(200 + 55 * abs((t % 1000) / 500 - 1))
        msg = self.font_med.render("Press SPACE / Tap to start", True, WHITE)
        msg.set_alpha(alpha)
        self.screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, 280))

        # Controls hint
        hint = self.font_small.render("SPACE / Click to flap", True, (220, 220, 220))
        self.screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, 330))

    def draw_dead_screen(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120))
        self.screen.blit(overlay, (0, 0))

        # Score panel
        panel = pygame.Surface((300, 220), pygame.SRCALPHA)
        panel.fill((255, 255, 255, 200))
        pygame.draw.rect(panel, BIRD_ORANGE, (0, 0, 300, 220), 4, border_radius=12)
        self.screen.blit(panel, (50, 180))

        go = self.font_big.render("GAME OVER", True, RED)
        self.screen.blit(go, (SCREEN_WIDTH // 2 - go.get_width() // 2, 190))

        sc = self.font_med.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(sc, (SCREEN_WIDTH // 2 - sc.get_width() // 2, 255))

        hs = self.font_med.render(f"Best:  {self.high_score}", True, DARK_GREEN)
        self.screen.blit(hs, (SCREEN_WIDTH // 2 - hs.get_width() // 2, 295))

        t = pygame.time.get_ticks()
        alpha = int(200 + 55 * abs((t % 1000) / 500 - 1))
        restart = self.font_med.render("SPACE / Tap to restart", True, BIRD_ORANGE)
        restart.set_alpha(alpha)
        self.screen.blit(restart, (SCREEN_WIDTH // 2 - restart.get_width() // 2, 345))

    def draw_flash(self):
        if self.flash_alpha > 0:
            flash = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            flash.fill(WHITE)
            flash.set_alpha(self.flash_alpha)
            self.screen.blit(flash, (0, 0))
            self.flash_alpha = max(0, self.flash_alpha - 15)

    # --- Update ---
    def update(self):
        # Clouds always move
        for cloud in self.clouds:
            cloud.update()
        self.clouds = [c for c in self.clouds if not c.is_off_screen()]
        if len(self.clouds) < 5 and random.random() < 0.005:
            self.clouds.append(Cloud())

        if self.state != "playing":
            return

        # Ground scroll
        self.ground_offset += PIPE_SPEED

        # Bird
        self.bird.update()

        # Spawn pipes
        now = pygame.time.get_ticks()
        if now - self.last_pipe_time > PIPE_INTERVAL:
            self.pipes.append(Pipe(SCREEN_WIDTH + 10))
            self.last_pipe_time = now

        # Pipes
        bird_rect = self.bird.get_rect()
        for pipe in self.pipes:
            pipe.update()
            if pipe.collides_with(bird_rect):
                self.die()
                return
            if not pipe.passed and pipe.x + pipe.WIDTH < self.bird.x:
                pipe.passed = True
                self.score += 1
                if self.score > self.high_score:
                    self.high_score = self.score
        self.pipes = [p for p in self.pipes if not p.is_off_screen()]

        # Ground / ceiling collision
        if self.bird.is_out_of_bounds():
            self.die()

    def die(self):
        self.state = "dead"
        self.bird.alive = False
        self.flash_alpha = 200

    # --- Main loop ---
    def run(self):
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                    key = getattr(event, 'key', None)
                    if key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if self.state == "start":
                        self.state = "playing"
                        self.bird.flap()
                    elif self.state == "playing":
                        self.bird.flap()
                    elif self.state == "dead":
                        self.reset()
                        self.state = "playing"
                        self.bird.flap()

            self.update()

            # --- Draw ---
            self.draw_background()
            for pipe in self.pipes:
                pipe.draw(self.screen)
            self.draw_ground()
            self.bird.draw(self.screen)
            self.draw_flash()

            if self.state == "playing":
                self.draw_score()
            elif self.state == "start":
                self.draw_start_screen()
                self.bird.draw(self.screen)
            elif self.state == "dead":
                self.draw_score()
                self.draw_dead_screen()

            pygame.display.flip()


if __name__ == "__main__":
    game = FlappyBird()
    game.run()
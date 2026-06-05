import pygame
import random
import sys

# -----------------------------
# Flappy Bird - Full Working Game
# -----------------------------

pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
FPS = 60

# Colors
SKY_BLUE = (135, 206, 235)
GREEN = (0, 180, 0)
DARK_GREEN = (0, 120, 0)
YELLOW = (255, 220, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)

# Fonts
font = pygame.font.SysFont("arial", 32, bold=True)
small_font = pygame.font.SysFont("arial", 22)

# Game settings
GRAVITY = 0.5
FLAP_POWER = -8
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3
PIPE_SPAWN_TIME = 1500  # milliseconds
GROUND_HEIGHT = 80

# Bird settings
bird_x = 80
bird_y = HEIGHT // 2
bird_radius = 18
bird_vel = 0

# Game state
pipes = []
score = 0
game_over = False
game_started = False

# Timer for spawning pipes
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, PIPE_SPAWN_TIME)

def reset_game():
    global bird_y, bird_vel, pipes, score, game_over, game_started
    bird_y = HEIGHT // 2
    bird_vel = 0
    pipes = []
    score = 0
    game_over = False
    game_started = False

def create_pipe():
    """Create one top and one bottom pipe with a random gap position."""
    gap_y = random.randint(120, HEIGHT - GROUND_HEIGHT - 120 - PIPE_GAP)
    top_pipe = pygame.Rect(WIDTH, 0, PIPE_WIDTH, gap_y)
    bottom_pipe = pygame.Rect(WIDTH, gap_y + PIPE_GAP, PIPE_WIDTH,
                              HEIGHT - GROUND_HEIGHT - (gap_y + PIPE_GAP))
    return {"top": top_pipe, "bottom": bottom_pipe, "passed": False}

def draw_text_center(text, y, color=WHITE):
    txt = font.render(text, True, color)
    rect = txt.get_rect(center=(WIDTH // 2, y))
    screen.blit(txt, rect)

def draw_small_center(text, y, color=WHITE):
    txt = small_font.render(text, True, color)
    rect = txt.get_rect(center=(WIDTH // 2, y))
    screen.blit(txt, rect)

def check_collision(bird_rect, pipe):
    return bird_rect.colliderect(pipe["top"]) or bird_rect.colliderect(pipe["bottom"])

def draw_scene():
    # Background
    screen.fill(SKY_BLUE)

    # Some simple clouds
    pygame.draw.circle(screen, WHITE, (70, 80), 25)
    pygame.draw.circle(screen, WHITE, (95, 70), 30)
    pygame.draw.circle(screen, WHITE, (125, 82), 22)

    pygame.draw.circle(screen, WHITE, (300, 120), 20)
    pygame.draw.circle(screen, WHITE, (325, 110), 28)
    pygame.draw.circle(screen, WHITE, (355, 122), 18)

    # Pipes
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe["top"])
        pygame.draw.rect(screen, GREEN, pipe["bottom"])
        pygame.draw.rect(screen, DARK_GREEN, pipe["top"], 4)
        pygame.draw.rect(screen, DARK_GREEN, pipe["bottom"], 4)

    # Ground
    pygame.draw.rect(screen, (222, 184, 135), (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
    pygame.draw.rect(screen, (139, 69, 19), (0, HEIGHT - GROUND_HEIGHT, WIDTH, 10))

    # Bird
    bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius,
                            bird_radius * 2, bird_radius * 2)
    pygame.draw.circle(screen, YELLOW, (bird_x, int(bird_y)), bird_radius)
    pygame.draw.circle(screen, BLACK, (bird_x + 6, int(bird_y) - 5), 3)

    return bird_rect

def game_loop():
    global bird_y, bird_vel, score, game_over, game_started

    bird_rect = None

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        reset_game()
                    else:
                        game_started = True
                        bird_vel = FLAP_POWER

                if event.key == pygame.K_r and game_over:
                    reset_game()

            if event.type == SPAWNPIPE and not game_over and game_started:
                pipes.append(create_pipe())

        if not game_over and game_started:
            # Bird physics
            bird_vel += GRAVITY
            bird_y += bird_vel

            # Move pipes
            for pipe in pipes:
                pipe["top"].x -= PIPE_SPEED
                pipe["bottom"].x -= PIPE_SPEED

            # Remove off-screen pipes
            pipes[:] = [p for p in pipes if p["top"].x + PIPE_WIDTH > 0]

            # Score update
            for pipe in pipes:
                if not pipe["passed"] and pipe["top"].x + PIPE_WIDTH < bird_x:
                    pipe["passed"] = True
                    score += 1

            # Bird rectangle
            bird_rect = pygame.Rect(bird_x - bird_radius, int(bird_y) - bird_radius,
                                    bird_radius * 2, bird_radius * 2)

            # Collision with ground / ceiling
            if bird_y - bird_radius <= 0:
                game_over = True

            if bird_y + bird_radius >= HEIGHT - GROUND_HEIGHT:
                game_over = True

            # Collision with pipes
            for pipe in pipes:
                if check_collision(bird_rect, pipe):
                    game_over = True
                    break

        # Draw everything
        bird_rect = draw_scene()

        # Draw score
        score_text = font.render(str(score), True, WHITE)
        score_shadow = font.render(str(score), True, BLACK)
        screen.blit(score_shadow, (WIDTH // 2 - score_shadow.get_width() // 2 + 2, 22 + 2))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 22))

        # Start message
        if not game_started and not game_over:
            draw_text_center("FLAPPY BIRD", 220, WHITE)
            draw_small_center("Press SPACE to start", 270, WHITE)
            draw_small_center("Press SPACE to flap", 305, WHITE)

        # Game over message
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 120))
            screen.blit(overlay, (0, 0))

            draw_text_center("GAME OVER", 230, RED)
            draw_small_center(f"Score: {score}", 275, WHITE)
            draw_small_center("Press SPACE or R to restart", 315, WHITE)

        pygame.display.flip()

game_loop()
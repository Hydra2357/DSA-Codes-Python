# 📊 DSA Codes Python

A clean Python learning repository for **Data Structures, Algorithms, coding patterns, and small Python games**. The repo is organized so each topic has one clear home and duplicated nested folders have been removed.

## 📁 Repository Structure

```text
DSA-Codes-Python/
├── dsa/
│   ├── fundamentals/          # Core DSA notebooks
│   └── patterns/
│       ├── notebooks/         # Interview-pattern notebooks
│       └── scripts/           # Reusable Python pattern implementations
├── games/
│   └── flappy_bird/           # Pygame Flappy Bird project
├── PyGames/                   # Git submodule
├── pycode/                    # Git submodule
├── .gitignore
└── README.md
```

## 📚 DSA Fundamentals

| Topic | Notebook |
| --- | --- |
| Arrays - basics | [`dsa/fundamentals/arrays_basic.ipynb`](dsa/fundamentals/arrays_basic.ipynb) |
| Arrays - advanced | [`dsa/fundamentals/arrays_advanced.ipynb`](dsa/fundamentals/arrays_advanced.ipynb) |
| Recursion | [`dsa/fundamentals/recursion.ipynb`](dsa/fundamentals/recursion.ipynb) |
| Linked Lists | [`dsa/fundamentals/linked_lists.ipynb`](dsa/fundamentals/linked_lists.ipynb) |
| Stacks | [`dsa/fundamentals/stacks.ipynb`](dsa/fundamentals/stacks.ipynb) |
| Queues | [`dsa/fundamentals/queues.ipynb`](dsa/fundamentals/queues.ipynb) |
| Trees | [`dsa/fundamentals/trees.ipynb`](dsa/fundamentals/trees.ipynb) |
| Graphs | [`dsa/fundamentals/graphs.ipynb`](dsa/fundamentals/graphs.ipynb) |
| Hash Maps | [`dsa/fundamentals/hash_maps.ipynb`](dsa/fundamentals/hash_maps.ipynb) |
| Hashing | [`dsa/fundamentals/hashing.ipynb`](dsa/fundamentals/hashing.ipynb) |
| Heaps | [`dsa/fundamentals/heaps.ipynb`](dsa/fundamentals/heaps.ipynb) |
| Python DSA utilities | [`dsa/fundamentals/python_dsa_utilities.ipynb`](dsa/fundamentals/python_dsa_utilities.ipynb) |
| Multithreading | [`dsa/fundamentals/multithreading.ipynb`](dsa/fundamentals/multithreading.ipynb) |

## 🧩 DSA Patterns

| Pattern | Location |
| --- | --- |
| LeetCode practice | [`dsa/patterns/notebooks/leetcode.ipynb`](dsa/patterns/notebooks/leetcode.ipynb) |
| Sliding Window notebook | [`dsa/patterns/notebooks/sliding_window.ipynb`](dsa/patterns/notebooks/sliding_window.ipynb) |
| Two Pointers notebook | [`dsa/patterns/notebooks/two_pointers.ipynb`](dsa/patterns/notebooks/two_pointers.ipynb) |
| Sliding Window Python implementations | [`dsa/patterns/scripts/sliding_window_patterns.py`](dsa/patterns/scripts/sliding_window_patterns.py) |
| Small Python example | [`dsa/patterns/scripts/hello_example.py`](dsa/patterns/scripts/hello_example.py) |

## 🎮 Games

The Flappy Bird project now lives in [`games/flappy_bird/`](games/flappy_bird/).

Run it with:

```bash
python games/flappy_bird/flappy_bird.py
```

Install Pygame first if needed:

```bash
python -m pip install pygame
```

## ✅ What Was Cleaned

- Removed duplicated DSA folders that were accidentally nested under the Flappy Bird project.
- Flattened `DSA Codes/DSA Codes/` into `dsa/fundamentals/`.
- Moved coding pattern notebooks and scripts into `dsa/patterns/`.
- Moved the Flappy Bird game into `games/flappy_bird/`.
- Removed tracked IDE project files from the repository.
- Added a root `.gitignore` to keep caches, virtual environments, notebooks checkpoints, and editor files out of version control.

## 👨‍💻 Author

**Mahesh** (Hydra2357)

# Turtle Race

A Python turtle race in which any turtle can win. The race includes a finish
line, a traffic-light countdown, random movement, and a winner message.

## Requirements

- Python 3
- Tkinter

`turtle` and `tkinter` are included with most Python installations. On some
Linux distributions, Tkinter may need to be installed separately, for example:

```bash
sudo apt install python3-tk
```

## Run the race

From this directory, run:

```bash
python3 main.py
```

The original command is also supported:

```bash
python3 turtles-1.py
```

## How the game works

```mermaid
flowchart TD
	A[Start main.py] --> B[Create Turtle screen]
	B --> C[Draw finish line]
	C --> D[Create five racers from TURTLE_CONFIG]
	D --> E[Show red, yellow, and green countdown]
	E --> F[Move each racer by a random distance]
	F --> G{Has a racer reached the finish?}
	G -- No --> F
	G -- Yes --> H[Identify the winner]
	H --> I[Show winner dialog]
	I --> J[End game]
```

## Project structure

- `main.py` - application entry point.
- `race.py` - screen setup, turtle creation, countdown, race logic, and winner dialog.
- `turtles-1.py` - backwards-compatible launcher for `main.py`.

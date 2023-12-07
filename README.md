# Tic-Tac-Toe

A simple Tic-Tac-Toe game implemented in Python using the Tkinter library for the graphical user interface. The game allows two players to take turns making moves, and a computer opponent that randomly selects its moves. The winner is determined when a player successfully forms a horizontal, vertical, or diagonal line with their symbol (X or O). In case of a draw, the game resets for a new round.

## Features

- Two-player mode with "X" and "O" symbols.
- Computer opponent with random move selection.
- Responsive GUI with a reset button for convenience.
- Winning and draw conditions are checked after each move.

## How to Play

1. Run the script.
2. The game starts with "X" as the first player.
3. Click on an empty cell to make a move.
4. The game alternates between human and computer moves.
5. The game announces the winner or a draw and resets for a new round.

## Implementation Details

- The game uses a 3x3 grid represented by a 2D list (`self.board`).
- The Tkinter library is employed for creating the graphical user interface.
- Player moves are handled through button clicks.
- The computer opponent selects random moves.
- The game checks for a winner or draw after each move.
- The reset button allows for starting a new game.

## Usage

Ensure you have Python installed on your system. Run the script, and the game window will appear. Follow the on-screen instructions to make moves and enjoy the game.

```bash
python tic_tac_toe.py
```

## Requirements

- Python 3.x
- Tkinter library (usually included in standard Python installations)

## Acknowledgments

The implementation is a basic example of a Tic-Tac-Toe game using Python and Tkinter, suitable for educational purposes and simple gameplay.

# 🎮 Tic Tac Toe - Python Console Game

A simple two-player Tic Tac Toe game built using Python for the command line. Enjoy a classic game of Xs and Os with a text-based grid interface!

---

## 📌 Features

* Two-player mode (Player 1 as X, Player 2 as O)
* Turn-based gameplay with text input
* Win/draw detection
* Minimal and clear display of the grid
* Runs entirely in the terminal

---

## 🛠️ How to Run

1. **Clone the repository or download the `.py` file:**

   ```bash
   git clone https://github.com/sujaydhulipudi/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. **Run the game:**

   ```bash
   python tic_tac_toe.py
   ```

3. **Follow the on-screen instructions:**

   * Choose whether to play as X or O.
   * Enter your move as a number between `1` and `9`, representing the grid:

     ```
     1 | 2 | 3
     ---------
     4 | 5 | 6
     ---------
     7 | 8 | 9
     ```

---

## 🧠 Game Logic

* The game board is represented by a 3x3 matrix (`grid`).
* Players alternate turns and place their mark (`X` or `O`) by inputting a number from 1–9.
* The game checks for a winner after every move.
* If no winner is found after 9 moves, the game ends in a draw.

---

## 🧾 Sample Output

```
Welcome to Tic Tac Toe!
Do you want to be X or O: X
You are player 1

Player 1, Enter your move position (1-9): 5

     |     |     
------------------------
     |  X  |     
------------------------
     |     |     
...
```

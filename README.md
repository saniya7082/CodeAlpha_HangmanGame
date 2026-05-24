Hangman Game

A classic, lightweight text-based Hangman game built using Python. The game selects a random secret word from a built-in list, and the player has 6 attempts to guess it correctly, one letter at a time.

This project was built to practice core programming fundamentals like loops, conditional logic, and string manipulation.

Features
Zero Dependencies: Runs purely on Python's built-in standard libraries (no external installations needed).
Input Validation: Prevents players from losing lives if they accidentally type numbers, symbols, or letters they have already guessed.
Live Progress Tracking: Displays the hidden word with underscores (e.g., `p _ t h o n`) and lists your previously guessed letters after every turn.
6-Life Limit: Strict turn-tracking to keep the game challenging.

Concepts Practiced
Randomization: Utilizing 'random.Choice' to pick a new word every game.
Control Flow: Keeping the game alive using `while` loops and checking win/loss states with `if-else` blocks.
Data Structures: Managing lists and sets to track guessed characters and unique word letters.

How to Run the Game
Make sure you have Python 3 installed on your computer. You can check by running this command in your terminal:
```bash
python --version
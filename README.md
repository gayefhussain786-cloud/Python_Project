# Python Mini-Projects

This repository contains Python mini-projects developed as part of the B.Tech CSE (Data Science) curriculum. The projects follow a strict *Package Architecture* and are designed with a focus on modularity and clean code.

## Project Structure
The repository is organized into self-contained modules to ensure a clear separation of logic and user interaction.

- *ATM_Project/*: A full ATM simulation featuring balance checks, deposits, and withdrawals.
- *Game_Project/*: A Stone-Paper-Scissors game utilizing Python's random module.

---

## Project 1: ATM Simulation
A menu-driven system that simulates real-world bank transactions.
- *Features*: 
  - Real-time Balance Display
  - Secure Withdrawals & Deposits
  - Detailed Transaction Statement (History)
- *Key Logic*: Uses a class-based approach in logic.py to maintain session state.

## Project 2: Stone–Paper–Scissors
An interactive game where the user competes against the computer.
- *Features*:
  - Randomized computer moves using the random module.
  - Score/Winner display after every round.
  - Built-in input validation.
- *Key Logic*: Game logic is separated from the main.py menu loop for better readability.

---

## Technical Requirements Followed
- [x] *Infinite Loops*: All systems run on a while True menu-driven system.
- [x] *Package Architecture*: No business logic is written directly in the main file.
- [x] *Clean Code*: Meaningful variable names and structured function definitions.
- [x] *Git Version Control*: Organized folders and meaningful commit messages.

## How to Run the Projects (Instructions) :-
 1. To Run Both the Codes Of Project:
Write these commands in the terminal to run this :
```bash
**cd ATM_Project
python main.py
#
cd ..
cd Game_Project
python main.py

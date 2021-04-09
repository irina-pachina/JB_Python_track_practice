# JetBrains Python track practice
Practice from the [Python track](https://hyperskill.org/tracks/2) by JetBrains.

## Projects:
1. [Simple Chatty Bot](https://hyperskill.org/projects/97?track=2)
   
   Console chatbot that guesses age and can give a test and check answers. Simple program to know the basic syntax of Python using variables, conditions, loops, and functions.
   
2. [Tic-Tac-Toe](https://hyperskill.org/projects/73?track=2)
   
   Implementation of the game of tic-tac-toe that:
   - Prints an empty grid at the beginning of the game.
   - Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
   - Ends the game when someone wins or there is a draw.
   
3. [Loan Calculator](https://hyperskill.org/projects/90?track=2)
   
   Loan calculator can compute differentiated payments, annuity payment, monthly payments for every month and overpayment, loan principal and period to repay a loan.
   Program works with command-line arguments using modules *argparse*, *sys*:
   
   `python loan_calculator_cli.py --type=diff --principal=1000000 --periods=10 --interest=10`
   
4. [Hangman](https://hyperskill.org/projects/69?track=2)
   
   Implementation of the game of guessing word letter by letter that:
   - Prints a menu where a player can choose to either play or exit.
   - Creates a game loop where the program chooses word using *random* module, asks the user to enter the letters, prints word with uncovered letters and counts misses.
   - Ends the game when the word is uncovered or the user spends 8 'lives'.
   
5. [Coffee Machine](https://hyperskill.org/projects/68?track=2)
   
   Introduction to OOP. Program prints a menu where a user can choose to buy a coffee, fill up the machine, take out a cash, check the remaining ingredients or exit.
   
   Class *CoffeeMachine* has a method that takes a string as input. Every time the user inputs a string to the console, the program invokes this method with one argument. Program stores the current state of the machine to handle inputs for different purposes. 
   
6. [Markdown Editor](https://hyperskill.org/projects/162?track=2)
   
   Implementation of the markdown editor that:
   - Recognizes the formatters from Markdown language: *plain*, *bold*, *italic*, *link*, *inline-code*, *header*, *ordered-list*, *unordered-list*, *line-break*.
   - Has special commands: *!help*, *!done*.
   - *!done* saves the text to a file using built-in functions.
   
7. [Simple Banking System](https://hyperskill.org/projects/109?track=2)
   
   Implementation of a banking system that:
   - Allows customers to create a new account and do other basic bank operations.
   - Uses Luhn algorithm to create and check valid card numbers.
   - Stores an account information in database using *SQLite*.
   - Processes all console inputs with a method of the class Bank storing current state of the program. 
   
8. [Numeric Matrix Processor](https://hyperskill.org/projects/96?track=2)
   
   Implementation of a matrix processor that:
   - Can read and output matrices, do operations on them - addition, multiplying by a constant, multiplying 2 matrices, compute the determinant of a square matrix, transpose and inverse them.
   - Uses *recursion* to calculate a determinant.

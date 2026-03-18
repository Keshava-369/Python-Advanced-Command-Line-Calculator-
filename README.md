# Advanced Command-Line Calculator 

A robust, Object-Oriented Command-Line Interface (CLI) calculator written in Python. This project is designed to perform both basic arithmetic and advanced mathematical operations directly from the terminal.

It includes comprehensive error handling to ensure the program remains stable even with invalid inputs or extreme mathematical edge cases (like dividing by zero or calculating massive factorials).

##  Features

- **Basic Operations:** Addition, Subtraction, Multiplication, and Division.
- **Advanced Mathematics:** * Power ($x^y$)
    - Square Root ($\sqrt{x}$)
    - Factorial ($x!$)
    - Base-10 Logarithm and Natural Logarithm (ln)
- **Trigonometry:** Sine, Cosine, and Tangent (input in degrees).
- **Session History:** Keeps a running log of all calculations performed during the current session.
- **Robust Error Handling:** * Prevents crashes from non-numeric inputs (`ValueError`).
    - Handles mathematical domain errors gracefully (e.g., negative square roots, division by zero).
    - Safely manages `KeyboardInterrupt` and `EOFError` for clean exits.

##  Prerequisites

- **Python 3.x:** Ensure you have Python installed on your system. No external libraries are required as the project uses Python's built-in `math` and `sys` modules.

## How to Run

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the `CLI_Calculator.py` file.
4. Run the following command:

```
python CLI_Calculator.py
```

##  Usage Example

Upon running the script, you will be greeted with an interactive menu:

```
========================================
    ADVANCED COMMAND-LINE CALCULATOR
========================================
 Basic Operations:
  1. Addition (+)
  2. Subtraction (-)
  3. Multiplication (*)
  4. Division (/)

 Advanced Operations:
  5. Power (x^y)
  6. Square Root (√x)
  7. Factorial (x!)
  8. Logarithm (base 10)
  9. Natural Logarithm (ln)
 10. Trigonometry (sin, cos, tan)

 Other:
 11. View History
  12. Exit
========================================
```

Simply type the number corresponding to the operation you want to perform and follow the on-screen prompts!

## Context

Developed as a programming project demonstrating Object-Oriented Programming (OOP) principles, state management, and exception handling in Python.

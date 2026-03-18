import math
import sys

class AdvancedCalculator:

    def __init__(self):
        self.history = []

    def display_menu(self):
        print("\n" + "="*40)
        print("    ADVANCED COMMAND-LINE CALCULATOR")
        print("="*40)
        print(" Basic Operations:")
        print("  1. Addition (+)")
        print("  2. Subtraction (-)")
        print("  3. Multiplication (*)")
        print("  4. Division (/)")
        print("\n Advanced Operations:")
        print("  5. Power (x^y)")
        print("  6. Square Root (√x)")
        print("  7. Factorial (x!)")
        print("  8. Logarithm (base 10)")
        print("  9. Natural Logarithm (ln)")
        print(" 10. Trigonometry (sin, cos, tan)")
        print("\n Other:")
        print(" 11. View History")
        print("  0. Exit")
        print("="*40)

    def get_number(self, prompt="Enter a number: "):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print(" Error: Invalid input. Please enter a valid number.")
            except EOFError:
                print("\n\nInput terminated. Exiting calculator...")
                sys.exit()

    def log_history(self, operation, result):
        """Saves the operation and result to history."""
        self.history.append(f"{operation} = {result}")

    def run(self):
        """Main loop to run the calculator."""
        while True:
            self.display_menu()
            try:
                choice = input("\nSelect an operation (0-11): ").strip()
            except EOFError:
                print("\n\nExiting calculator. Have a great day!")
                sys.exit()

            if choice == '0':
                print("Exiting calculator. Have a great day!")
                sys.exit()

            elif choice in ['1', '2', '3', '4', '5']:
                # Operations requiring two numbers
                num1 = self.get_number("Enter the first number: ")
                num2 = self.get_number("Enter the second number: ")

                if choice == '1':
                    res = num1 + num2
                    self.log_history(f"{num1} + {num2}", res)
                    print(f"\n Result: {num1} + {num2} = {res}")
                elif choice == '2':
                    res = num1 - num2
                    self.log_history(f"{num1} - {num2}", res)
                    print(f"\n Result: {num1} - {num2} = {res}")
                elif choice == '3':
                    res = num1 * num2
                    self.log_history(f"{num1} * {num2}", res)
                    print(f"\n Result: {num1} * {num2} = {res}")
                elif choice == '4':
                    if num2 == 0:
                        print("\n Error: Division by zero is undefined.")
                    else:
                        res = num1 / num2
                        self.log_history(f"{num1} / {num2}", res)
                        print(f"\n Result: {num1} / {num2} = {res}")
                elif choice == '5':
                    try:
                        res = math.pow(num1, num2)
                        self.log_history(f"{num1} ^ {num2}", res)
                        print(f"\n Result: {num1} raised to power {num2} = {res}")
                    except ValueError:
                        print("\n Error: Math domain error (e.g., fractional power of a negative number).")
                    except OverflowError:
                        print("\n Error: The result is too large to calculate (Overflow).")

            elif choice in ['6', '7', '8', '9']:
                # Operations requiring one number
                num = self.get_number("Enter the number: ")

                if choice == '6':
                    if num < 0:
                        print("\n Error: Cannot calculate square root of a negative number in real numbers.")
                    else:
                        res = math.sqrt(num)
                        self.log_history(f"√{num}", res)
                        print(f"\n Result: Square root of {num} = {res}")
                elif choice == '7':
                    if num < 0 or not num.is_integer():
                        print("\n Error: Factorial is only defined for non-negative integers.")
                    elif num > 1000:
                        print("\n Error: Number too large. Please enter a number <= 1000 to prevent freezing.")
                    else:
                        res = math.factorial(int(num))
                        self.log_history(f"{int(num)}!", res)
                        print(f"\n Result: {int(num)}! = {res}")
                elif choice == '8':
                    if num <= 0:
                        print("\n Error: Logarithm undefined for zero or negative numbers.")
                    else:
                        res = math.log10(num)
                        self.log_history(f"log10({num})", res)
                        print(f"\n Result: Base-10 Logarithm of {num} = {res}")
                elif choice == '9':
                    if num <= 0:
                        print("\n Error: Natural Logarithm undefined for zero or negative numbers.")
                    else:
                        res = math.log(num)
                        self.log_history(f"ln({num})", res)
                        print(f"\n Result: Natural Logarithm (ln) of {num} = {res}")

            elif choice == '10':
                # Trigonometric 
                angle = self.get_number("Enter the angle in degrees: ")
                radians = math.radians(angle)
                try:
                    func = input("Choose function (sin, cos, tan): ").strip().lower()
                except EOFError:
                    print("\n\nExiting calculator. Have a great day!")
                    sys.exit()
                
                if func == 'sin':
                    res = math.sin(radians)
                    self.log_history(f"sin({angle}°)", res)
                    print(f"\n Result: sin({angle}°) = {res}")
                elif func == 'cos':
                    res = math.cos(radians)
                    self.log_history(f"cos({angle}°)", res)
                    print(f"\n Result: cos({angle}°) = {res}")
                elif func == 'tan':
                    # Handle others for tan (e.g., 90, 270 degrees)
                    if angle % 180 == 90:
                        print("\n Error: Tangent is undefined for this angle (infinity).")
                    else:
                        res = math.tan(radians)
                        self.log_history(f"tan({angle}°)", res)
                        print(f"\n Result: tan({angle}°) = {res}")
                else:
                    print("\n Error: Invalid trigonometric function selected.")

            elif choice == '11':
                # View History
                print("\n--- Calculation History ---")
                if not self.history:
                    print(" No calculations performed yet.")
                else:
                    for item in self.history:
                        print(f" > {item}")
                print("---------------------------")

            else:
                print("\n Error: Invalid choice. Please select a number from the menu.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    # This block ensures the calculator runs only when executed directly
    print("Initializing Calculator...")
    calc = AdvancedCalculator()
    try:
        calc.run()
    except KeyboardInterrupt:
        print("\n\nCalculator interrupted by user. Exiting...")
        sys.exit()
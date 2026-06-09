# Calculator Program
# Demonstrates Clean Code:
# Function and variable names are descriptive and clear.
# Demonstrates DRY:
# "Calculation complete" is stored in one place and reused.
# Demonstrates Single Responsibility:
# Each function handles only one task (input, calculation, or output).
# Demonstrates KISS:
# No unnecessary repeated print statements.



# FUNCTION 1 — Input
# Responsibility: Collect two numbers from the user only.
# No math, no printing results here.


def get_numbers():
    """Prompt the user for two float numbers and return them."""
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    return first_number, second_number



# FUNCTION 2 — Calculation
# Responsibility: Perform math only.
# No input prompts or print statements here.


def calculate(first_number, operator, second_number):
    """Perform the calculation based on the operator and return the result."""
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        # Guard against division by zero before dividing
        if second_number == 0:
            return "Error: Cannot divide by zero"
        return first_number / second_number
    else:
        return None  # Signal that the operator was invalid



# FUNCTION 3 — Output
# Responsibility: Display the result only.
# The completion message is printed ONCE here — not repeated. (DRY)


def display_result(result):
    """Print the result and a single completion message."""
    if result is None:
        print("Invalid operation")
    else:
        print("The answer is:", result)

    # Stored and printed once — fixes the repeated print violation (DRY + KISS)
    completion_message = "Calculation complete"
    print(completion_message)



# MAIN — Execution only
# Ties everything together cleanly.
# No logic or math.


def main():
    print("Welcome to Calculator")

    operator = input("Choose operation (+, -, *, /): ")

    first_number, second_number = get_numbers()

    result = calculate(first_number, operator, second_number)

    display_result(result)

    # Printed once — fixes the duplicate thank-you message (DRY + KISS)
    print("Thank you for using calculator")


# Standard entry point guard
if __name__ == "__main__":
    main()
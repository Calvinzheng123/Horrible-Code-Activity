# Calculator Program

# Violates Clean Code:
# Function names and variable names are unclear.

# Violates DRY:
# "Calculation complete" is repeated instead of reusing code.

# Violates Single Responsibility:
# Each function handles input, calculations, and output.

# Violates KISS:
# There are unnecessary repeated print statements.


def x():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("The answer is:", a + b)

    print("Calculation complete")
    print("Calculation complete")


def y():
    c = float(input("Enter first number: "))
    d = float(input("Enter second number: "))

    print("The answer is:", c - d)

    print("Calculation complete")
    print("Calculation complete")


def z():
    e = float(input("Enter first number: "))
    f = float(input("Enter second number: "))

    print("The answer is:", e * f)

    print("Calculation complete")
    print("Calculation complete")


def w():
    e = float(input("Enter first number: "))
    f = float(input("Enter second number: "))

    print("The answer is:", e / f)

    print("Calculation complete")
    print("Calculation complete")


print("Welcome to Calculator")

g = input("Choose operation (+, -, *, /): ")

if g == "+":
    x()

elif g == "-":
    y()

elif g == "*":
    z()

elif g == "/":
    w()

else:
    print("Invalid operation")

print("Thank you for using calculator")
print("Thank you for using calculator")
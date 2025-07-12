# Compare Two Numbers

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Compare and display result
if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} and {num2} are equal")
# To run:python A6.NumberComparison.py
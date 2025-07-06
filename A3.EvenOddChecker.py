# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Part 1: Check a single number
num = int(input("Enter a number to check: "))
print(f"{num} is {check_even_odd(num)}.")

# Part 2: Check a list of numbers
number_list = [12, 7, 9, 4, 20, 33, 15,25]

print("\nChecking list of numbers:")
for n in number_list:
    print(f"{n} is {check_even_odd(n)}.")

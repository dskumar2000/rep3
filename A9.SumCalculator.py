# Input: number n
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Loop from 1 to n and add each number
for i in range(1, n + 1):
    total += i

# Output the result
print(f"Sum of numbers from 1 to {n} is: {total}")
# To run : python A9.SumCalculator.py
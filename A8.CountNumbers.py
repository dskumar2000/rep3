# Sample list of numbers
numbers = [10, -5, 0, 23, -8, 0, 3, -1, 0]

# Initialize counters
positive_count = 0
negative_count = 0
zero_count = 0

# Count each type
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# Display results
print("Number List:", numbers)
print("✅ Positive numbers:", positive_count)
print("❌ Negative numbers:", negative_count)
print("⭕ Zeros:", zero_count)
# to run:: python A8.CountNumbers.py
numbers = (1, 5, 2, 3, 6, 4)

# 1. Print elements directly
print("--- 1. Tuple Elements ---")
for item in numbers:
    print(item)

# 2. Print elements using index
print("\n--- 2. Elements by Index ---")
for i in range(len(numbers)):
    print(numbers[i])

# 3. Voting eligibility check
print("\n--- 3. Voting Eligibility ---")
age = int(input("User Age: "))
if 18 <= age <= 110:
    print("Eligible for voting")
else:
    print("You are not eligible for voting")

# 4. Find maximum value
print("\n--- 4. Maximum Value ---")
max_value = numbers[0]
for item in numbers:
    if item > max_value:
        max_value = item
print("Max value:", max_value)

# 5. Multiplication table
print("\n--- 5. Multiplication Table ---")
num = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 6. Factorial of a number
print("\n--- 6. Factorial ---")
n = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# 7. Sum of factorials (1! + 2! + ... + n!)
# nested for loop
print("\n--- 7. Sum of Factorials ---")
limit = int(input("Enter limit for sum of factorials: "))
total = 0
for i in range(1, limit + 1):
    current_fact = 1
    for j in range(1, i + 1):
        current_fact *= j
    total += current_fact
print("Sum of factorials:", total)
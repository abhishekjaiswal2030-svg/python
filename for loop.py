# ==========================================
# Loop Concepts:
# 1. for loop   -> Jab pata ho kahan se kahan tak chalna hai (i = index)
# 2. while loop -> Jab kisi condition ke match hone tak chalana ho
# ==========================================


# ------------------------------------------
# 1. Print next 21 numbers starting after 15
# ------------------------------------------
number = 15
for i in range(0, 21):
    number += 1
    print(number)


# ------------------------------------------
# 2. Print numbers within a user-defined range
# ------------------------------------------
first_number = int(input('Start number: '))
second_number = int(input('Last number: '))

for i in range(first_number, second_number + 1):
    print(i)


# ------------------------------------------
# 3. Print multiplication table of any number
# ------------------------------------------
number = int(input('Which number table do you want: '))

for i in range(1, 11):
    print(i,'*',number,'=',number*i)

# Sample Output (for 5):
# 1 * 5 = 5
# 2 * 5 = 10


# ------------------------------------------
# 4. Find Even and Odd numbers in a range
# ------------------------------------------
first_number = int(input('Start number: '))
second_number = int(input('Last number: '))

for i in range(first_number, second_number + 1):
    if i % 2 == 0:
        print("Even Number:", i)
    else:
        print("Odd Number:", i) 
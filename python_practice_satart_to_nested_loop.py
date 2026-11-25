"""
==========================================================
 PYTHON PRACTICE - ALL IN ONE (bina def ke)
 Author : Abhishek Jaiswal
==========================================================
 INDEX (program chalane par number chuno)
 ---------------------------------------------------------
  PART 1 : Basics
    1  Operators
    2  Data types & type casting
  PART 2 : Collections
    3  String functions
    4  List functions
    5  Tuple
    6  Dictionary / data structure
  PART 3 : Conditional (if / elif / else)
    7  Q1 Even/Odd
    8  Q2 Positive/Negative/Zero
    9  Q3 Greater of two numbers
    10 Q4 Voting eligibility
    11 Q5 Check password
    12 Q6 Pass or Fail
    13 Voter list (nested if)
  PART 4 : Loops
    14 Next 21 numbers
    15 Numbers in range
    16 Multiplication table
    17 Even/Odd in range
    18 Max & Min value
    19 Sum & Average
    20 Odd numbers in range
    21 Tables in range (nested loop)
    22 for & while demo
    23 while: prime numbers till 154
    24 Loop with list
    25 Prime (single number)
    26 Prime (list)
    27 Even/Odd (list)
  PART 5 : Exams
    28 Exam 2 (full)
    29 Exam 3: positive/negative
    30 Exam 3: multiples of 3 & 5
    31 Exam 3: grade
    32 Exam 3: login
  PART 6 : Student projects
    33 Marks pass/fail
    34 Student data pass/fail
==========================================================
"""

print("========== PYTHON PRACTICE MENU ==========")
print("PART 1 : 1 Operators | 2 Data types")
print("PART 2 : 3 String | 4 List | 5 Tuple | 6 Dictionary")
print("PART 3 : 7 Even/Odd | 8 Pos/Neg/Zero | 9 Greater of two | 10 Voting")
print("         11 Password | 12 Pass/Fail | 13 Voter list")
print("PART 4 : 14 Next 21 numbers | 15 Range | 16 Table | 17 Even/Odd range")
print("         18 Max/Min | 19 Sum/Avg | 20 Odd range | 21 Tables range")
print("         22 for & while | 23 while prime | 24 Loop+list | 25 Prime")
print("         26 Prime list | 27 Even/Odd list")
print("PART 5 : 28 Exam 2 | 29 Exam3 pos/neg | 30 Exam3 multiples")
print("         31 Exam3 grade | 32 Exam3 login")
print("PART 6 : 33 Marks pass/fail | 34 Student data pass/fail")
choice = int(input("Number chuno: "))
print()

# subjects ki list (Part 3, 5, 6 me kaam aayegi)
subjects = ['Math', 'Physics', 'Computer', 'Art', 'English', 'Hindi']


# ==========================================================
# PART 1 : BASICS
# ==========================================================

# ---------- 1. Operators ----------
if choice == 1:
    print(30 + 40, 40 - 30, 40 * 3, 40 / 4, 45 % 5, 2 ** 5)


# ---------- 2. Data Types & Type Casting ----------
elif choice == 2:
    name = ['abhi', 'jais', 'shafi', 'jatin']    # List (mutable)
    name_1 = ('abhi', 'jais', 'shafi', 'jatin')  # Tuple (immutable)
    user = {"name": "Aarav", "age": 25}          # Dictionary

    # Arithmetic & type casting
    a = 40
    b = 10.50
    c = a + b
    d = bool(10)
    print(type(b))        # <class 'float'>
    print(type(d))        # <class 'bool'>
    print('sum:', c)      # sum: 50.5

    x = 12.68
    x = int(x)
    print(type(x), x)     # <class 'int'> 12

    # List operations
    name[0] = 'Abhishek'  # first element modify
    print(name[0])        # Abhishek
    print(name[2])        # shafi
    print(len(name))      # 4
    print(name[0].count('a', 0, 2))  # 'Ab' me 'a' = 1

    # Dictionary operations
    print('dict', user)
    print(user["name"])
    print(user['age'])
    # user.keys() me index [0] nahi chalta, isliye list() me convert
    print(list(user.keys())[0])      # name

    # List sorting & methods
    str_list = [20, 40, 50, 30]      # 'str' naam use mat karo (built-in hai)
    print(str_list)
    str_list.insert(2, 10)
    str_list.sort()
    print(str_list.index(50))        # sorting ke baad 50 ka index
    print(str_list)                  # [10, 20, 30, 40, 50]
    str_list.append(1)
    print(str_list)


# ==========================================================
# PART 2 : COLLECTIONS
# ==========================================================

# ---------- 3. String functions ----------
elif choice == 3:
    n = "abhIShek jaiSwal"
    print(len(n))                           # length
    print(n.lower())                        # abhishek jaiswal
    print(n.upper())                        # ABHISHEK JAISWAL
    print(n.title())                        # Abhishek Jaiswal
    print(n.capitalize())                   # Abhishek jaiswal
    print(n.strip())                        # start/end ke space hatata hai
    print(n.replace('abhIShek', 'killer'))  # replace everywhere
    print(n.find("a"))                      # index, nahi mila to -1
    print(n.count("a"))                     # kitni baar aaya
    print(n.startswith('abh'))              # True
    print(n.endswith('sal'))                # False


# ---------- 4. List functions ----------
elif choice == 4:
    l = ["list", "value"]
    n = [10, 20, 4000, 50, 10, 20]

    print(l)
    print(l[0])               # 'list'

    # Adding
    l.append("python")        # end me add
    print(l)
    l.insert(1, "python")     # index 1 par insert
    print(l)

    # Removing
    l.remove("python")        # pehla 'python' hatata hai
    print(l)
    l.pop(1)                  # index 1 ka item (index na do to last)
    print(l)

    # Sort / index / reverse / extend
    n.sort()
    print(n)                  # [10, 10, 20, 20, 50, 4000]
    print(n.index(50))        # 4
    n.reverse()
    print(n)                  # [4000, 50, 20, 20, 10, 10]
    n.extend([50, 50, 60, 10, 8, 70])
    print(n)


# ---------- 5. Tuple ----------
elif choice == 5:
    t = ("tuple", "function", "python")
    print(t)          # ('tuple', 'function', 'python')
    print(t[1])       # 'function'
    print(t[1:3])     # ('function', 'python')

    # Tuple immutable hota hai (change nahi hota), neeche wali line error degi:
    # t[3] = "abhishek"   # TypeError (index 3 bhi out of range hai)


# ---------- 6. Dictionary / Data structure ----------
elif choice == 6:
    student_info = {'name': 'ajeet', 'roll': 101, 'course': 'DADS'}
    print(student_info['name'])
    print(student_info.keys())
    print(student_info.values())

    # List of dictionaries
    student_infomation = [{'name': 'ajeet', 'roll': 101, 'course': 'DADS'},
                          {'name': 'abhi', 'roll': 102, 'course': 'DADS'},
                          {'name': 'shafi', 'roll': 103, 'course': 'DADS'},
                          {'name': 'jatin', 'roll': 104, 'course': 'DADS'}]
    print(student_infomation[2]['roll'])
    print(student_infomation[2].keys())
    print(student_infomation[2].values())

    teacher = [{'name': 'Abhishek', 'batch_no': 305, 'time': '4:30-6:00'}]
    print(teacher[0]['name'])
    print(teacher[0].keys())
    print(teacher[0].values())


# ==========================================================
# PART 3 : CONDITIONAL STATEMENTS
# ==========================================================

# ---------- 7. Q1 Even / Odd ----------
elif choice == 7:
    user = int(input('Give me number:'))
    if user % 2 == 0:
        print(user, ':This is Even number')
    else:
        print(user, ':This is odd number')


# ---------- 8. Q2 Positive / Negative / Zero ----------
elif choice == 8:
    user = int(input('Give me number:'))
    if user > 0:
        print(user, ':Positive')
    elif user < 0:
        print(user, ':Negative')
    else:
        print(user, ':Zero')


# ---------- 9. Q3 Greater of two numbers ----------
elif choice == 9:
    user_1 = int(input('Give me Number 1:'))
    user_2 = int(input('Give me Number 2:'))
    if user_1 > user_2:
        print(user_1, ':Greater Number 1')
    elif user_1 < user_2:
        print(user_2, ':Greater Number 2')
    else:
        print(user_1, '=', user_2, 'Equal Number')


# ---------- 10. Q4 Voting eligibility ----------
elif choice == 10:
    user = int(input('User Age:'))
    if user >= 18:
        print(user, ': Eligible for Voting')
    else:
        print(user, ': You are not Eligible for Voting')


# ---------- 11. Q5 Check password ----------
elif choice == 11:
    user_name = input('Enter User Name:')
    user_password = input('Enter User Password:')
    user = 'Admin'
    password = 'sql123'
    if user == user_name and password == user_password:
        print('welcome in python')
    else:
        print('chal bhak')


# ---------- 12. Q6 Student Pass or Fail ----------
elif choice == 12:
    marks = []
    for sub in subjects:
        marks.append(int(input("Student " + sub + ":")))
    total_marks = marks[0] + marks[1] + marks[2] + marks[3] + marks[4] + marks[5]
    if total_marks >= 198 and total_marks < 600:
        print('Total Marks:', total_marks, 'Pass')
    else:
        print('Total Marks:', total_marks, 'fail')


# ---------- 13. Voter list (nested if) ----------
elif choice == 13:
    for i in range(0, 2):
        name = input("User Name: ")
        age = int(input("User Age: "))
        country = input("User Country: ").strip().title()

        if country == "United Kingdom":
            print("Name:", name)
            print('Country:', country)
            print("You are UK citizen")
            if age >= 18:
                print('Age:', age)
                print("You are eligible for vote")
            else:
                print('Age:', age)
                print("You are not eligible for vote")
        else:
            print("You are not from United Kingdom")

        print("Thank you for applying for the voter list.")


# ==========================================================
# PART 4 : LOOPS
# for loop   -> jab pata ho kahan se kahan tak chalna hai (i = index)
# while loop -> jab kisi condition ke match hone tak chalana ho
# ==========================================================

# ---------- 14. 15 ke baad ke next 21 numbers ----------
elif choice == 14:
    number = 15
    for i in range(0, 21):
        number += 1
        print(number)


# ---------- 15. Numbers in range ----------
elif choice == 15:
    first_number = int(input('Start number: '))
    second_number = int(input('Last number: '))
    for i in range(first_number, second_number + 1):
        print(i)


# ---------- 16. Multiplication table ----------
elif choice == 16:
    number = int(input('Which number table do you want: '))
    for i in range(1, 11):
        print(i, '*', number, '=', number * i)

    # Sample Output (for 5):
    # 1 * 5 = 5
    # 2 * 5 = 10


# ---------- 17. Even / Odd in range ----------
elif choice == 17:
    first_number = int(input('Start number: '))
    second_number = int(input('Last number: '))
    for i in range(first_number, second_number + 1):
        if i % 2 == 0:
            print("Even Number:", i)
        else:
            print("Odd Number:", i)


# ---------- 18. Max & Min value ----------
elif choice == 18:
    numbers = [10, 5, 2, 50, 6, -4]    # 'list' naam use mat karo
    max_value = numbers[0]
    min_value = numbers[0]
    for i in numbers:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    print('max value:', max_value)
    print('min value:', min_value)


# ---------- 19. Sum & Average ----------
elif choice == 19:
    numbers = [10, 5, 2, 50, 6, -4]
    total = 0
    for i in numbers:
        total += i
    print('sum:', total)
    print('average:', total / len(numbers))


# ---------- 20. Odd numbers in range ----------
elif choice == 20:
    start = int(input("Start:"))
    end = int(input("End:"))
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i)


# ---------- 21. Tables in range (nested loop) ----------
elif choice == 21:
    start = int(input("Start:"))
    end = int(input("End:"))
    for j in range(start, end + 1):
        for i in range(1, 11):
            print(j * i)
        print("================")


# ---------- 22. for & while demo ----------
elif choice == 22:
    for i in range(0, 5):
        print(i, "this is the start")

    i = 0
    while i <= 4:
        print(i, 'this is the end')
        i += 1
    print('this is the for and while loop')


# ---------- 23. while: prime numbers till 154 ----------
elif choice == 23:
    i = 2
    while i <= 154:
        divisor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor += 1
        if divisor == 2:
            print("Prime Number:", i)
        i += 1


# ---------- 24. Loop with list ----------
elif choice == 24:
    numbers = [0, 5, 2, 3, 6, 4]

    # for loop se (index ke sath)
    length = len(numbers)
    for i in range(0, length):
        print(numbers[i])

    # while loop se (ulta print)
    print("--- reverse ---")
    length = len(numbers) - 1
    while length >= 0:
        print(numbers[length])
        length -= 1


# ---------- 25. Prime (single number) ----------
elif choice == 25:
    number = int(input('number:'))
    divisor = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisor += 1
    if divisor == 2:
        print('Prime Number:', number)
    else:
        print('Not a prime number:', number)


# ---------- 26. Prime (list) ----------
elif choice == 26:
    number = [51, 50, 70, 10, 2, 3, 4, 5]
    for m in range(0, len(number)):
        num = number[m]
        div = 0
        for i in range(1, num + 1):
            if num % i == 0:
                div += 1
        if div == 2:
            print(num, "prime")
        else:
            print(num, "not prime")


# ---------- 27. Even / Odd (list) ----------
elif choice == 27:
    number = [51, 50, 70, 10, 2, 3, 4, 5]
    for m in number:
        if m % 2 == 0:
            print(m, "is even Number")
        else:
            print(m, "is odd Number")


# ==========================================================
# PART 5 : EXAMS
# ==========================================================

# ---------- 28. Exam 2 ----------
elif choice == 28:
    numbers = (1, 5, 2, 3, 6, 4)

    # 1. Elements directly
    print("--- 1. Tuple Elements ---")
    for item in numbers:
        print(item)

    # 2. Elements using index
    print("\n--- 2. Elements by Index ---")
    for i in range(len(numbers)):
        print(numbers[i])

    # 3. Voting eligibility
    print("\n--- 3. Voting Eligibility ---")
    age = int(input("User Age: "))
    if 18 <= age <= 110:
        print("Eligible for voting")
    else:
        print("You are not eligible for voting")

    # 4. Maximum value
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

    # 6. Factorial
    print("\n--- 6. Factorial ---")
    n = int(input("Enter a number for factorial: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial:", fact)

    # 7. Sum of factorials (1! + 2! + ... + n!) - nested for loop
    print("\n--- 7. Sum of Factorials ---")
    limit = int(input("Enter limit for sum of factorials: "))
    total = 0
    for i in range(1, limit + 1):
        current_fact = 1
        for j in range(1, i + 1):
            current_fact *= j
        total += current_fact
    print("Sum of factorials:", total)


# ---------- 29. Exam 3: positive / negative ----------
elif choice == 29:
    for i in range(0, 10):
        number = int(input())
        if number > 0:
            print('positive')
        elif number < 0:
            print('negative')
        else:
            print('zero')


# ---------- 30. Exam 3: multiples of 3 & 5 ----------
elif choice == 30:
    for i in range(0, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i)


# ---------- 31. Exam 3: grade ----------
elif choice == 31:
    marks = []
    for sub in subjects:
        marks.append(int(input("Student " + sub + ":")))
    total_mark = 0
    for m in range(0, 6):
        total_mark += marks[m]

    print("total_mark", total_mark)
    avg = total_mark / 6
    print(avg)
    if avg > 99:
        print('Grade A')
    elif avg > 90:
        print('Grade B')
    elif avg > 70:
        print('Grade C')
    elif avg > 40:
        print('Grade D')
    else:
        print('bhag jao')


# ---------- 32. Exam 3: login (5 attempts) ----------
elif choice == 32:
    user = 'admin'
    password = 'sql123'
    for i in range(0, 5):
        user_name = input('Enter User Name:')
        user_password = input('Enter User Password:')
        if user == user_name and password == user_password:
            print('welcome in python')
        else:
            print('chal bhak')


# ==========================================================
# PART 6 : STUDENT PASS / FAIL PROJECTS
# ==========================================================

# ---------- 33. Marks pass/fail ----------
# Total marks + har subject me 33 se upar ho to 'Great' warna 'Back'
elif choice == 33:
    marks = []
    for sub in subjects:
        marks.append(int(input("Student " + sub + ":")))

    total_marks = 0
    for m in marks:
        total_marks += m

    if total_marks >= 198 and total_marks < 600:
        print('Total Marks:', total_marks, 'Pass')
    else:
        print('Total Marks:', total_marks, 'fail')

    for m in marks:
        if m >= 33:
            print(m, 'Great')
        else:
            print(m, 'Back')


# ---------- 34. Student data pass/fail ----------
elif choice == 34:
    student = {}
    student['Name'] = input('Student:')
    student['Roll'] = int(input('Roll_no:'))
    student['Class'] = int(input('Class:'))

    total_marks = 0
    for sub in subjects:
        student[sub] = int(input("Student " + sub + ":"))
        total_marks += student[sub]

    print(student)
    if total_marks >= 198 and total_marks < 600:
        print('Total Marks:', total_marks, 'Pass')
    else:
        print('Total Marks:', total_marks, 'fail')

    for sub in subjects:
        if student[sub] >= 33:
            print(sub, student[sub], 'Great')
        else:
            print(sub, student[sub], 'Back')


# ---------- galat number ----------
else:
    print("Galat number, dobara try karo.")

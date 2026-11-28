# ==========================================
# Loop Concepts:
# 1. for loop   -> Jab pata ho kahan se kahan tak chalna hai (i = index)
# 2. while loop -> Jab kisi condition ke match hone tak chalana ho
# ==========================================

'''
# ------------------------------------------
# 1. Print next 21 numbers starting after 15
# ------------------------------------------
number = 15
for i in range(0, 21):
    number += 1
    print(number)
'''

'''
# ------------------------------------------
# 2. Print numbers within a user-defined range
# ------------------------------------------
first_number = int(input('Start number: '))
second_number = int(input('Last number: '))

for i in range(first_number, second_number + 1):
    print(i)
'''
'''
# ------------------------------------------
# 3. Print multiplication table of any number
# ------------------------------------------
number = int(input('Which number table do you want: '))

for i in range(1, 11):
    print(i,'*',number,'=',number*i)

# Sample Output (for 5):
# 1 * 5 = 5
# 2 * 5 = 10
'''
'''
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
'''
list = [10, 5, 2, 50, 6, -4]
max_value=list[0]
min_value=list[0]
for i in list:
 if i>max_value:
    max_value=i
   
 if i<min_value:
    min_value=i
print('max value:',max_value)
print('min value:',min_value)

'''
sum=list[0]
for i in list:
 i+=sum
 sum=i
print(sum)
'''

'''
length=list.__len__()
sum=list[0]
avg=sum/length
for i in list:
 i+=sum
 sum=i
avg=sum/length
print(avg)
'''
start=int(input("Start:"))
end=int(input("End:"))
for i in range(start,end+2):
 if i%2!=00:
  print(i)

'''
start=int(input("Start:"))
end=int(input("End:"))
for j in range(start,end+1):
 for i in range(1,11):
  print(j*i)
 print("================")
print()
'''
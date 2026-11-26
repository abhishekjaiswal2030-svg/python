'''
16. Write a program to count how many digits are present in a positive integer. (Hint: convert the number to a
string and iterate over it, or use a loop with arithmetic.)
'''
num=int(input('User enter the number: '))
if num>0:
 num=str(num)
 print("Digits Counts:: ",num.__len__())
'''
2. Multiplication Table
Accept an integer from the user and print its multiplication table from 1 to 10 using a loop.
'''
user=int(input("Enter the number: "))
for i in range(1,11):
 print(i,"*",user,"=",user*i)
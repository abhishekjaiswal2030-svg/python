#13. Write a program to print the multiplication table of a number entered by the user.
number=int(input("User enter the number: "))
for i in range(1,11):
 print(number,"*",i,"=",number*i)
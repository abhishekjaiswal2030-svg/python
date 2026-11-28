#15. Write a program to calculate the factorial of a number using a for loop.
num=int(input('User enter the number: '))
fact=1
for i in range(1,num+1):
 fact=fact*i
print("Factotial:: ",fact)
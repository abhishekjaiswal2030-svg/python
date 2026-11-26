#14. Write a program to calculate the sum of the first N natural numbers. Accept N from the user.
num=int(input('User enter the number: '))
nat=0
for i in range(0,num+1):
 nat+=i
print("Natural:: ",nat)

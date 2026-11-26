#22. Write a program to check whether a number is prime. Use a for loop and a conditional statement.
n=int(input("Enter the Number: "))
div=0
for i in range(1,n+1):
 if n%i==0:
  div+=1
if div==2:
 print('-------Prime Number-------')
else:
 print('----Not a prime number----')
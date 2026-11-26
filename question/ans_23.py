#23. Write a program to print all prime numbers between 1 and N.
n=int(input("Enter the Number: "))
for m in range(1,n+1):
 div=0
 for i in range(1,m+1):
  if m%i==0:
   div+=1
 if div==2:
  print(m,"Prime Number")
 else:
  print(m,"Not a Prime Number")
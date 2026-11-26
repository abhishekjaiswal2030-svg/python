#19. Write a program to find the sum of all odd numbers between 1 and N.
a=int(input('Enter the first Number: '))
sum=0
for i in range(1,a+1):
 if i%2!=0:
  sum+=i
print('sum of all odd numbers: ',sum)
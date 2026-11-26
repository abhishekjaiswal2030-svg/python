#10. Write a program to check whether three sides can form a valid triangle. If valid, identify whether it is equilateral, isosceles, or scalene.
a=int(input('Enter the first Number: '))
b=int(input('Enter the second Number: '))
c=int(input('Enter the third Number: '))
if a==b==c:
 print('Equilateral')
elif a==b or b==c or c==a:
 print('Isosceles')
else:
 print('Scalene')

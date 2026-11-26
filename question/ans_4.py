#4. Write a program to check whether a given year is a leap year.
year=int(input('Enter the Year:'))
if year%4==0 or year%400==0:
 print('leap year')
else:
 print('Not a leap year')
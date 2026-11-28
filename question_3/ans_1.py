'''
1. Sum of Natural Numbers
Ask the user for a positive integer n. Use a for loop to calculate and display the sum of numbers from 1 to n.
'''
user=int(input("Enter the number: "))
sum=0
if user>=0:
 for i in range(0,user+1):
  sum=i+sum
print('Sum of Natural Numbers: ',sum)
  


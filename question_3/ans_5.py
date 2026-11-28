'''
5. Factorial of a Number
Accept a non-negative integer and calculate its factorial using a loop. Handle 0 correctly.
'''

user=int(input("Enter the number: "))
if user>=0:
 fact=1
 for i in range(1,user+1):
  fact=fact*i
print('Calculate its factorial: ',fact)
  

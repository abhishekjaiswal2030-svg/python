'''
3. Count Even and Odd Numbers
Accept 10 integers from the user. Use a loop to count how many are even and how many are odd. Display both counts.
'''
odd=0
even=0
for i in range(1,11):
 user=int(input("Enter the number: "))
 if user>=0:
  if user%2==0:
   print("even")
   even+=1
  else:
   print("odd")
   odd+=1
 
print('Count of odd: ',odd)
print('Count of even: ',even)
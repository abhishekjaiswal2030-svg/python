#24. Write a program to accept 10 numbers from the user and count how many are #positive, negative, and zero.
p=0
nig=0
z=0
for m in range(1,11):
 n = int(input('Give me Number:'))
 if n>0:
    print('positive')
    p+=1
 elif n<0:
    print('negative')
    nig+=1
 else:
  z+=1
  print('zero')
print(p," Total Positive")
print(nig,' Total Negative')
print(z,' Total Zero')

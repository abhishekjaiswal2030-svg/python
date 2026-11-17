number=int(input('number:'))
divsior=0 

for i in range(1,number+1):
 if (number%i==0):
  divsior+=1
if(divsior==2):
  print('Prime Number:',number)
else:
  print('Not a prime number:',number)
number=[51,50,70,10,2,3,4,5]
'''
for m in range(0,number.__len__()):
 num = number[m]
 div = 0
 for i in range(1, num + 1):
  if num % i == 0:
   div += 1
 if div == 2:
  print(num,"prime")
 else:
  print(num,"not prime")
'''
'''
for m in number:
  if(m%2==0):
    print(m," is even Number")
  else:
    print(m,"is odd numbber")
'''
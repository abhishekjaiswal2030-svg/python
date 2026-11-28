
a = 'abhishek jaiswal kuch kro'
l = len(a)
'''
u= "".join(dict.fromkeys(a))
#h=len("".join(dict.fromkeys(a)))

for m in range(0, l):
 b = 0 
 for i in range(0, l):
  if a[i] == u[m]:
   b += 1   
 print(b, u[m])
'''


for m in range(0,l):
 u=""
 for i in range(0,l):
  if a[i]!=a[m]:
 print(u)
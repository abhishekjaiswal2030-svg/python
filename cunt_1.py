
a = 'abhishek jaiswal kuch kro'
u= "".join(dict.fromkeys(a))
#h=len("".join(dict.fromkeys(a)))
l = len(a)
for m in range(0, l):
 b = 0 
 c = 0 
 for i in range(0, l):
  if a[i] == u[m]:
   b += 1   
 print(b, u[m])
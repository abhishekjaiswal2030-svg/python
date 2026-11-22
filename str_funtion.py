#String funtion
n="abhIShek jaiSwal"
print(n.__len__()) #==8 or print(len(v))
print(n.lower()) #==abhishek jaiswal
print(n.upper())  #==ABHISHEK JAISWAL
print(n.title())   #==Abhishek Jaiswal
print(n.capitalize()) #==Abhishek jaiswal
print(n.strip()) #==(cut sapce between for last and first)
print(n.replace('abhIShek','killer')) #==change every where in n 
print(n.find("a")) #==(0) return krta hai if nhi hai (-1)
print(n.count("a")) #== (3) how much word
print(n.startswith('abh')) #==True
print(n.endswith('sal'))   #==False
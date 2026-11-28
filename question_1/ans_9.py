#9. Write a simple calculator using if-elif-else. Accept two numbers and an operator (+, -, *, /). Handle division by zero.

num_1=int(input('Enter the first Number: '))
ope=str(input('Enter the operator: '))
num_2=int(input('Enter the second Number: '))

if ope=="+":
 sum=num_1+num_2
 print(sum)
elif ope=="-":
 m=num_1-num_2
 print(m)
elif ope=="*":
 into=num_1*num_2
 print(into)
elif ope=="/" and (num_1!=0 and num_2!=0):
 d=num_1/num_2
 print(d)
else:
 print('infinity')
 
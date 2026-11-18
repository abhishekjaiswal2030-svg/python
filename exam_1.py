'''
#Q1. Check Even or Odd Number.
user=int(input('Give me number:'))
if user%2==0:
 print(user,':This is Even number')
else:
 print(user,':This is odd number')
'''
'''
#Q2. Check Positive, Negative or Zero.
user=int(input('Give me number:'))
if user>0:
 print(user,':Positive')
elif user<0:
  print(user,':Negative')
else:
   print(user,':Zero')
'''
'''
#Q3. Find the Greater of Two Numbers.
user_1=int(input('Give me Number 1:'))
user_2=int(input('Give me Number 2:'))
if user_1>user_2:
 print(user_1,':Greater Number 1')
elif user_1<user_2:
 print(user_2,':Greater Number 2')
else: 
 print(user_1,'=',user_2,'Equle Number')
'''
'''
#Q4. Check Voting Eligibility.
user=int(input('User Age:'))
if user>=18:
 print(user,': Eligibile for Voting')
else:
 print(user,': You are not Eligibile for Voting')
'''
'''
#Q5. Check Password.
user_name=input('Enter User Name:')
user_password=input('Enter User Password:')
user=('Admin')
password=('sql123')
if user==user_name and password==user_password:
 print('welcome in python')
else:
 print('chal bhak')
'''
#Q6. Student Pass or Fail.

marks=[int(input("Student Math:")),int(input("Student physics:")),int(input("Student Computer:")),int(input("Student Art:")),int(input("Student English:")),int(input("Student Hindi:"))]
total_marks=marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+marks[5]
if total_marks>=198 and total_marks<600:
 print('Total Marks:',total_marks,'Pass') 
else:
 print('Total Marks:',total_marks,'fail')












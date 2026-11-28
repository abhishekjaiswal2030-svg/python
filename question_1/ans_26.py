# 26. Create a number guessing game. Store a secret number in your program and allow the user up to 5 attempts.
# After each attempt, display “Too high” or “Too low”. Use a for loop and conditional statements. Display a success
# message if the user guesses correctly; otherwise reveal the secret number.
for i in range(0,5):
 
 user_name=input('Enter User Name:')
 user_password=int(input('Enter User Password:'))
 user=('admin')
 password=8542
 if user==user_name and password==user_password:
  print('welcome in python')
 elif user_password>password:
  print('Too high')
 elif user_password<password:
  print('Too low')
else:
 print('user_name=admin','user_password=8542')
''' 
5. Write a program that accepts a student's marks and displays the grade using the following rules: 90–100 = A,
80–89 = B, 70–79 = C, 60–69 = D, below 60 = Fail. Also validate that marks are between 0 and 100.
'''
mark=int(input('Mark: '))
if mark>=0 and mark<=100:
  if mark>=90:
    print('A')
  elif mark>=89:
    print('B')
  elif mark>=79:
    print('C')
  elif mark>=69:
    print('D')
  else:
    print('Fail')
else:
 print('Number not accurate') 
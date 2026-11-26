'''
for i in range(0,101):
 if i%3==0 and i%5==0:
  print(i)
'''
'''
marks=[int(input("Student Math:")),int(input("Student physics:")),int(input("Student Computer:")),int(input("Student Art:")),int(input("Student English:")),int(input("Student Hindi:"))]
total_mark=0
for m in range(0,6):
 total_mark+=marks[m]

print("total_mark",total_mark)
avg=total_mark/6
print(avg)
if avg>99:
  print('Grade A')
elif avg>90:
  print('Grade B')
elif avg>70:
  print('Grade C')
elif avg>40:
  print('Grade D')
else:
 print('bhag jao')
'''




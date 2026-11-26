#25. Write a program to calculate the total and average of 5 subject marks, then display the grade using conditional statements.

marks=[int(input("Student Math:")),int(input("Student physics:")),int(input("Student Computer:")),int(input("Student English:")),int(input("Student Hindi:"))]
total_mark=0
for m in marks:
 total_mark=total_mark+m
print('Total_mark: ',total_mark)
avg=total_mark/5
print('avg: ',avg)
if total_mark > 500:
    print('Number not accurate')
else:
    if total_mark >= 400:
        print('Grade:: A')
    elif total_mark >= 300:
        print('Grade:: B')
    elif total_mark >= 250:
        print('Grade:: C')
    elif total_mark >= 165:
        print('Grade:: D')
        print(':: Pass ::')
    else:
        print('Total Marks:',total_mark,'-------Fail------') 
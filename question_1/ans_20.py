#20. Write a program to reverse a string using a for loop without using slicing.
a = input("Enter whatever: ")#abhi
rev = ""
for i in a:
    rev = i + rev
print(rev)

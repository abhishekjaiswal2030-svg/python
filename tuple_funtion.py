# Tuple basics
t = ("tuple", "function", "python")

print(t)  # ('tuple', 'function', 'python')
print(t[1])  # Element at index 1 -> 'function'
print(t[1:3])  # Slice from index 1 up to (3 - 1) -> ('function', 'python')

# Tuples are immutable (cannot be changed after creation),
# and index 3 is also out of range here (valid indices are 0, 1, 2)
t[3] = "abhishek"  # Raises TypeError
print(t)
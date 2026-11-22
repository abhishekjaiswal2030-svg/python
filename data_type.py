# --- Data Types & Collections ---
name = ['abhi', 'jais', 'shafi', 'jatin']       # List (mutable)
name_1 = ('abhi', 'jais', 'shafi', 'jatin')   # Tuple (immutable)
user = {"name": "Aarav", "age": 0.7}           # Dictionary

# --- Basic Arithmetic & Type Casting ---
a = 40
b = 10.50
c = a + b
d = bool(10)

print(type(b))                                # Output: <class 'float'>
print(type(d))                                # Output: <class 'bool'>
print('sum:', c)                              # Output: sum: 50.5

x = 12.68
x = int(x)
print(type(x), x)                             # Output: <class 'int'> 12

# --- List Operations & Modifications --------

name[0] = 'Abhishek'                          # Modifying the first list element
print(name[0])                                # Output: Abhishek
print(name[2])                                # Output: shafi
print(len(name))                              # Output: 4

# Counting characters in string (Note: range 0 to 2 checks 'Ab', so 'a' count is 1)
print(name[0].count('a',0,2))

# --- Dictionary Operations ---
print('dict', user)                           # Output: dict {'name': 'Aarav', 'age': 25}
print(user["name"])                           # Output: Aarav
print(user['age'])                            # Output: 25

# Why dictionary is converted into a list here:
# user.keys() returns a view object (dict_keys(['name', 'age'])) which does not support direct indexing [0].
# Wrapping it in list() converts it into a subscriptable list: ['name', 'age'], allowing us to access index 0 ('name').
print(list(user.keys())[0])                   # Output: name

# --- List Sorting & Methods ---
str_list = [20, 40, 50, 30]      
print(str_list)                               # (Changed variable name from 'str' to 'str_list' because 'str' is a built-in keyword)
str_list.insert(2, 10)                              # Inserting 10 at index 1
str_list.sort()                                 # Sorting the list

print(str_list.index(50))                     # Output: Index of 50 after sorting
print(str_list)                               # Output: [10, 20, 30, 40, 50]

str_list.append(1)
print(str_list)
# List functions / methods example

# 1. Basic list access
l = ["list", "value"]
n = [10, 20, 4000, 50, 10, 20]

print(l)      # ['list', 'value']
print(l[0])   # Index 0 ka element -> 'list'

# 2. Adding elements
l.append("python")
print(l)      # End mein 'python' add karega -> ['list', 'value', 'python']

l.insert(1, "python")
print(l)      # Index 1 par 'python' insert karega -> ['list', 'python', 'value', 'python']

# 3. Removing elements
l.remove("python")
print(l)      # Sirf pehla 'python' remove karega -> ['list', 'value', 'python']

l.pop(1)
print(l)      # Index 1 ka item hatayega (index na do to last item hatata hai) -> ['list', 'python']

# 4. Sorting, indexing, reversing, aur extending
n.sort()
print(n)           # Ascending order mein sort (jab sab elements comparable/numbers hon) -> [10, 10, 20, 20, 50, 4000]

print(n.index(50)) # Sorted list mein 50 ka index -> 4

n.reverse()
print(n)           # List ka order ulta kar dega -> [4000, 50, 20, 20, 10, 10]

n.extend([50, 50, 60, 10, 8, 70])
print(n)           # Ek saath saare elements end mein add karega -> [4000, 50, 20, 20, 10, 10, 50, 50, 60, 10, 8, 70]
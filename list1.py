my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[0])  # p

print(my_list[2])  # o


print(my_list[4])  # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])
# Negative indexing in lists
my_list = ['p','r','o','b','e']

print(my_list[-1])

print(my_list[-5])
# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']

# elements from index 2 to index 4
print(my_list[2:5])

# elements from index 5 to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

# Correcting mistake values in a list
odd = [2, 4, 6, 8]   
odd[0] = 1            

print(odd)
odd[1:4] = [3, 5, 7]

# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)

# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])

print(["re"] * 3)

# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

del my_list[2]

print(my_list)

del my_list[1:5]

print(my_list)

#remove
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list)

print(my_list.pop(1))

print(my_list)

print(my_list.pop())

print(my_list)

my_list.clear()

# Output: []
print(my_list)


































print(odd)

# =======================================
# LISTS
# =======================================
# A list is an ordered collection (keeps order, allows duplicates). In python the list
# will be a very common data structure when dealing with multiple pieces of values we want
# to iterate.

# Think about a list of fruits. To store the fruits we have we need a "basket,"
# to store them in. In this case our list is the data we put into our SQUARE BRACKETS "[]"
# we make a list in the form "listName = ["stuff", "thats", "in", "the", "list"]

fruits = ["apple", "banana", "apple", "cherry"]
print("List:", fruits)



# =======================================
# List Practice !!!
# =======================================
#
# Can you make a list of your own? In this section, try making a list of anything,
# then print out the contents!
vegetables = ["corn","carrots", "brocolli", "squash"]
print("List of vegetables: ", vegetables)

numbers=[3,4,5,10,1,2,3]
print("List of Numbers: ", numbers)


# =======================================
# Indexing
# =======================================
# Say we want to only display a single item of our list. We just want to pull a
# Single fruit from our "basket," so we use the Index!
# Index is of the form list[index], or "list at index number"
# In python (and most other languages) we start counting at zero,
# so if we want to access nth thing in our list, we go to index n-1.
print("First item:", fruits[0])

print("4th item: ", fruits[3])

# =======================================
# Adding and Removing
# =======================================
# Append and remove is important. In python, we just say list.append(thing we are adding)
# Here we insert the string "pear" at the end of the list
fruits.append("pear")
print("After append:", fruits)

fruits.append("watermelon")
print("After Append: ")
# It's pretty intuitive, here is remove

fruits.append(5)
print(fruits)

fruits.remove("banana")
print("After remove:", fruits)
# Say we add two tomatoes to the end of our list.
fruits.append("tomato")
fruits.append("tomato")
print(fruits)

# =======================================
# Add and Remove Practice!
# =======================================
# Now lets see if you can do the same to you list you created. Try adding something,
# printing, removing something, and then printing again!








# Each time we call remove it only removes the first instance.
# Here is how you would remove everything, by iterating through
# and using the function multiple times.
for anything in fruits[1:3]:
    if anything == 'tomato':
        fruits.remove(anything)
print(fruits)
# Which Brings us to iteration!
# ---------------------------------------
# Iteration
# Iteration is doing something repeatedly, or over and over.
# As you can see, there are many ways we can get through our lists,
# or "iterate," through our data most commonly with the use of for, and while loops
# ---------------------------------------

print("\nIterating fruits (method 1: simple for-loop)")
for f in fruits:
    print("Fruit:", f)

print("\nIterating fruits (method 2: by index)")
for i in range(len(fruits)):
    print("Index", i, "->", fruits[i])

print("\nIterating fruits (method 3: enumerate for index + value)")
for i, f in enumerate(fruits):
    print(f"Index {i} has {f}")

print("\nIterating fruits (method 4: while-loop)")
i = 0
while i < len(fruits):
    print("While loop ->", fruits[i])
    i += 1

#print("\nIterating fruits (method 5: list comprehension)")
#uppercased = [f.upper() for f in fruits]
#print("Uppercased:", uppercased)

print("\nIterating fruits (method 6: unpacking with * operator)")
print(*fruits)  # prints items separated by spaces

# =======================================
# Iterating Practice!!
# =======================================
# There are many ways we can iterate our data. Try some of them now,
# with the list you created!






# For more information on lists, their functions, and examples
# you can go to the official python documentation or read this
# handy guide by W3schools.
# https://docs.python.org/3/tutorial/datastructures.html
# https://www.w3schools.com/python/python_lists.asp



# =======================================
# Sets
# =======================================
#Sets are similar to lists but have some key characteristics from lists.
# They only include one copy of  each value that that satisfies the condition of the set.

# Say we have a list called a
a = [4,7,7,8,8,9,2,2,4,7]

# we want a set of everything that satisfies a condition, say all the odd numbers in the set
# think of this statement as {the set of all | such that}
# {the set of all num | such that num is in a and num is odd}
res = {num for num in a if num % 2 !=0}
print(res)

res2 = {anotherNum for anotherNum in a if anotherNum*anotherNum <= 16}
print(res2)

# =======================================
# Set Practice
# =======================================
# Make a set from this list
b = [1,2,3,4,55,6,2,4,12,64,256]
# Where some number thisNumber, is both in b and is also divisible by 3

res3 ={thisNumber for thisNumber in b if thisNumber % 3 == 0}
print("result 3: " ,res3)

# ========================================
# Dict
# ========================================
# Dictionaries (aka "dict") store KEY -> VALUE pairs.
# Key -> Value pairs. Fast lookups. Order is insertion order (Py3.7+).
# Syntax: {key: value, ...}     Keys: hashable (str/int/tuple). Values: anything.
# https://www.w3schools.com/python/python_dictionaries.asp

# Create
inventory = {"apple": 3, "banana": 1}
empty = {}
print(inventory)

# Read
print(inventory["apple"])          # 3  (raises KeyError if missing)
print(inventory.get("pear", 0))    # 0  (safe default)

# Add / Update
inventory["banana"] = 5            # update
inventory["pear"] = 2              # add


inventory["banana"] = 4           # update again
print (inventory.get("forbiddenMango"))
print(inventory)

# Remove
del inventory["pear"]              # delete key
count = inventory.pop("apple", 0)  # remove & return value (safe)
print(count, inventory)

# Check key
print("banana" in inventory)       # True

# Iterate (most useful)
for k, v in inventory.items():
    print(k, "->", v)

# Quick patterns
# 1) Dict comprehension
prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.1}
discount = {k: round(v * 0.9, 2) for k, v in prices.items() if v >= 1.0}
print(discount)  # {'apple': 1.08, 'cherry': 1.89}

# 2) Frequency count (idiomatic)
words = "a b a c a b".split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)    # {'a': 3, 'b': 2, 'c': 1}

# 3) Sorting results (optional)
print(sorted(counts.items(), key=lambda kv: kv[1], reverse=True))  # by value desc
# ========================================
# Dict Practice !!!
# ========================================
# Make a dictionary to keep track of a video game store's game_inventory







# ========================================
# Quick When-To-Use
# ========================================
# - LIST: ordered collection, duplicates allowed. Great for sequences.
# - SET: unique items, fast membership tests, no duplicates.
# - DICT: labeled data (key -> value), fast lookups and updates.

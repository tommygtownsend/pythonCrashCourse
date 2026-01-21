# ***************************************************************
# Iterators and Generators
# ***************************************************************

# Let's take a look at Iterators and Generators.
# An iterator is an object that can remember where it is in a sequence
# It has 2 special methods,
# It has two special methods:
# __iter__() → makes it iterable (so you can use for ... in)
#__next__() → tells Python how to get the next item.
# When Python runs out of items, __next__() raises StopIteration to signal “we’re done.”
# https://www.w3schools.com/python/python_iterators.asp

# We will Define a class that will behave like an iterator
class CountDown:
    # __init__ is the constructor; it runs when the object is created
    def __init__(self, start): # This is like the constructor in Java
        # Store the starting number in an instance variable
        self.current = start

    # __iter__() makes the object itself iterable (so we can use 'for ... in')
    def __iter__(self):
        return self   # return the iterator object (this class)

    # __next__() defines what happens each time we call next()
    def __next__(self):
        # If the current number is <= 0, stop the iteration
        if self.current <= 0:
            raise StopIteration   # required to end a for-loop
        # Save the current value to return
        num = self.current
        # Decrease the counter for the next call
        self.current -= 1
        # Return the saved number
        return num

# Create an iterator object that counts down from 5
for number in CountDown(5):
    # Each loop automatically calls __next__() until StopIteration
    print(number)




# That is a lot of boilerplate code, just to do a simple countdown,we can use a generator with yeild
def countdown(n):
    while n > 0:
        yield n   # pause & return value
        n -= 1
for number in countdown(3):
    print(number)


# Define a generator function that yields even numbers up to a limit
def even_numbers(limit):
    # Start counting from 0
    num = 0
    # Keep going until num exceeds the limit
    while num <= limit:
        # If num is divisible by 2, it's even
        if num % 2 == 0:
            # yield sends the value out, then pauses here
            yield num
        # Increase num by 1 each loop
        num += 1

# Use the generator in a for-loop
for value in even_numbers(10):
    # Each time through, we get the next even number
    print(value)





# Generator expressions
squares = (x*x for x in range(5))  # generator expression

for sq in squares:
    print(sq)


# ***************************************************************
# Iterators and Generators
# ***************************************************************

# Generators are great for working with large data because they don’t load everything at once.
def read_file_line_by_line(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

# Using the generator
for line in read_file_line_by_line("bigdata.txt"):
    print(line)   # prints one line at a time

# define your own function called read_csv_line_by_line() that can take in the bigdata2.txt,
# and displays the data, sorted. you can use python's built in sorts like .sort()

import numpy as np  # import the NumPy library with alias 'np'

# ********************** 1) WHY NUMPY (lists vs arrays) **********************
# NumPy is short for "Numerical Python"
# It is one of the most used libraries for handling all kinds of data.
# It performs calculations on large amounts of data more quickly by doing vector math on everything

# Some resouces for more numpy study
# https://numpy.org/doc/ # Official Documentation
# https://www.youtube.com/watch?v=VXU4LSAQDSc # Here is a great youtube tutorial
# https://www.w3schools.com/python/numpy/default.asp # W3 has great documentation as well
# https://www.geeksforgeeks.org/python/numpy-cheat-sheet/ another cheat sheet for numpy


# Python lists are general-purpose containers (flexible but slow for math)
lst = [1, 2, 3, 4]  # create a Python list of ints
print("List  * 2 ->", lst * 2)  # list * 2 repeats the list (not numeric multiply)

# NumPy arrays store numbers densely and support fast vectorized math
arr = np.array([1, 2, 3, 4])  # make a NumPy 1D array from a list
print("Array * 2 ->", arr * 2)  # elementwise multiply -> [2 4 6 8]

# Quick feel for list vs array (same result, arrays scale faster for large data)
py_list = list(range(1_0000))  # Python list of 0..9999
np_arr   = np.array(py_list)   # NumPy array from the same values
print("Sum(list)  =", sum(py_list))    # sum using Python built-in
print("np.sum(arr)=", np_arr.sum())    # sum using NumPy method

# ********************** 2) CREATING ARRAYS **********************
# With Numpy We have no shortage of arrays we can create! Here are some of the most common.
a = np.array([1, 2, 3])            # create from Python list
z = np.zeros((2, 3))               # 2x3 array filled with 0.0 (float) Fixes the problem of size complexity in sparse matrix
o = np.ones((3, 2))                # 3x2 array filled with 1.0
r = np.arange(0, 5, 0.5)            # integers [0,2,4,6,8] (stop is exclusive)
l = np.linspace(0, 1, 5)           # 5 evenly spaced points from 0 to 1

print("Array a:", a)               # show 1D array
print("Zeros z:\n", z)             # show 2D zeros array
print("Ones  o:\n", o)             # show 2D ones array
print("Arange r:", r)              # show step sequence
print("Linspace l:", l)            # show evenly spaced points


print('**************************************')
print('**************************************')

# Control data type at creation (memory/speed/precision)
# This is great because normally python isn't super specific with types.
ints32 = np.array([1, 2, 3], dtype=np.int32)   # force 32-bit int
floats = np.array([1, 2, 3], dtype=np.float64) # force 64-bit float (default on many systems)
ints16 = np.array([1,2,3,4,5,6,7,8], dtype=np.int16)
print("dtype control:", ints32.dtype, floats.dtype)  # print element dtypes

# ********************** 3) ARRAY ATTRIBUTES **********************

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])       # make a 2x3 array (rows x cols)
print("arr2d:\n", arr2d)            # display the 2D array
print("shape ->", arr2d.shape)      # tuple of (rows, cols)
print("ndim  ->", arr2d.ndim)       # number of dimensions (2 here)
print("size  ->", arr2d.size)       # total element count (6)
print("dtype ->", arr2d.dtype)      # data type of elements

# Views vs copies (reshape returns a view when possible)
base = np.arange(12)                 # array [0 1 2 3 4 5]
view = base.reshape(2, 6)           # 2x3 view that shares memory
base[10] = 9                        # modify base in-place
print("view sees base change:\n", view)  # view reflects the change
safe = base.copy()                  # explicit independent copy
base[1] = -1                        # modify base again
print("safe copy unaffected:", safe)     # copy is unchanged

# ********************** 4) INDEXING & SLICING **********************

a = np.array([10, 20, 30, 40, 50])  # 1D array for indexing demos
print("a[0]   ->", a[0])            # first element
print("a[-1]  ->", a[-1])           # last element
print("a[1:4] ->", a[1:4])          # slice from index 1 to 4
print("a[::2] ->", a[::2])          # slice with step 2

b = np.array([[1, 2, 3],
              [4, 5, 6]])           # 2x3 array for 2D indexing
print("b[0,1] ->", b[0, 1])         # element at row 0, col 1 (value 2)
print("b[:,1] ->", b[:, 1])         # all rows, column 1 (get a column)
print("b[1,:] ->", b[1, :])         # row 1, all columns (get a row)


c = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

print('6767676767767676767767767767')
print('c[2,1] ->', c[2,1] )


# Boolean mask to filter values
mask = a > 25                       # boolean array: True where a > 25
print("mask (a>25):", mask)         # show mask
print("a[mask]:", a[mask])          # apply mask to select elements

# Fancy indexing (pick positions by index list/array)
idx = [0, 2, 4]                     # positions to take
print("a[[0,2,4]] ->", a[idx])      # gather elements at those positions

# ********************** 5) ARRAY OPS + BROADCASTING **********************

x = np.array([1, 2, 3])             # 1D array x
y = np.array([4, 5, 6])             # 1D array y
print("x + y ->", x + y)            # elementwise add
print("x * y ->", x * y)            # elementwise multiply
print("x ** 2->", x ** 2)           # elementwise power
print("y > 4 ->", y > 4)            # elementwise comparison -> booleans



# When you do math on different shape arrays, numpy will align everything to the right
# If dimensions are equal we are fine.
# If one dimesnion is one, numpy stretches (braodcasts it)
# If neither match it is an error
# Broadcasting demo (align shapes from right; 1 or equal sizes can broadcast)
m = np.array([[1],
              [2],
              [3]])                 # shape (3,1) column vector
v = np.array([10, 20, 30])          # shape (1,3) row-ish vector
v_row = v[np.newaxis, :]            # shape (1,3) make v explicitly row
print("m + v_row ->\n", m + v_row)  # broadcasts to (3,3) and adds

M = np.arange(12).reshape(4, 3)     # shape (4,3): rows 0..3, cols 0..2
bias = np.array([100, 200, 300])    # shape (3,) per-column bias
print("M + bias ->\n", M + bias)    # add bias to each row (broadcast across rows)

# ********************** 6) AGGREGATIONS **********************

data = np.array([[1, 2, 3],
                 [4, 5, 6]])        # 2x3 data matrix
print("sum(data) ->", data.sum())   # sum of all elements
print("mean      ->", data.mean())  # average of all elements
print("min/max   ->", data.min(), data.max())  # global min and max
print("argmax    ->", data.argmax())           # index of max in flattened array

print("sum axis=0 ->", data.sum(axis=0))  # per-column sum (down rows)
print("sum axis=1 ->", data.sum(axis=1))  # per-row sum (across columns)

# ********************** 7) RESHAPING, TRANSPOSE **********************

arr = np.arange(6)                  # [0 1 2 3 4 5]
print("reshape(2,3):\n", arr.reshape(2, 3))  # change shape to 2 rows x 3 cols
print("transpose:\n", arr.reshape(2, 3).T)   # transpose rows<->cols
print("flatten:", arr.ravel())      # flatten to 1D (view if possible)

u = np.array([1, 2, 3])             # 1D row of three elements
v = np.array([4, 5, 6])             # another 1D row
print("vstack:\n", np.vstack([u, v]))        # stack as rows -> 2x3
print("column_stack:\n", np.column_stack([u, v]))  # stack as columns -> 3x2

# ********************** 8) RANDOM NUMBERS **********************

np.random.seed(0)                    # set RNG seed for reproducible outputs
print("rand:\n", np.random.rand(3, 3))        # uniform [0,1) 3x3
print("randn:\n", np.random.randn(3, 3))      # standard normal 3x3
print("randint:", np.random.randint(1, 7, 10)) # 10 integers in [1,6]

cards = np.array(["A", "K", "Q", "J"])        # small array of labels
np.random.shuffle(cards)                       # in-place random shuffle
print("shuffled:", cards)                      # show shuffled order
print("weighted choice:", np.random.choice([0,1], size=100, p=[0.7,0.3]))  # sample with probs

# ********************** 9) I/O QUICK LOOK **********************

tmp = np.arange(50000)                   # [0 1 2 3 4... 50000]
np.save("demo.npy", tmp)             # save in NumPy binary format (.npy)
print("npy load:", np.load("demo.npy"))       # load the .npy file

np.savetxt("demo.csv", np.arange(6).reshape(3,2), delimiter=",", fmt="%d")  # write CSV
print("wrote demo.csv")              # confirm CSV write

# ********************** 10) MINI PROJECT: DICE SIMULATION **********************

N = 1000000000                      # number of simulated trials
die1 = np.random.randint(1, 7, N)    # N rolls of die 1 (values 1..6)
die2 = np.random.randint(1, 7, N)    # N rolls of die 2 (values 1..6)
sums = die1 + die2                   # vectorized pairwise sum of dice

values, counts = np.unique(sums, return_counts=True)  # unique sums + their counts
probs = counts / N                   # convert counts to probabilities
for v, p in zip(values, probs):      # iterate over each sum and probability
    print(f"Sum {v:>2}: {p:.3f}")    # print nicely formatted probability per sum

max_is_6 = np.mean((die1 == 6) | (die2 == 6))         # proportion where at least one die is 6
print(f"P(max die = 6) ≈ {max_is_6:.3f}")             # print estimated probability


# ********************** 11) More Questions **********************
# https://www.geeksforgeeks.org/python/python-numpy-practice-exercises-questions-and-solutions/
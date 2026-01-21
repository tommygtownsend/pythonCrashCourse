import numpy as np

print(np.__version__) # We can print the version

my_list = [1,2,3,4]

my_list= my_list * 2 # This will just duplicate all elements in the list

print(my_list)

# Rather than using a list, we can create a numpy array!
array = np.array([1,2,3,4])
print(array)
array = array * 2 # Now we can quickly mult every entry by 2
print(array)

print(type(array)) # display the type for the array confirming it is np array

# Multidimensional array
array_md = np.array([[['A', 'B', 'C'],
                     ['D', 'E', 'F'],
                     ['G', 'H', 'I']]]) # A 2d array, matrix
print(array.ndim)
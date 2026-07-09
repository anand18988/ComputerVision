# creating arrays
import numpy as np

# Create a 1D array
row = np.array([10,20,30])
print(row)

# Create a 2D array 3X3 grid of zeros, simulating a black image)
black_image = np.zeros((3,3))
print(black_image)

#Creating 2D array of random numbers (simulating image noise)
noise = np.random.randint(0,255, size = (3,3))
print(noise)

# checking array properties
img = np.zeros((480,640,3)) # simulating a color image
print(img.shape)            # returns (480,640,3) ->( height, width, channels)
print(img.ndim)             # returns 3 -> its 3-dimensional array          
print(img.dtype)            # return float64

# indexing and slicing (cropping images)
# create a 4X4 matrix
matrix = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

# Get a single pixel value (Row 0, Column 1)
print (matrix[0,1])

# Slice/Crop a section: matrix[start_row:end_row,start_col:end_col]
# remember the end index is not included
crop = matrix [0:2, 1:3]
print(crop) 

# Array maths (filtering and brightness)
pixels = np.array([10,20,30])

#increase brightness of all pixel by 50
bright_pixels = pixels + 50
print(bright_pixels)

# contrast : multiply all pixels by 2
high_contrast = pixels * 2
print(high_contrast)

# Changing shapes (reshaping)
grid = np.array([[1,2],[3,4]])
print(grid)
flattened = grid.reshape(-1) # flattened to 1D array
print(flattened)

#Broadcasting in NumPy is a mechanism that allows arithmetic operations between arrays of different shapes.
import numpy as np

# A 2D array of shape (3, 3)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# A 1D array of shape (3,)
B = np.array([10, 20, 30])

# Perform addition using broadcasting
result = A + B
print("broadcasting \n",result)
result = B+A
print(result)

# Boolean indexing in NumPy is a powerful technique that allows you to select, filter, or modify elements 
# in an array based on specific conditions
import numpy as np

arr = np.array([10, 25, 30, 45, 60])

# Step 1: Create a boolean mask
mask = arr > 30  
# Output: [False, False, False,  True,  True]

# Step 2: Use mask to index the array
filtered_arr = arr[mask]  
# Output: [45, 60]
print(filtered_arr)

# Select all even numbers
evens = arr[arr % 2 == 0] 
# Output: [10, 30, 60]
print(evens)

# Select values greater than 15 AND less than 50
combined = arr[(arr > 15) & (arr < 50)]
# Output: [25, 30, 45]
print(combined)

# Replace all values less than 30 with 0
arr[arr < 30] = 0
print(arr) 
# Output: [0, 0, 30, 45, 60]

import numpy as np

# Array with missing data
data = np.array([10.5, np.nan, 20.3, np.nan, 45.1])

# Create a mask for non-NaN values using the ~ (NOT) operator
clean_mask = ~np.isnan(data)
# Output: [True, False, True, False, True]

# Filter out the NaNs
clean_data = data[clean_mask]
print(clean_data)  
# Output: [10.5, 20.3, 45.1]

# Replace all NaNs with 0 in-place
data[np.isnan(data)] = 0.0
print(data)  
# Output: [10.5,  0. , 20.3,  0. , 45.1]

arr = np.array([10, 20, 30, 40, 50])

#Fancy Indexing (Integer Array Indexing)
# Grab elements at index 0, 4, and 1
indices = [0, 4, 1]
print(arr[indices])  
# Output: [10, 50, 20]

matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# We want to select: matrix[0, 0], matrix[1, 2], and matrix[2, 1]
row_indices = [0, 1, 2]
col_indices = [0, 2, 1]

print(matrix[row_indices, col_indices])
# Output: [10, 60, 80]


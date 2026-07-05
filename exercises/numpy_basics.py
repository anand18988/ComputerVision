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
import numpy as np

# creating array 
new_array = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9],
                      [10,11,12]])

print("array is :", new_array)

# creating all zeros array
zero_array = np.zeros((4,4))
print("4d zero array", zero_array)

# creating noise array 
noise_array = np.random.randint(0,255,size = (4,4))
print("noise array :", noise_array)

# indexing in array
print("indexing is just pointing arrays row and column",new_array[0,2])

# slicing or cropping

sliced_array = new_array[0:2,0:2]
print("sliced array: ",sliced_array)

# for reshaping an array
reshaped_array = new_array.reshape(3,4)
print('reshaped array', reshaped_array)

# transposing array
transposed_array = reshaped_array.T
print("transposed array: ", transposed_array)

# matrix multiplication
multipil_array = np.matmul(reshaped_array,transposed_array)
print("multiplication of reshaped and transposed :\n", multipil_array)

# broadcasting
broad_array = multipil_array + 20
print("broadcasting 20 over matrix :\n ", broad_array)
# Define the original array
original_array = [0,-6,0,3,0,3,0,1,0,9,7,0,9,0,0,3,5]

# Initialize a new array with the first element from the original array
new_array = [original_array[0]]

# Calculate the sum of elements (A[i] + A[i+1]) and store in the new array
for i in range(len(original_array) - 1):
    new_array.append(original_array[i] + original_array[i+1])

# Print the new array
print(new_array)


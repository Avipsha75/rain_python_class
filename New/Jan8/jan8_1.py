import numpy as np

#Puzzle: Find the sum of elements along the diagonal and flip the matrix

#Generate a random 4x4 matrix with values between 0 and 100
matrix = np.random.randint(1, 21, (4, 4))
print("Original Matrix:")
print(matrix)

#Calculate the sum of the diagonal
diagonal_sum = np.trace(matrix)
print(f"\nSum of the diagonal: {diagonal_sum}")

#Flip the matrix vertically and horizontally
flipped_matrix = np.flip(matrix)
print("\nFlipped Matrix:")
print(flipped_matrix)

#Bonus: Identify positions of elements greater than 15
positions = np.argwhere(matrix > 15)
print("\nPositions of elements greater than 15:")
for pos in positions:
    print(f"Row: {pos[0] + 1}, Column: {pos[1] + 1}")
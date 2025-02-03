import numpy as np

arr = np.array([1, 2, 3, 4, 5])

sum = np.sum(arr)

mean = np.mean(arr)

std_dev = np.std(arr)

sum_multiplied = np.sum(arr * 2)

mean_multiplied = np.mean(arr * 2)

std_dev_multiplied = np.std(arr * 2)

print("Sum:", sum)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Sum multiplied by 2:", sum_multiplied)
print("Mean multiplied by 2:", mean_multiplied)
print("Standard Deviation multiplied by 2:", std_dev_multiplied)

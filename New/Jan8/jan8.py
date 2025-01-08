import numpy as np

arr = np.array([1,2,3,4,5])

print("1 D array:", arr)

arr = np.array([[1,2,3],[4,5,6]])

print("2 D array:", arr)

a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print(type(arr))
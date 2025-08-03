import numpy as np

a = np.array([1, 2, 3])
b = np.array([(2, 5, 6), (4, 10, 12), (8, 20, 24)])
c = np.zeros((4, 3))
d = np.eye(4)

print(a)
print(b)
print(c)
print(d)

b.max() # Max value of the matrix
b.min() # Min value of the matrix
b.sum() # Sum of values of the matrix
b.mean() # Mean of values of the matrix
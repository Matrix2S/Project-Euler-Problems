import numpy as np

x = np.arange(1,101)
x1 = sum(x**2)
x2 = sum(x)**2

y = x2 - x1
print(y)

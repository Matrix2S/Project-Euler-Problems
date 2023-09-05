import numpy as np

def fibonacci():
    x = [1,2]
    while x[len(x)-1] < 4000000:
        y = x[len(x)-1]+x[len(x)-2]
        if y >= 4000000:
            break
        x.append(y)
    return x

x = fibonacci()
x = np.asarray(x, dtype = "float")
y = np.array(x%2,dtype=bool)
sum(x[np.invert(y)])


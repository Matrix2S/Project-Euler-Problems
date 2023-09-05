import numpy as np

def solution(x):
    y = 0.0
    for i in x:
        if i%3 == 0:
           y = y+i
        elif i%5 == 0:
           y = y+i 
    print(y)

x = np.arange(1,1000, dtype = "float32")
solution(x)




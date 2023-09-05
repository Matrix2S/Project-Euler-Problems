
x1 = 1
x2 = 1
a = x1 + x2
k = 3

while len(str(a)) < 1000:    
    x1 = x2
    x2 = a
    a = x1 + x2
    k = k+1
print(k)

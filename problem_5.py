def check(x):
    if (x%20 == 0 and x%19 == 0 and x%18 == 0 and x%17 == 0 and x%16 == 0 and
            x%15 == 0 and x%14 == 0 and x%13 == 0 and x%12 == 0 and x%11 == 0):
        print(x)
        return True
    else:
        return False


x = 2520
while check(x) == False:
    x = x+1
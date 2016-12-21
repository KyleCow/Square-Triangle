m = -1
import math
while 1 == 1:
    m = m + 1
    x =(m*(m+1))/2
    if float(x).is_integer():
        s = math.sqrt(x)
        if float(s).is_integer():
            print("SquareTriangle=",x)

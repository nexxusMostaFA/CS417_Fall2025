import numpy as np

def slope_line(x1 , y1 , x2 , y2):
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    return m , c


tests = [ (0,0,1,1) , (0,1,1,0) , (0,0.5,1,0.5) ]
for t in tests:
    m , c  = slope_line(t[0] , t[1] , t[2] , t[3])
    print(f"Slope = {m} --- Intercept = {c}")
    print("*"   *20)
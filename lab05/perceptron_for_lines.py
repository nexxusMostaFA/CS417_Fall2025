import numpy as np

def step(x):
    return 1 if x >= 0 else 0

def p_lines(x):
    w = [1 ,1]
    b = -1
    z = np.dot(x , w) + b
    return step(z)


tests = [(0, 0), (0.6, 0.6), (1, 0), (0, 1), (0.2, 0.7)]
for p in tests:
    print(p, p_lines(p))
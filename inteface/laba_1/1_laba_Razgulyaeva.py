import time
import numpy as np
import math


def classic(a, b, step, fun):
    start = time.time()
    if fun == 'sin':
        print(sum(math.sin(i)*math.sin(i+step) for i in range(a, b-step, step))/step)
    return time.time() - start


def numpy_method(a, b, step, fun):
    if fun == 'sin':
        start = time.time()
        y = np.sin(np.array([i for i in range(a, b, step)]))
        print(sum(y[: -1]*y[1:])/step)
    return time.time()-start


print('Enter date (start, finish, step) :', end=' ')
a, b, step = map(int, input().split())
print(classic(a, b, step, 'sin'))
print(numpy_method(a, b, step, 'sin'))

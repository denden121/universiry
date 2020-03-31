import time
import numpy as np
import math


def classic_method(a, b, step, func):
    start = time.time()
    if func == 'sin':
        print('Classic method',sum(math.sin(i)*math.sin(i+step) for i in range(a, b-step, step))/step)
    elif func == 'cos':
        print('Classic method',sum(math.cos(i)*math.cos(i+step) for i in range(a, b-step, step))/step)
    else:
        raise('Error')
    finish = time.time() - start
    return finish


def numpy_method(a, b, step, func):
    if func == 'sin':
        start = time.time()
        y = np.array([i for i in range(a, b, step)])
        y = np.sin(y)
        result = sum(y[: -1]*y[1:])/step
        print('Numpy result:',result)
    elif func == 'cos':
        start = time.time()
        y = np.array([i for i in range(a, b, step)])
        y = np.cos(y)
        result = sum(y[: -1]*y[1:])/step
        print('Numpy result:',result)
    else:
        raise('Error')
    finish = time.time() - start
    return finish


print('Enter date start:', end=' ')
a = int(input()) 
print('Enter date finish:', end=' ')
b = int(input()) 
print('Enter date step:', end=' ')
step = int(input()) 
print('Classic method time:',classic_method(a, b, step, 'sin'))
print('Numpy method time: ',numpy_method(a, b, step, 'sin'))

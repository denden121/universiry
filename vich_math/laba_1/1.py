from math import *
from sympy import *
from sympy.sets import Interval


def create_file(name_file):
    with open(name_file, 'w') as f:
        f.write('f(x)=-(x-1)*(x-1)+2\n')
        f.write('-1 1\n')
        f.write('0.000001')


def first_method(func, start, finish, eps):
    i = 0
    while True:
        i += 1
        center = (start + finish)/2
        result = eval(func.replace('x', str(center)))
        if abs(result) < eps:
            with open('result.txt', 'w') as f:
                f.write(f'The root of the function is = {center}\n')
                error = abs(finish - start) / (2**i)
                f.write(f'The possible inaccuracy = {error}')
            break
        temp_result = eval(func.replace('x', str(start)))
        if result*temp_result < 0:
            finish = center
        else:
            start = center


def second_method(func, start, finish, eps):
    left_result = result = eval(func.replace('x', str(start)))
    right_result = result = eval(func.replace('x', str(finish)))
    x = start - ((left_result*(finish-start)
                       ) / (right_result-left_result))
    result_x = result = eval(func.replace('x', str(x)))
    last_x = x
    if result_x * right_result < 0:
        result = right_result
        dot = finish
    else:
        result = left_result
        dot = start
    while True:
        result_n = eval(func.replace('x', str(last_x)))
        x = last_x - (result_n/(result-result_n))*(dot-last_x)

        if abs(x - last_x) < eps:
            break
        last_x = x
    error = abs(x - last_x)
    with open('result.txt', 'w') as f:
        f.write(f'The root of the function is = {x}\n')
        f.write(f'The possible inaccuracy = {error}')


def third_method(func, start, finish, eps):
    left_result = eval(func.replace('x', str(start)))
    x = symbols('x')
    diff2 = diff(func, x, x)
    left_diff2 = eval(str(diff2).replace('x', str(start)))
    if left_result * left_diff2 > 0:
        last_x = start
    else:
        right_diff2 = eval(str(diff2).replace('x', str(finish)))
        right_result = eval(func.replace('x', str(finish)))
        if right_diff2*right_result > 0:
            last_x = finish
        else:
            last_x = start
            print("approximation is impossible")
    i = 0
    while True:
        i += 1
        diff1 = diff(func, x)
        result_diff1 = eval(str(diff1).replace('x', str(last_x)))
        result_last_x = eval(func.replace('x', str(last_x)))
        new_x = last_x - result_last_x/result_diff1
        new_result_x = eval(func.replace('x', str(new_x)))
        if abs(new_x-last_x) < eps and abs(new_result_x) < eps:
            break
        last_x = new_x

    down = maximum(diff(func, x, x), x, Interval(start, finish)) / \
        (2*minimum(diff(func, x), x, Interval(start, finish)))
    up = 2**i - 1
    error = (down**up)*(abs(finish - start)**(2*i))
    with open('result.txt', 'w') as f:
        f.write(f'The root of the function is = {new_x}\n')
        f.write(f'The possible inaccuracy = {error}')


def fourth_method(func, start, finish, eps):
    temp_start = start
    temp_finish = finish
    left_result = eval(func.replace('x', str(temp_start)))
    right_result = eval(func.replace('x', str(temp_finish)))
    new_x = temp_start - \
        (left_result/(right_result-left_result))*(temp_finish-temp_start)
    last_x = new_x
    x = symbols('x')
    diff1 = diff(func, x)
    diff2 = diff(func, x, x)
    diff2_result_right = eval(str(diff2).replace('x', str(temp_finish)))
    if right_result*diff2_result_right > 0:
        dot = temp_finish
    else:
        dot = temp_start
    while True:
        result_last_x = eval(func.replace('x', str(last_x)))
        result_dot = eval(func.replace('x', str(dot)))
        result_diff1_dot = eval(str(diff1).replace('x', str(dot)))
        new_x = last_x - result_last_x * \
            (dot - last_x)/(result_dot-result_last_x)
        dot = dot-(result_dot/result_diff1_dot)
        if abs(new_x-last_x) < eps and abs(result_dot) < eps:
            break
        last_x = new_x
    error = abs(new_x - last_x)
    with open('result.txt', 'w') as f:
        f.write(f'The root of the function is = {new_x}\n')
        f.write(f'The possible inaccuracy = {error}')


create_file(r'input.txt')
with open(r'input.txt') as f:
    func = f.readline().split('=')[1]
    start, finish = map(float, f.readline().split(' '))
    eps = float(f.readline())

while True:
    print('Select method(1,2,3,4) or exit(5)', end=' ')
    method = input()
    if method == '1':
        first_method(func, start, finish, eps)
    elif method == '2':
        second_method(func, start, finish, eps)
    elif method == '3':
        third_method(func, start, finish, eps)
    elif method == '4':
        fourth_method(func, start, finish, eps)
    elif method == '5':
        break
    else:
        print('Repeat enter')

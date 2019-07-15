# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Read the numbers entered through the space, and sort them in ascending order
print(sorted(map(int, input().split())))

# Fill the table n * m from 1 before m * n snake
[[ m * i + j * (i % 2 == 0) + (m - 1 - j) * (i % 2 == 1) for j in range(m)] for i in range(n)]

# Encodes the text with Caesar cipher
print("".join([chr(ord(c) + 1) for c in input()]))

# Decodes the text encoded by Caesar cipher
print("".join([chr(ord(c) - 1) for c in input()]))


# String conversion 
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
       return (f'{self.__class__.__name__}('
               f'{self.color!r}, {self.mileage!r})')

    #def __str__(self):
        #return f'a {self.color} car, mileage = {self.mileage}'

my_car = Car('red', 39023)
print(my_car)


# Decorators wrap a function, modifying its behavior
# 1
import functools

def do_twice(func):
	@functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
    
@do_twice
def greet(name):
    print(f'Hello {name}')
    
greet('World')
print(greet)

@do_twice
def return_greeting(name):
    print('Creating greeting')
    return (print(f'Hi {name}'))
    
return_greeting('gk')
print(return_greeting)

print(do_twice)

# 2
import functools
import time

def timer(func):
    '''Print the runtime of the decorated function'''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs')
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(100)])
        
waste_some_time(1)
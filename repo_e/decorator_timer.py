from time import time



@decorator
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j
long_time(10)

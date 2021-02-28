from numba import jit
import numpy as np

from utils.time import time_work, get_time_work

@get_time_work
def go(n): # Function is compiled to machine code when called the first time
    rez = []
    for i in range(n):
        rez.append(i**100)
    return rez

@get_time_work
@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def go_fast(n): # Function is compiled to machine code when called the first time
    rez = []
    for i in range(n):
        rez.append(i**100)
    return rez

import math
import os
import sys


def function_sort(other):
    return sorted(other)


def function_map(some_list):
    out_list = map(double_numbers, some_list)
    return list(out_list)


def double_numbers(numbers_list):
    return numbers_list + numbers_list


def filter_list(numbers):
    out_numbers = filter(good_numbers, numbers)
    return list(out_numbers)


def good_numbers(number):
    if number % 2 == 0:
        return True
    else:
        return False


def functions_pi():
    return math.pi


def functions_sqrt(number):
    return math.sqrt(number)


def functions_pow(number, degree):
    return math.pow(number, degree)


def functions_hypo(x, y):
    return math.hypot(x, y)

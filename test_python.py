import default_functions as t1
import math

# pi функция
assert t1.functions_pi() == math.pi

# sqrt функция
assert t1.functions_sqrt(4) == 2
assert t1.functions_sqrt(16) == 4
assert t1.functions_sqrt(2) > 0

# pow функция
assert t1.functions_pow(2, 2) == 4
assert t1.functions_pow(4, 2) == 16

# функция hypot
assert t1.functions_hypo(1, 2) > 0
assert t1.functions_hypo(2, 2) == math.sqrt(8)
assert t1.functions_hypo(5, 12) == 13

# функция filter
assert len(t1.filter_list((1, 2, 3, 4))) == 2
assert len(t1.filter_list((1, 3, 3, 7, 9, 9, 11, 31))) == 0

# функция map
assert t1.function_map([1, 2, 3]) == [2, 4, 6]
assert t1.function_map([1, 1, 1]) == [2, 2, 2]
assert t1.function_map([-1, -1, -1]) == [-2, -2, -2]
assert len(t1.function_map([-1, -1, -1, 3, 4, 5, 5, 4, 4, 4])) == len([-1, -1, -1, 3, 4, 5, 5, 4, 4, 4])

# функция sorted
tmp = [1, 3, 4, 32, 2, 11, 5]
tmp2 = ['kirill', 'ivan', 'kristina', 'roman', 'anton']
assert len(t1.function_sort(tmp)) == len(tmp)
assert len(t1.function_sort(tmp2)) == len(tmp2)
assert t1.function_sort(tmp)[0] == 1
assert t1.function_sort(tmp)[6] == 32
assert int(t1.function_sort(tmp)[0]) < int(t1.function_sort(tmp)[int(len(tmp) - 1)])
assert t1.function_sort(tmp2)[0] == 'anton'
assert t1.function_sort(tmp2)[4] == 'roman'

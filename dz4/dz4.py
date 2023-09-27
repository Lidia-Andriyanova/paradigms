# Функциональная, процедурная, структурная парадигмы

def average(nums):
    return sum(nums)/len(nums)


def Pirson(arr_x, arr_y):
    avg_x = average(arr_x)
    avg_y = average(arr_y)
    diff_x = list(map(lambda num: num - avg_x, arr_x))
    diff_y = list(map(lambda num: num - avg_y, arr_y))
    mult_xy = list(map(lambda x, y: x * y, diff_x, diff_y))
    sqrt_x = list(map(lambda num: num ** 2, diff_x))
    sqrt_y = list(map(lambda num: num ** 2, diff_y))
    sum_mult_xy = sum(mult_xy)
    sum_sqrt_x = sum(sqrt_x)
    sum_sqrt_y = sum(sqrt_y)
    return sum_mult_xy / ((sum_sqrt_x * sum_sqrt_y) ** 0.5)


array1 = [6, 12, 13, 17, 22, 25, 27, 29, 30, 32]
array2 = [45, 47, 39, 58, 68, 76, 75, 74, 78, 81]

print(array1)
print(array2)
print('Коэффициент корреляции Пирсона:', Pirson(array1, array2))
# FizzBuzz. Напишите программу, которая через пробел выводит числа от 1 до 100,
# но вместо чисел, которые делятся на 3 она пишет Fizz, вместо чисел, которые делятся на 5 – Buzz,
# а вместо чисел, которые делятся и на 3, и на 5 – FizzBuzz.

# for num in range(1, 101):
#     if (num % 3 == 0) and (num % 5 == 0):
#         print('FizzBuzz', end=' ')
#     elif num % 3 == 0:
#         print('Fizz', end=' ')
#     elif num % 5 == 0:
#         print('Buzz', end=' ')
#     else:
#         print(num, end=' ')

# Есть массив положительных и отрицательных чисел.
# Надо положительные числа перенести в начало массива в том порядке, в котором они изначально шли.
# Что случится с отрицательными числами нам не важно.
# Массив предполагается очень большим.
# [10, -1, -2, 3, 4, 6] -> [10,3, 4, 6, 0, 0], [10, 3, 4, 6, 4, 6], [10, 3, 4, 6, -1, -2]

arr = [-12, 5, -7, -56, 10, -1, 20, -2, 3, 4, 6]

# arr_result = []
# count_negative = 0
#
# for i in arr:
#     if i > 0:
#         arr_result.append(i)
#     else:
#         count_negative += 1
#
# arr_result.extend([0 for i in range(count_negative)])
# print(arr_result)

# for i, a in enumerate(arr):
#     if arr[i] < 0:


def func1():
    a = [10, -1, -2, 3, 4, 6]
    cursor = 0
    for idx in range(len(a)):
        if a[idx] > 0:
            a[cursor] = a[idx]
            cursor += 1
    print(a)

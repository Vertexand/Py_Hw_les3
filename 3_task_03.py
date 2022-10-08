# 3/  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


def list_rand_nums(n: int):
    list = []
    if n <= 0:
        print("don't put a minus!")
        return [0]

    for i in range(n):
        list.append(round(uniform(1, n), 2))
    return list
   

def dif_max_min(list_nums: list):
    max = min = list_nums[0] % 1

    for k in range(1, len(list_nums)):
        num = round(list_nums[k] % 1, 2)
        if num > max:
            max = num
        elif num < min:
            min = num

    result = round(max - min, 2)
    print(f"Min: {min}, Max: {max}")
    return result


all_list = list_rand_nums(int(input("n of numbers: ")))
print(all_list)
print(dif_max_min(all_list))


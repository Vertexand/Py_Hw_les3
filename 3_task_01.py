# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. # Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from random import sample


def rand_list(n: int):
    if n < 0:
        print("don't put a minus")
        return []

    list_nums = sample(range(0, 11), n)
    return list_nums

def sum_odd_pos(list_nums):
    sum_nums = 0
    for i in range(1, len(list_nums), 2):
        sum_nums += list_nums[i]
    return sum_nums

all_list = rand_list(int(input("n of numbers: ")))
print(all_list)
print(sum_odd_pos(all_list))


# list = [1,2,3,4,5]#вар 2
# sum = 0
# for i in range(1, len(list), 2):
#     sum += list[i]
# print(sum)

# list = [1, 2, 3, 4, 5]  # 3 вар
# sum = 0
# i = 1
# while i <= len(list):
#     sum += i
#     i += 2
# print(sum)
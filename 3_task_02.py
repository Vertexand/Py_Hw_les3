#  2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6] #вар 1 
res_list = []

for i in range(len(my_list)//2):
    res_list.append(my_list[i]*my_list[-i-1])

if len(my_list)%2 != 0:
    res_list.append(my_list[len(my_list)//2] ** 2)
    
print(res_list)


# from random import sample # вар 2


# def list_rand_nums(count):
#     if count < 0:
#         print("Negative value of the number of numbers!")
#         return []

#     list_nums = sample(range(1, count * 2), count)
#     return list_nums


# def prod_pairs(list_nums: list):
#     res_list = []
#     len_list = len(list_nums)

#     for k in range(len_list // 2):
#         res_list.append(list_nums[k] * list_nums[len_list - k - 1])

#     if len_list % 2:
#         res_list.append(list_nums[len_list // 2])
#     return res_list


# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(prod_pairs(all_list))












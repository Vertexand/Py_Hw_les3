#  2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# my_list = [2, 3, 4, 5, 6] #зад 
# res_list = []

# for i in range(len(my_list)//2):
#     res_list.append(my_list[i]*my_list[-i-1])

# if len(my_list)%2 != 0:
#     res_list.append(my_list[len(my_list)//2] ** 2)
    
# print(res_list)


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




# import math
# list = [2, 3, 4, 5, 6,7]
# result = []              

# n = math.ceil(len(list) / 2)                 #floor округление к меньшему #ceil округление к большему
# for i in range(n):
#     result.append(list[i] * list[-i - 1])
# print(result)

# from random import randrange

# def multiplication_of_pairs(new_list):
#     right_side = new_list[int(len(new_list)/2):]
#     right_side.reverse()
#     if len(new_list)%2 !=0:
#         left_side = new_list[:int(len(new_list)/2)+1]
#     else:
#         left_side = new_list[:int(len(new_list)/2)]
#     result_list = [l_value*r_value for l_value, r_value in zip(left_side, right_side)]   
#     return result_list


# new_list = [value for value in range(1, randrange(4,20))]
# print(new_list)
# print(multiplication_of_pairs(new_list))


# from random import randrange# вар из семир чел

# def multiplication_of_pairs(new_list):
#     right_side = new_list[int(len(new_list)/2):]
#     right_side.reverse()
#     if len(new_list)%2 !=0:
#         left_side = new_list[:int(len(new_list)/2)+1]
#     else:
#         left_side = new_list[:int(len(new_list)/2)]
#     result_list = [l_value*r_value for l_value, r_value in zip(left_side, right_side)] #генератор списка  зип сшивает два массива  
#     return result_list


# new_list = [value for value in range(1, randrange(4,20))]
# print(new_list)
# print(multiplication_of_pairs(new_list))
# n=[1,2,3,4,5,6,7]
# print(n[4:1:-1])
# print(n[::-1])
# print(n[1:6])# 

# print([0 for i in range(23)]) #все 0

my_list = [2, 3, 4, 5, 1] # задача сем
res_list = []
half_steps = len(my_list)//2

if len(my_list)%2 != 0:
    half_steps +=1
for i in range(half_steps):
    res_list.append(my_list[i]*my_list[-i-1])

print(res_list)





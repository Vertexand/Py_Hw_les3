# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи in 8 out -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in 5 out 5 -3 2 -1 1 0 1 1 2 3 5


# num = 8# мануилов семин 5
# my_list = [1, 0, 1]
# for _ in range(1, num):
#     print(my_list[0], my_list[1] - my_list[0])
#     print(my_list[-1], my_list[-2] + my_list[-1])
#     my_list.append(my_list[-2] + my_list[-1])
#     my_list.insert(0, my_list[1] - my_list[0])


# def fib(n):
#     a = 0
#     b = 1
#     for __ in range(n):
#         a, b = b, a + b
#     return a


# from random import randrange #только в одну правую сторону

# new_list = [0, 1]

# for number in range(8):
#     new_list.append(new_list[number-1]+new_list[number-2])
# else:
#     new_list = [-val for val in new_list[:0:-1]] + new_list
# print(new_list)

# def input_numbers (): # никита коптелов
#     while True :
#         numb = input('введите число - ')
#         try:
#             numbers = int(numb)
#             return numbers
#         except:
#             print('не число')

# def get_two_numb (num):
#     numb_1 = 1
#     numb_2 = 1
#     fibo_nums = []
#     for i in range(num):
#         fibo_nums.append(numb_1) #добавляет в конец
#         numb_1, numb_2 = numb_2, numb_1 + numb_2
#     numb_1 = 0
#     numb_2 = 1
#     for i in range(num+1):
#         fibo_nums.insert(0, numb_1)# место указыв и
#         numb_1, numb_2 = numb_2, numb_1 - numb_2
#     return fibo_nums


# # number = input_numbers()
# print(f'числа негафибаначчи - {get_two_numb(number)}')

negafib = [1, 0] #николай
for i in range(8):
    negafib.insert(0, negafib[1] - negafib[0])
for i in range(9):
    negafib.append(negafib[-2] + negafib[-1])

print(negafib)

# n = int(input('Задайте число: ')) #кирилл

# l = list()
# l2 = []
# f1 = 0
# f2 = 1
# for i in range(n):
#     f1,f2 = f2,f1 - f2
#     l.append(f1)
# l.reverse()
# l.append(0)
# for i in range(len(l)):
#     l2.append(abs(l[i]))
# l2.reverse()
# lst = l + l2[1:]
# print(lst)

# #ыыыыыыыыыыыыыы гая
# import math

# user_n = abs(int(input("Input Fibonacci N: ")))
# list_negative = []
# list_positive = []

# def fibonacci(n):
#     if n == -1:
#         return 1
#     elif n == -2:
#         return -1
#     elif n in [1, 2]:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# for i in range(0, user_n + 1):
#     list_negative.insert(0, fibonacci(i) * ((-1)**(i+1)))

# for i in range(1, user_n + 1):
#     list_negative.append(fibonacci(i))
# #print(list_negative)
# for i in list_negative:
#      print(i, end = "    ")


# def concatenatio(*params):# здесь строки, возмож передачи больш колич аргуменв
#     res: str = "" #переменная : тип данных
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ... числа не работ, здесь склеивание срок


# def concatenatio(*params):# здесь числа, возмож передачи больш колич аргуменв
#     # res: int = 0 #переменная : тип данных так делать можно но не нужно
#     res=0
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4)) #  10  TypeError: ... числа не работ, здесь склеивание срок


# def fib(n):  # лекция 2
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# # print(list)  # 1 1 2 3 5 8 13 21 34
# def fib2(n):
#     if n in [0]:
#         return 0
#     if n in [-1]:
#         return 1
#     else:
#         return fib2(n+2) - fib2(n+1)
# l = []
# for e in range (-9,1):
#     l.append(fib2(e))
# print(l, list)


# print(colors)
# t = tuple( l) # tuple( list) список в кортеж
# print(t)

# def concatenatio(*params):# возмож передачи больш колич аргуменв
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw соеденило строки


#     list1.append(fib(e)*(−1)**(n+1))
# F−n = (−1)**(n+1)Fn.

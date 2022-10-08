# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101 ; 3 -> 11;  2 -> 10

def conv_bin(num: int):
    list = []

    while num > 0:
        list.insert(0, num % 2)
        num //= 2

    print(*list, sep="")


conv_bin(int(input('Введите число: ')))
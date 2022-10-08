# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи in 8 out -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in 5 out 5 -3 2 -1 1 0 1 1 2 3 5

negafib = [1, 0] 
for i in range(8):
    negafib.insert(0, negafib[1] - negafib[0])
for i in range(9):
    negafib.append(negafib[-2] + negafib[-1])

print(negafib)


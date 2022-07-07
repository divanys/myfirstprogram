#Создание матриц(2 курс), ведёт Манакова(или типа как-то так), всё в одном файле, задачи>
#> не все(пару штук только подписано) подписаны, поэтому воображение))))

from random import randint

# a = randint(2, 6)
# b = randint(2, 6)
#
# matrix = [[randint(-10, 10) for j in range(b)] for i in range(a)] #создание матрицы(в данном случае квадратной)
#
# for i in matrix:
#     print(*i, sep='\t')
#
# for i in range(a):
#     for j in range(b):
#         if matrix[i][j] < 0 :
#             matrix[i][j] = matrix[i][j] ** 2
#
# print('vjihsghdifvojwhqeghvfnwjisdhvfwiehhvfjhsdgv')
#
# for i in matrix:
#     print(*i, sep='\t')


# rows = randint(2, 6)
# colums = randint(2, 6)
# matrix1 = [[randint(-10, 10) for j in range(colums)] for i in range(rows)] #создание матрицы(в данном случае квадратной)
# Positive = False
#
# for i in matrix1:
#     for j in i:
#         if j > 0:
#             Positive = True
# for i in matrix1:
#     print(*i, sep='\t')
# print(Positive)
# print(type(i), type(j))

# rows = randint(2, 6)
# colums = randint(2, 6)
# matrix1 = [[randint(-10, 10) for j in range(colums)] for i in range(rows)] #создание матрицы(в данном случае квадратной)
#
# for i in matrix1:
#     print(*i, sep='\t')
#
# for i in range(rows):
#     for j in range(colums):
#         if j == 1:
#             matrix1[i][j] = matrix1[i][j] ** 2
#
# for i in matrix1:
#     print(*i, sep='\t')

# rows = randint(2, 6)
# colums = randint(2, 6)
# matrix1 = [[randint(-10, 10) for j in range(colums)] for i in range(rows)] #создание матрицы(в данном случае квадратной)
#
# for i in matrix1:
#     print(*i, sep='\t')
#
# for i in range(rows):
#     for j in range(colums):
#         if matrix1[i][j] % 2 == 1:
#             matrix1[i][j] = 0
#
# for i in matrix1:
#     print(*i, sep='\t')

#
# rows = randint(2, 6)
# colums = randint(2, 6)
# matrix1 = [[randint(-10, 10) for j in range(colums)] for i in range(rows)] #создание матрицы(в данном случае квадратной)
#
# k = int(input())
# for i in matrix1:
#     print(*i, sep='\t')
#
# for i in range(rows):
#     matrix1[i][k-1] = matrix1[i][k-1] * 2
#
# print('vqerjbvbvhbqkckqklwwrklhqgwpvuawhviqueyruiejnwojtgno;pivj0ew')
#
# for i in matrix1:
#     print(*i, sep='\t')

#
# rows = randint(2, 6)
# colums = randint(2, 6)
# matrix1 = [[randint(-10, 10) for j in range(colums)] for i in range(rows)] #создание матрицы(в данном случае квадратной)
#
# for i in matrix1:
#     print(*i, sep='\t')
#
# print('vqerjbvbvhbqkckqklwwrklhqgwpvuawhviqueyruiejnwojtgno;pivj0ew')
# for i in range(rows):
#     for j in range(colums):
#         matrix1[i][-1] = -1
# for i in matrix1:
#     print(*i, sep='\t')


# rows = randint(2, 6)
# colums = randint(2, 6)
#
# matrix2 = [[randint(-10, 10) for j in range(colums)] for i in range(rows)]
#
# print('Вывод первой матрицы')
# for i in matrix2:
#     print(*i, sep='\t')
#
# print('jnasfkjbaskbnkjnkmv')
#
# for i in range(rows):
#     for j in range(colums):
#         matrix2[-1][j] = 0
# print('Вывод второй матрицы')
# for i in matrix2:
#     print(*i, sep='\t')
#
# rows = randint(2, 6)
# colums = randint(2, 6)
#
# matrix2 = [[randint(1, 3) for j in range(colums)] for i in range(rows)]
#
# print('Вывод первой матрицы')
# for i in matrix2:
#     print(*i, sep='\t')
#
# k = int(input())
#
# print('jnasfkjbaskbnkjnkmv')
#
# print('Сумма: ', list(map(sum, zip(*matrix2)))[k-1])
#
# print('Вывод второй матрицы')
# for i in matrix2:
#     print(*i, sep='\t')


#для каждой нечётной строки матрицы найти срАриф
#
# rows = randint(2, 6)
# columns = randint(2, 6)
# matrix = [[randint(-2, 2) for j in range(columns)] for i in range(rows)]
# n = []
#
# for i in matrix:
#     print(*i, sep='\t')
#
# for i in range(rows):
#     summ = 0
#     for j in range(columns):
#         if (i + 1) % 2 == 1:
#             summ += matrix[i][j]
#         n.append(summ)
#     if (i + 1) % 2 == 1:
#         print(n[-1]/2)
#
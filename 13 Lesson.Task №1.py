import random

# Функция сложения матриц
def add_matrices(matrix_1, matrix_2):
    # Проверка размерности матриц
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        # Инициализация матрицы результата
        matrix_3 = [[0] * len(matrix_1[0]) for _ in range(len(matrix_1))]
        # Сложение матриц
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]
        return matrix_3
    else:
        print("Матрицы разной размерности!")
        return None

# Создание матриц заданной размерности
matrix_1 = [[random.randint(-100, 100) for _ in range(10)] for _ in range(10)]
matrix_2 = [[random.randint(-100, 100) for _ in range(10)] for _ in range(10)]

# Вывод матриц
print("Matrix 1:")
for row in matrix_1:
    print(row)

print("\nMatrix 2:")
for row in matrix_2:
    print(row)

# Сложение матриц
matrix_3 = add_matrices(matrix_1, matrix_2)
if matrix_3:
    print("\nMatrix 3:")
    for row in matrix_3:
        print(row)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

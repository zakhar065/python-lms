# Ввод количества чисел
N = int(input())

# Ввод чисел через пробел и разделение их в список чисел
numbers = list(map(int, input().split()))

# Создание множества уникальных чисел
unique_numbers = set(numbers)

# Вывод количества уникальных чисел
print(len(unique_numbers))


print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

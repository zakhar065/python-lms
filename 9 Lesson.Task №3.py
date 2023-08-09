# Ввод последовательности чисел через пробел
sequence = list(map(int, input().split()))

# Создание множества для хранения уникальных чисел
unique_numbers = set()

# Перебор чисел в последовательности
for number in sequence:
    # Проверка, является ли число повторным или новым
    if number in unique_numbers:
        print("YES")
    else:
        print("NO")
    
    # Добавление числа в множество
    unique_numbers.add(number)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

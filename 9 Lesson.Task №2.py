# Ввод чисел первого списка
list1 = set(map(int, input().split()))

# Ввод чисел второго списка
list2 = set(map(int, input().split()))

# Подсчет чисел, содержащихся одновременно в обоих списках
common_numbers = len(list1.intersection(list2))

# Вывод количества общих чисел
print(common_numbers)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

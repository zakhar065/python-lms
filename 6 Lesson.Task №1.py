N = int(input("Введите число N: "))
count = 0

for _ in range(N):
    num = int(input("Введите число: "))
    if num == 0:
        count += 1

print("Количество чисел, равных нулю:", count)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

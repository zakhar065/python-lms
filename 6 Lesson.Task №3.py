A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

for i in range(A, B + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

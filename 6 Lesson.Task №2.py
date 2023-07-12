import math

X = int(input("Введите число X: "))
count = 0

sqrtX = int(math.sqrt(X))

for i in range(1, sqrtX + 1):
    if X % i == 0:
        count += 1
        if X // i != i:
            count += 1

print("Количество натуральных делителей числа X:", count)
print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

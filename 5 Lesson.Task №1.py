number = int(input("Введите число: "))

if number > 0 and number % 2 == 0:
    print("положительное четное число")
elif number > 0 and number % 2 != 0:
    print("положительное нечетное число")
elif number < 0 and number % 2 == 0:
    print("отрицательное четное число")
elif number < 0 and number % 2 != 0:
    print("отрицательное нечетное число")
else:
    print("нулевое число")

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

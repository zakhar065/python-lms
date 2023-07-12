X = int(input("Введите минимальную сумму инвестиций: "))
A = int(input("Введите сумму денег, которую имеет Майкл: "))
B = int(input("Введите сумму денег, которую имеет Иван: "))

if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

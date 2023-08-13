def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_list(n):
    factorials = [factorial(i) for i in range(n, 0, -1)]
    return factorials

number = int(input("Введите число: "))
result = factorial_list(number)
print(result)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

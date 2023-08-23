def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_list(n):
    factorial_n = factorial(n)
    factorials = []
    for i in range(factorial_n, 0, -1):
        factorials.append(factorial(i))
    return factorials

number = int(input("Введите число: "))
result = factorial_list(number)
print(result)
print("консоль закроется через 60 секунд...")
import time
time.sleep(60)

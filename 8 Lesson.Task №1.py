N = int(input())

numbers = 
for i in range(N):
    number = int(input())
    numbers.append(number)

numbers.reverse()

for number in numbers:
    print(number)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

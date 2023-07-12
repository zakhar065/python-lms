m = int(input())
n = int(input())

weights = 
for i in range(n):
    weight = int(input())
    weights.append(weight)

weights.sort()

boats = 0
i = 0
j = n - 1

while i <= j:
    if weightsi + weightsj <= m:
        i += 1
        j -= 1
    else:
        j -= 1
    boats += 1

if i == j:
    boats += 1

print(boats)
print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

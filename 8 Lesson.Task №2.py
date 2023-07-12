def changearray(arr):
    arr.reverse()
    return arr

N = int(input())
arr = list(map(int, input().split()))
result = changearray(arr)
for num in result:
    print(num, end=" ")
print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

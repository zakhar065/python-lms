def shiftarray(arr):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

N = int(input())
arr = list(map(int, input().split()))

result = shiftarray(arr)

for num in result:
    print(num, end=" ")

print("консоль закроется через 60 секунд...")
import time
time.sleep(60)

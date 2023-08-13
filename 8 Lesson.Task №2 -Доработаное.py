def shift_array(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    return arr

N = int(input())
arr = list(map(int, input().split()))

result = shift_array(arr)

for num in result:
    print(num, end=" ")

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

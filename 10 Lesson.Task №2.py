my_dict = {}

for number in range(10, -6, -1):
    my_dict[number] = number ** number

print(my_dict)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

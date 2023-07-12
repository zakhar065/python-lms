string = input("Введите строку: ")

if string == string[::-1]:
    print("yes")
else:
    print("no")



print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

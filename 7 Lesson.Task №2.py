string = input("Введите строку: ")
result = ""

for i in range(len(string)):
    if string[i] != " ":
        result += string[i]
    elif i > 0 and string[i-1] != " ":
        result += " "

print(result)
print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

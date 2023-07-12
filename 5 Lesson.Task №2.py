word = input("Введите слово: ")

vowels = 0
consonants = 0

for letter in word:
    if letter.lower() in "aeiou":
        vowels += 1
    elif letter.isalpha():
        consonants += 1

if vowels == 0 or consonants == 0:
    print(False)
else:
    print("Количество гласных:", vowels)
    print("Количество согласных:", consonants)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

word = input("Введите слово: ")
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonants = 0

for letter in word.lower():
    if letter in vowels:
        vowels[letter] += 1
    elif letter.isalpha():
        consonants += 1

if all(value == 0 for value in vowels.values()) or consonants == 0:
    print(False)
else:
    print("Количество гласных:")
    for vowel, count in vowels.items():
        if count > 0:
            print(vowel + ":", count)
    print("Количество согласных:", consonants)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

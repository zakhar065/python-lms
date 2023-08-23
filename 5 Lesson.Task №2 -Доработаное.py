word = input("Введите слово: ")
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonants = 0
total_vowels = 0

for letter in word.lower():
    if letter in vowels:
        vowels[letter] += 1
        total_vowels += 1
    elif letter.isalpha():
        consonants += 1

if total_vowels == 0 or consonants == 0:
    print(False)
else:
    print("Количество гласных:", total_vowels)
    print("Количество каждой гласной:")
    for vowel, count in vowels.items():
        if count > 0:
            print(vowel + ":", count)
    print("Количество согласных:", consonants)


print("консоль закроется через 60 секунд...")
import time
time.sleep(60)

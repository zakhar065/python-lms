pet_type = input("Введите вид питомца: ")
age = input("Введите возраст питомца: ")
name = input("Введите кличку питомца: ")

sentence = f"Это {pet_type} по кличке \"{name}\". Возраст: {age} года."
print(sentence)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

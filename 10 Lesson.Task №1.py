pets = {}

name = input("Введите имя питомца: ")
species = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

pets[name] = {
    "Вид питомца": species,
    "Возраст питомца": age,
    "Имя владельца": owner
}

age_suffix = "год" if age == 1 else "года" if 2 <= age <= 4 else "лет"

info = f"Это {species} по кличке \"{name}\". Возраст питомца: {age} {age_suffix}. Имя владельца: {owner}"
print(info)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

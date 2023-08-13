class CashRegister:
    def __init__(self, money_amount):
        self.money = money_amount

    def top_up(self, amount):
        self.money += amount

    def count_1000(self):
        return self.money // 1000

    def take_away(self, amount):
        if amount <= self.money:
            self.money -= amount
        else:
            raise ValueError("Недостаточно денег в кассе")


# Пример использования класса CashRegister
# Создаем объект класса CashRegister с начальной суммой 5000
register = CashRegister(5000)

# Пополняем кассу на 2000
register.top_up(2000)
print("Текущая сумма в кассе:", register.money)

# Выводим сколько целых тысяч осталось в кассе
print("Осталось целых тысяч в кассе:", register.count_1000())

# Забираем из кассы 3000
register.take_away(3000)
print("Текущая сумма в кассе после изъятия:", register.money)

# Пытаемся забрать из кассы 10000, что вызовет ошибку
try:
    register.take_away(10000)
except ValueError as e:
    print("Ошибка:", str(e))


print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

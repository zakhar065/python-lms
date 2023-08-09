class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass

autobus = Autobus("Renault Logan", 180, 12)
print("Название автомобиля:", autobus.name)
print("Скорость:", autobus.max_speed)
print("Пробег:", autobus.mileage)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

class Transport:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

transport = Transport("Renault Logan", 180, 12)
print("Название автомобиля:", transport.name)
print("Скорость:", transport.maxspeed)
print("Пробег:", transport.mileage)

print("консоль закроется через 60 секунд...")
import time
time.sleep(60)


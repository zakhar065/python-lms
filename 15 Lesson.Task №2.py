class Transport: 
    def __init__(self, name, max_speed, mileage): 
        self.name = name 
        self.max_speed = max_speed 
        self.mileage = mileage 

    def seating_capacity(self, capacity): 
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):  
    def __init__(self, name, max_speed, mileage):  
        super().__init__(name, max_speed, mileage)  
      
    def seating_capacity(self, capacity=50):  
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"  
  
bus = Autobus("Renault Logan", 180, 12)  
print(bus.seating_capacity())
print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

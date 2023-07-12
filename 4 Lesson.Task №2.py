number = 46275

# Подсчет количества десятков, единиц и сотен
thousands = number // 10000
tensofthousands = number % 10000 // 1000
hundreds = number % 1000 // 100
tens = number % 100 // 10
units = number % 10

# Возведение количества десятков в степень количества единиц
powerresult = tens ** units

# Умножение результата на количество сотен
multiplicationresult = powerresult * hundreds

# Вычисление разности между количеством десятков тысяч и количеством тысяч
difference = tensofthousands - thousands

# Разделение результата на разность
finalresult = multiplicationresult / difference

print(finalresult)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

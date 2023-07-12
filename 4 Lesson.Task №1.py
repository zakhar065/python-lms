# Ввод сторон прямоугольника
length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))

# Вычисление площади
area = length * width

# Вычисление периметра
perimeter = 2 * (length + width)

# Вывод результатов
print("Площадь прямоугольника:", area)
print("Периметр прямоугольника:", perimeter)


print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

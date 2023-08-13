class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
   
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Невозможно уменьшить s")
    
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        return dx + dy
turtle = Turtle(0, 0, 1)
print("Начальная позиция черепашки:", turtle.x, turtle.y)
turtle.evolve()
print("Количество клеточек на каждом ходу после эволюции:", turtle.s)
turtle.go_up()
print("Новая позиция после хода вверх:", turtle.x, turtle.y)
turtle.degrade()
print("Количество клеточек на каждом ходу после обратного развития:", turtle.s)
moves = turtle.count_moves(3, 4)
print("Минимальное количество действий до (3, 4):", moves)

print("консоль закроется через 10 секунд...")
import time
time.sleep(10)

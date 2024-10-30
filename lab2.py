import random
import tkinter as tk
import math
import random
import json

def load_config():
    with open('rain.json', 'r') as f:
        return json.load(f)


class Droplet:
    def __init__(self, canvas):
        self.config = load_config()
        # Случайная начальная позиция капли
        self.x = random.randint(0, self.config['width'])
        self.y = random.randint(0, self.config['height'])
        self.size = random.randint(self.config['min_droplet_size'], self.config['max_droplet_size'])


        self.speed = random.uniform(self.config['min_speed'], self.config['max_speed'])
        self.angle = random.uniform(math.radians(self.config['min_angle']), math.radians(self.config['max_angle']))

        # Вычисляем смещение по оси X и Y
        self.dx = self.speed * math.sin(self.angle)
        self.dy = self.speed * math.cos(self.angle)

        # Рисуем каплю
        self.canvas = canvas
        self.droplet = canvas.create_line(self.x, self.y, self.x + self.dx, self.y + self.size, fill='blue', width=2)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y > self.config['height']:
            self.y = 0
            self.x = random.randint(0, self.config['width'])

        # Перемещаем каплю на новое место
        self.canvas.coords(self.droplet, self.x, self.y, self.x + self.dx, self.y + self.size)


class RainSimulation:
    def __init__(self, root):
        self.config = load_config()
        self.canvas = tk.Canvas(root, width=self.config['width'], height=self.config['height'], bg='grey')
        self.canvas.pack()

        self.droplets = [Droplet(self.canvas) for _ in range(self.config['density'])]

        self.animate()

    def animate(self):
        for droplet in self.droplets:
            droplet.move()

        # Обновляем анимацию каждые 20 миллисекунд
        self.canvas.after(20, self.animate)


# Создание окна и запуск симуляции
root = tk.Tk()
root.title("Rain Simulation")

# Запуск симуляции дождя
rain_sim = RainSimulation(root)

# Основной цикл tkinter
root.mainloop()


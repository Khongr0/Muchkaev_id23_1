import random
import tkinter as tk
import math
import random

class AnimatedPointApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()

        self.center_x = 300
        self.center_y = 300
        self.radius = 200

        self.circle = self.canvas.create_oval(self.center_x - self.radius,
                                              self.center_y - self.radius,
                                              self.center_x + self.radius,
                                              self.center_y + self.radius,
                                              fill='red')


        self.angle = 0
        self.point = self.canvas.create_oval(self.center_x - 5, self.center_y - 5,
                                             self.center_x + 5, self.center_y + 5,
                                             fill='blue')

        self.animate()

    def animate(self):
        x = self.center_x + self.radius * math.cos(math.radians(self.angle))
        y = self.center_y + self.radius * math.sin(math.radians(self.angle))

        self.canvas.coords(self.point, x - 5, y - 5, x + 5, y + 5)

        self.angle += 1

        self.root.after(10, self.animate)


root = tk.Tk()
root.title("Animated Point on Circle")

app = AnimatedPointApp(root)

root.mainloop()
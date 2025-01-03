import tkinter as tk
from tkinter import ttk
import math

RHO_AIR = 1.225
G = 9.81

def calculate_height(v0, volume, massa, time):
    buoyant_force = volume * RHO_AIR * G
    gravity_force = massa * G
    net_force = buoyant_force - gravity_force
    accel = net_force / massa
    height = v0 * time + 0.5 * accel * time ** 2
    return max(height, 0)

def start_animation():
    volume = volume_slider.get()
    mass = mass_spinbox.get()
    initial_speed = speed_slider.get()

    mass = float(mass)
    volume = float(volume)
    initial_speed = float(initial_speed)

    reset_animation()

    time = 0
    while True:
        height = calculate_height(initial_speed, volume, mass, time)
        canvas.coords(ball, 190, 400 - height, 210, 420 - height)
        canvas.update()
        if height <= 0 and time > 0:  # Если шар остановился
            break
        time += 0.1
        root.after(50)

def reset_animation():
    canvas.coords(ball, 190, 400, 210, 420)
    canvas.update()

root = tk.Tk()
root.title("Симуляция запуска воздушного шара")
frame = ttk.Frame(root)
frame.pack(pady=10)
ttk.Label(frame, text="Объем шара (м³):").grid(row=0, column=0, padx=5, pady=5)
volume_slider = ttk.Scale(frame, from_=1, to_=10, length=200, orient="horizontal")
volume_slider.set(8)
volume_slider.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(frame, text="Масса груза (кг):").grid(row=1, column=0, padx=5, pady=5)
mass_spinbox = ttk.Spinbox(frame, from_=1, to_=50, width=10)
mass_spinbox.set(10)
mass_spinbox.grid(row=1, column=1, padx=5, pady=5)
ttk.Label(frame, text="Начальная скорость (м/с):").grid(row=2, column=0, padx=5, pady=5)
speed_slider = ttk.Scale(frame, from_=0, to_=20, length=200, orient="horizontal")
speed_slider.set(5)
speed_slider.grid(row=2, column=1, padx=5, pady=5)
start_button = ttk.Button(frame, text="Запуск", command=start_animation)
start_button.grid(row=3, column=0, padx=5, pady=5)
reset_button = ttk.Button(frame, text="Сброс", command=reset_animation)
reset_button.grid(row=3, column=1, padx=5, pady=5)
canvas = tk.Canvas(root, width=400, height=400, bg="skyblue")
canvas.pack(pady=10)
ball = canvas.create_oval(190, 400, 210, 420, fill="red")
root.mainloop()
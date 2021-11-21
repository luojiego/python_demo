# 面向过程示例 3
from random import random
 
def move_cars():
    for i, _ in enumerate(car_positions):
        if random() > 0.3:
            car_positions[i] += 1
 
def draw_car(car_position):
    print ('-' * car_position)
 
def run_step_of_race():
    global time
    time -= 1
    move_cars()
 
def draw():
    print ('')
    for car_position in car_positions:
        draw_car(car_position)
 
time = 5
car_positions = [1, 1, 1]
 
while time:
    run_step_of_race()
    draw()
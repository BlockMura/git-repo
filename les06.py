# coding: utf-8

import turtle
import random
import math

PHI = 360 / 7
R = 70

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    
def draw_gun(base_x,base_y):
    #рисуем основной круг
    gotoxy(base_x,base_y)
    turtle.circle(100)
    # рисуем мушку
    gotoxy(base_x,base_y + 200)
    draw_circle(5, 'red')
    # рисуем пулевые отверстия
    for i in range(0,7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad)*R, base_y + math.cos(phi_rad)*R + 72)
        draw_circle(29, 'white')

        
def run_gun(base_x,base_y, start):
    for i in range(start, random.randrange(7,100)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad)*R, base_y + math.cos(phi_rad)*R + 72)
        draw_circle(29, 'brown')
        draw_circle(29, 'white')
        
    draw_circle(29,'brown')
    gotoxy(base_x + math.sin(phi_rad)*R, base_y + math.cos(phi_rad)*R + 72)
    return i % 7
        
turtle.speed(0)

draw_gun(100,100)

answer = ''
start = 0

while answer != 'N':
    answer = turtle.textinput("Играть?", "Y/N")
    if answer == 'Y':
        start = run_gun(100, 100, start) 
     
    if start == 0:
        gotoxy(-150,200)
        turtle.write("Вы проиграли", font=("Arial", 18, "normal"))
        
    else:
        pass        
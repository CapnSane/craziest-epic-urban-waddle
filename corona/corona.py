from turtle import *

def corona(x):
    color('green')
    bgcolor('black')
    speed(11)
    hideturtle()
    b=0
    while b<x:
            right(b)
            forward(b*3)
            b=b+1

corona(200)

import turtle
import time
import random

window = turtle.Screen()
height = 400
width = 400
window.setup(height, width)
window.bgcolor("black")
window.title("Snake Game")

trt = turtle.Turtle()
trt.shape("square")
trt.color("white")
trt.speed(1)
trt.penup()

apple = turtle.Turtle()
apple.shape("square")
apple.color("red")
apple.speed(0)
apple.penup()

move_dist = 20

facing = "right"

def get_rand_coord():
    rand_x = random.randrange(0, width // 2, move_dist) 
    rand_y = random.randrange(0, height // 2, move_dist)

    return (rand_x, rand_y)

def get_apple():
    x, y = get_rand_coord()

    apple.setx(x)
    apple.sety(y)

def up():
    global facing
    facing = "up"
        
def down():
    global facing
    facing = "down"

def right():
    global facing
    facing = "right"

def left():
    global facing
    facing = "left"

def move(direction):
    if direction == "up":
        trt.sety(trt.ycor() + move_dist)
    elif direction == "down":
        trt.sety(trt.ycor() - move_dist)
    elif direction == "left":
        trt.setx(trt.xcor() - move_dist)
    else:
        trt.setx(trt.xcor() + move_dist)

apple_is_spawned = False
tail_q = []
tail_q.append(trt)
tail_len = 0

while True:
    if not apple_is_spawned:
        get_apple()
        apple_is_spawned = True

    
    # enqueue current position
    move(facing)


    for i in range(len(tail_q)-1, 0, -1):
        tail_q[i].goto(tail_q[i-1].pos())


    is_x_bounds = int(trt.xcor()) == width // 2 or int(trt.xcor()) == -width // 2
    is_y_bounds = int(trt.ycor()) == height // 2 or int(trt.ycor()) == -height // 2 


    if is_x_bounds or is_y_bounds:
        print("GAME OVER")
        break

    if trt.xcor() == apple.xcor() and trt.ycor() == apple.ycor():
        x, y = trt.pos()
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("white")
        segment.speed(1)
        segment.penup()
        tail_q.append(segment)
        apple_is_spawned = False


    window.onkey(up, "Up")
    window.onkey(down, "Down")
    window.onkey(right, "Right")
    window.onkey(left, "Left")

    window.listen()



window.mainloop()

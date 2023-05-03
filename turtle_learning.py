import turtle, time, math
colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
petals = int(input('how many petals would you like on your rosette?\n'))
width = int(input('how wide would you like the pen to be? default is 1.\n'))
speed = int(input('how fast would you like the turtle to be? defualt is 100.\n'))
turtle.Screen().setup(width=0.5, height=0.75, startx=None, starty=None)
i = 0
color_number = 0
turtle.speed(100000)
turtle.width(width)
while i in range(petals):
    turtle.color(colors[color_number])
    color_number += 1
    if color_number > 5:
        color_number = 0
    r = 0
    for r in range(2):
        turtle.circle(100, 90)
        turtle.circle(100//2, 90)
        r += 1
    turtle.right(360 / petals)
    i = i + 1
i = 0
while i in range(2):
    turtle.right(1)
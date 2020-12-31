from turtle import *


def repression(length, num_rep):
    if num_rep == 0:
        forward(length)
        return
    repression(length, num_rep - 1)
    left(60)
    repression(length, num_rep - 1)
    right(120)
    repression(length, num_rep - 1)
    left(60)
    repression(length, num_rep - 1)


def snowflake(pen_size, color_name, length, num_for, num_rep):
    pensize(pen_size)
    color(color_name)
    for i in range(num_for):
        repression(length, num_rep)
        left(60)
        repression(length, num_rep)
        right(120)


begin_fill()
# speed(#here is number)
"""
The turtle’s speed lies in the range 0-10.
If input is a number greater than 10 or smaller than 0.5, speed is set to 0.
Speedstrings  are mapped to speedvalues in the following way:
‘fastest’ :  0
‘fast’    :  10
‘normal’  :  6
‘slow’    :  3
‘slowest’ :  1
Speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning.
Write like that "speed(10)"
"""

# First snowflake (n = 2)
# """
penup()
goto(-120, 60)
pendown()
snowflake(3, "black", 9, 6, 2)
# """

# Second snowflake (n = 4)
"""
penup()
goto(-200, 140)
pendown()
snowflake(3, "black", 5, 6, 3)
"""

# Third snowflake (n = 8)
"""
penup()
goto(-240, 140)
pendown()
snowflake(3, "black", 2, 6, 4)
"""
        
horiz(9, 6)
color('cyan')
end_fill()

hideturtle()
exitonclick()

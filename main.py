import turtle as t
import random

tim = t.Turtle()

t.colormode(255)


def random_color():
    # function generates and returns random colour from python RGB colors
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_shape(num_sides):
    # function crates number of sides in range
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(80)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random_color())
    draw_shape(shape_side_n)

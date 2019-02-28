#
# Pearce Phanawong
# motion_parallax.py
# Description: This program displays a graphics user interface with
#              an image of some very basic mountains. The image is
#              made using graphics.py and the image has a slight
#              paralax effect based on the position of the mouse.
#              There is also several birds that wrap around the
#              interface.
#
#
#
from graphics import graphics
import random

def main():
    gui = graphics(500, 500, 'Landscape')
    center = color()
    side1 = color()
    side2 = color()
    #this index is for the start position of the birds
    i = -350
    while True:
        gui.clear()
        background(gui)
        middle(gui, center)
        sides(gui, side1, side2)
        foreground(gui)
        birds(gui, i)
        i += 3
        if i >= 550:
            i = -350
        gui.update_frame(60)

def color():
    '''
    This function generates a random color, which will be used for
    picking the colors for the mountains.
    '''
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    mountain_color = graphics.get_color_string(0, red, green, blue)
    return mountain_color

def background(canvas):
    '''
    This function will make the background of the canvas blue and
    place the sun on there, which placement will vary slightly
    based on the position of the mouse on the canvas.
    '''
    x = (canvas.mouse_x / 64)
    y = (canvas.mouse_y / 64)
    canvas.rectangle(-50, -50, 600, 600, 'steelblue1')
    canvas.ellipse(x + 400, y + 50, 50, 50, 'yellow')


def middle(canvas, color):
    '''
    This function displays the mountain in the middle, which is the
    "furthest" mountain away. The position of the mountain will change
    slightly based on the position of the mouse and the color of it is
    random from the color function.
    '''
    x = (canvas.mouse_x / 32)
    y = (canvas.mouse_y / 32)
    canvas.triangle(x + 225, y + 150, x + 75, y + 550, x + 375, y + 450, color)

def sides(canvas, left, right):
    '''
    This function displays the two closer mountains and their positions change
    slightly based on the position of the mouse. Both mountains have randomly
    generated colors from the color function.
    '''
    x1 = (canvas.mouse_x / 16)
    y1 = (canvas.mouse_y / 16)
    x2 = (canvas.mouse_x / 16)
    y2 = (canvas.mouse_y / 16)
    canvas.triangle(x1 + 95, y1 + 200, x1 - 45, y1 + 500,
                    x1 + 295, y1 + 500, left)
    canvas.triangle(x2 + 355, y2 + 200, x2 + 155, y2 + 500,
                    x2 + 555, y2 + 500, right)

def foreground(canvas):
    '''
    This function displays the foreground, which includes the grass, grass
    blades, and the tree. The position of this layer will change the most
    based on the position of the mouse.
    '''
    x = (canvas.mouse_x / 8)
    y = (canvas.mouse_y / 8)
    i = 50
    while i >=  -25:
        canvas.line(x + i * 15, y + 390, x + i * 15, y + 400, 'green', 3)
        i -= 1
    canvas.rectangle(x - 100, y + 400, 600, 150, 'green')
    canvas.rectangle(x + 375, y + 390, 25, 60, 'brown')
    canvas.ellipse(x + 388, y + 350, 60, 100, 'green')

def birds(canvas, x):
    '''
    This function displays the birds and has the birds fly across from
    left to right of the canvas and has it wrap back around.
    '''
    i = 5
    while i > 0:
        j = i * 50
        canvas.line(x + 25 + j, 25 + j, x + 50 + j,  50 + j, 'black', 2)
        i -= 1
    i = 5
    while i > 0:
        j = i * 50
        canvas.line(x + 75 + j, 25 + j, x + 50 + j, 50 + j, 'black', 2)
        i -= 1


main()
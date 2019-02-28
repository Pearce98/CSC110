#
# Pearce Phanawong
# three.py
# Description: This program will create three different shapes of
#              three different colors and have them slide across
#              the display.
#

from graphics import graphics
import random

def main():
    #This creates the canvas
    gui = graphics(500, 500, 'Three Shapes')
    #This loop makes it so it repeats infinitely
    while True:
        #start at -100 so its off the screen
        i = -100
        #These are the three different height values for the shapes
        y1 = random.randint(0, 400)
        y2 = random.randint(50, 450)
        y3 = random.randint(0, 400)
        #This loop creates the 3 objects and has them scroll across the screen
        while i < 550:
            gui.clear()
            gui.rectangle(i - 50, y1, 100, 100, 'yellow')
            gui.ellipse(i, y2, 100, 100, 'blue')
            gui.triangle(i, y3, i - 50, y3 + 100, i + 50, y3 + 100, 'red')
            i += 6
            gui.update_frame(60)

main()
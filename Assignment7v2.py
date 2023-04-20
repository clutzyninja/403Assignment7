# ****************
# CMSC 403
# Assignment 7
# Brandon Binczak
# 4/6/23
# *****************

import random
import sys
import tkinter as tk
import rectpack
from rectpack import *


class CustomCanvas:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

    def draw_rectangle(self, rect):
        self.canvas.create_rectangle(rect.x, rect.y, rect.x + rect.width, rect.y + rect.height, outline="black",
                                     fill=rect.color)

    def run(self):
        self.root.mainloop()


class Rectangle:
    def __init__(self, height, width, x=0, y=0):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = self._get_random_color()

    @staticmethod
    def _get_random_color():
        colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']
        color = random.choice(colors)
        return color


def pack(allRect, canvasSize):
    p = newPacker()
    p.add_bin(canvasSize[1], canvasSize[0])
    for r in allRect:
        p.add_rect(r.height, r.width)
    p.pack()
    packed_rects = p.rect_list()
    return packed_rects


def main():
    filep = sys.argv[1]

    # Read canvas size and rectangles from file
    with open(filep, 'r') as file:
        canvas_size = tuple(map(int, file.readline().strip().split(',')))
        rectangles = []
        for line in file:
            height, width = map(int, line.strip().split(','))
            rectangles.append(Rectangle(height, width))

    # Pack rectangles on canvas
    packed_rectangles = pack(rectangles, canvas_size)

    # Create custom canvas and draw rectangles
    custom_canvas = CustomCanvas(canvas_size[0], canvas_size[1])
    for rect in packed_rectangles:
        rect_obj = Rectangle(rect[4], rect[3], rect[1], rect[2])
        custom_canvas.draw_rectangle(rect_obj)

    custom_canvas.run()


if __name__ == "__main__":
    main()

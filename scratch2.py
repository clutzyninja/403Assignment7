for rect in packed_rectangles:
    # pass
    rect_obj = Rectangle(rect[4], rect[3], rect[1], rect[2] + rect[4])
    custom_canvas.draw_rectangle(rect_obj)
    print(rect)
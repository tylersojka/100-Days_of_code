import math

test_h = int(input("what is the height of the wall "))
test_w = int(input("what is the width of the wall "))
coverage = 5

def paint(test_h, test_w):
    paint_cans = math.ceil(test_h * test_w / coverage)
    print(paint_cans)

paint(test_h, test_w)
    

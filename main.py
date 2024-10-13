from window import *
from cell import *


def main():
    win = Window(800,600)
    red_line = Line(point1=Point(100, 200), point2=Point(300,400))
    # cell_test = Cell(True, True, True, True, 0, 100, 0, 100, win=win)
    # cell_test.draw()
    
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)
    
    
    win.draw_line(red_line)
    win.wait_for_close()

main()
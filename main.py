from window import *
from cell import *


def main():
    win = Window(800,600)
    red_line = Line(point1=Point(100, 200), point2=Point(300,400))
    cell_test = Cell(True, True, True, True, 0, 100, 0, 100, win=win)
    cell_test.draw()
    win.draw_line(red_line)
    win.wait_for_close()

main()
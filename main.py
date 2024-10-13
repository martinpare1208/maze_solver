from window import *

def main():
    win = Window(800,600)
    red_line = Line(point1=Point(100, 200), point2=Point(300,400))
    win.draw_line(red_line)
    win.wait_for_close()

main()
from tkinter import Tk, BOTH, Canvas
from line import *
from cell import *

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.canvas_widget = Canvas(self.__root_widget, bg="white", height=height, width=width)
        self.canvas_widget.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close())
        

    def draw_line(self, line, fill_color):
        line.draw(self.canvas_widget, fill_color=fill_color)
    
    def redraw(self):
        self.__root_widget.update_idletasks
        self.__root_widget.update()

    def close(self):
        self.running = False
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print('Window closed.')
    
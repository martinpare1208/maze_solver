from tkinter import Tk, BOTH, Canvas
from point import *

class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2
        
    def draw(self, canvas, fill_color):
        print('Draw is being run')
        self.__canvas = canvas
        self.__canvas.create_line(self.__point1.x, self.__point1.y, self.__point2.x, self.__point2.y,  fill=fill_color, width=2)
        
        
        
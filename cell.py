from tkinter import Tk, BOTH, Canvas
from window import *

class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1,x2,y1,y2, win):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

        
    def draw(self):
        if self.has_bottom_wall: 
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y2), Point(self._x2, self._y1)))

        
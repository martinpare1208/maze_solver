from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title = 'Window'
        self.canvas_widget = Canvas(self.root_widget, bg="white", height=height, width=width)
        self.canvas_widget.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close())

    
    def redraw(self):
        self.root_widget.update_idletasks
        self.root_widget.update()

    def close(self):
        self.running = False
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print('Window closed.')
    
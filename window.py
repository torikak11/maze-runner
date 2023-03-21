from tkinter import Tk, Canvas
from line import Line, Point

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Maze Runner")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()

    def close(self):
         self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
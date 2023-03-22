
class Cell:
    def __init__(self, left, right, top, bottom, x1, y1, x2, y2, win):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.canvas = win.canvas

    def draw(self, fill_color):
        if self.has_left_wall:
            self.canvas.create_line(self.__x1, self.__y1, self.__x1, self.__y2, fill=fill_color, width=2)
        if self.has_right_wall:
            self.canvas.create_line(self.__x2, self.__y1, self.__x2, self.__y2, fill=fill_color, width=2)
        if self.has_top_wall:
            self.canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y1, fill=fill_color, width=2)
        if self.has_bottom_wall:
            self.canvas.create_line(self.__x1, self.__y2, self.__x2, self.__y2, fill=fill_color, width=2)

    def draw_move(self, to_cell, undo=False):
        start_x = (self.__x2 - self.__x1) // 2 + self.__x1
        start_y = (self.__y2 - self.__y1) // 2 + self.__y1
        end_x = (to_cell.__x2 - to_cell.__x1) // 2 + to_cell.__x1
        end_y = (to_cell.__y2 - to_cell.__y1) // 2 + to_cell.__y1
        if undo:
            self.canvas.create_line(start_x, start_y, end_x, end_y, fill="gray", width=2)
        else:
            self.canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=2)
        
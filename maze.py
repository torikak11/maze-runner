from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed
        if self._seed is not None:
            random.seed(self._seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(0, self._num_cols):
            col_cells = []
            for row in range(0, self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()
    
    def _draw_cell(self, i , j):
        if self._win is None:
            return
        x = self._x1 + (i * self._cell_size_x)
        y = self._y1 + (j * self._cell_size_y)
        x2 = x + self._cell_size_x
        y2 = y + self._cell_size_y
        self._cells[i][j].draw(x, y, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.04)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            directions = 0

            if i > 0 and self._cells[i-1][j].visited == False:
                to_visit.append((i-1, j))
                directions += 1
            if j > 0 and self._cells[i][j-1].visited == False:
                to_visit.append((i, j-1))
                directions += 1
            if i < self._num_cols - 1 and self._cells[i+1][j].visited == False:
                to_visit.append((i+1, j))
                directions += 1
            if j < self._num_rows - 1 and self._cells[i][j+1].visited == False:
                to_visit.append((i, j+1))
                directions += 1

            if directions == 0:
                self._draw_cell(i, j)
                return
            
            direction = random.randrange(directions)
            index = to_visit[direction]

            if index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            if index[1] == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False

            self._break_walls_r(index[0], index[1])

    def _reset_cells_visited(self):
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._cells[i][j].visited = False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        #checking left cell
        if i > 0 and self._cells[i-1][j].visited == False and self._cells[i][j].has_left_wall == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        #checking top cell
        if j > 0 and self._cells[i][j-1].visited == False and self._cells[i][j].has_top_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        #checking right cell
        if i < self._num_cols - 1 and self._cells[i+1][j].visited == False and self._cells[i][j].has_right_wall == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        #checking bottom cell
        if j < self._num_rows - 1 and self._cells[i][j+1].visited == False and self._cells[i][j].has_bottom_wall == False:   
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        
        return False

    def solve(self):
        return self._solve_r(0, 0)

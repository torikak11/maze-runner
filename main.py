from window import Window
from line import Line, Point

def main():
    win = Window(800, 600)
    p1 = Point(0, 0)
    p2 = Point(100, 100)
    line = Line(p1, p2)
    win.draw_line(line, "purple")
    win.wait_for_close()

main()
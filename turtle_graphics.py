# turtle_graphics.py
import itertools
from browser import document, window

canvas = document["my_canvas"]
ctx = canvas.getContext("2d")

class Turtle:
    def __init__(self):
        self.x = canvas.width // 2
        self.y = canvas.height // 2
        self.angle = 0
        self.color = 'black'
        self.speed = 1
        self.pensize = 1
        ctx.lineWidth = self.pensize
        self.color_cycle = itertools.cycle(['red', 'green', 'blue', 'yellow'])

    def forward(self, distance):
        new_x = self.x + distance * window.Math.cos(self.angle)
        new_y = self.y - distance * window.Math.sin(self.angle)
        ctx.beginPath()
        ctx.moveTo(self.x, self.y)
        ctx.lineTo(new_x, new_y)
        ctx.stroke()
        self.x = new_x
        self.y = new_y

    def right(self, angle):
        self.angle -= angle * (window.Math.PI / 180)

    def left(self, angle):
        self.angle += angle * (window.Math.PI / 180)

    def pencolor(self, color):
        self.color = color
        ctx.strokeStyle = self.color

    def cycle_pencolor(self):
        self.pencolor(next(self.color_cycle))

    def circle(self, radius):
        ctx.beginPath()
        ctx.arc(self.x, self.y, radius, 0, 2 * window.Math.PI)
        ctx.stroke()

    def bgcolor(self, color):
        canvas.style.backgroundColor = color

    def set_speed(self, speed):
        speed_map = {'slow': 200, 'normal': 100, 'fast': 50}
        self.speed = speed_map.get(speed, 100)

    def set_pensize(self, size):
        self.pensize = size
        ctx.lineWidth = self.pensize
    
    def clear(self):
        ctx.clearRect(0, 0, canvas.width, canvas.height)


turtle = Turtle()

def draw_circle(size, angle, shift, delay=300, max_size=700):
    if size > max_size:
        draw_circle(30, 0, 1, 300)
        turtle.clear()
        return
    turtle.cycle_pencolor()
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    window.setTimeout(lambda s=size, a=angle, sh=shift, d=delay: draw_circle(s + 5, a + 1, sh + 1, d), delay)

turtle.bgcolor('black')
turtle.set_speed('slow')
turtle.set_pensize(5)
draw_circle(30, 0, 1)


# def draw():
#     turtle = Turtle()
#     turtle.bgcolor('lightyellow')
#     turtle.set_pensize(5)
#     turtle.set_speed(10)

#     for _ in range(4):
#         turtle.cycle_pencolor()
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.circle(50)
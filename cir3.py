import arcade
from random import randint

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

circles = []
n = 10
 
def initialize():
    for i in range(n):
        circle = Circle(randint(100, SCREEN_WIDTH-100),
                        randint(100, SCREEN_HEIGHT-100),
                        randint(-5,5),
                        randint(-5,5))
        circles.append(circle)

class Circle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
 
    def move(self):
        self.x += self.vx
        self.y += self.vy
 
        # เพิ่มโค้ดส่วนจัดการการชนขอบจอที่นี่ด้วย
 
    def draw(self):
        arcade.draw_circle_outline(self.x, self.y,
                                   20, arcade.color.BLACK)

def on_draw(delta_time):
    arcade.start_render()
 
    for c in circles:
        c.move()
        c.draw()

def main():
    initialize()
 
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                       "Circles")
    arcade.set_background_color(arcade.color.WHITE)
 
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()

if __name__ == '__main__':
    main()
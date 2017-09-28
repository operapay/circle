import arcade
from random import randint

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

vxs = []
vys = []
xs = []
ys = []
n = 10
 
def initialize():
    for i in range(n):
        xs.append(randint(100, SCREEN_WIDTH-100))
        ys.append(randint(100, SCREEN_HEIGHT-100))
        vxs.append(randint(-5,5))
        vys.append(randint(-5,5))

def draw_and_move_circle(i):
    xs[i] += vxs[i]
    ys[i] += vys[i]
 
    arcade.draw_circle_outline(xs[i], ys[i], 20, arcade.color.BLACK)

def on_draw(delta_time):
    arcade.start_render()
 
    for i in range(n):
        draw_and_move_circle(i)

def main():
    initialize()
 
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                       "Circles")
    arcade.set_background_color(arcade.color.WHITE)
 
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()

if __name__ == '__main__':
    main()
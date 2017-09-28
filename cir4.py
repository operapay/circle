import arcade
import time
from random import randint
from pyglet.window import key

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def initialize():
    for i in range(n):
        circle = Circle(randint(100, SCREEN_WIDTH-100),
                        randint(100, SCREEN_HEIGHT-100),
                        randint(1,7),
                        randint(1,7),
                        randint(10,30))
        circles.append(circle)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y,
                                  10, arcade.color.BLUE)
    def control(self, keys):
        if keys[key.LEFT]:
            self.x -= 5
        if keys[key.RIGHT]:
            self.x += 5
        if keys[key.UP]:
            self.y += 5
        if keys[key.DOWN]:
            self.y -= 5
        
    def is_hit(self, circle):
            if ((circle.x-self.x)**2 + (circle.y-self.y)**2)**0.5 <= circle.r+10:              
                return True
            else:   
                return False 
                        
circles = []
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
n = 10
keys = key.KeyStateHandler()

class Circle:
    def __init__(self, x, y, vx, vy,r):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
 
    def move(self):
        self.x += self.vx
        self.y += self.vy
 
        if self.x < 0:
            self.vx *= -1
        if self.x > SCREEN_WIDTH:
            self.vx *= -1
        if self.y < 0:
            self.vy *= -1
        if self.y > SCREEN_HEIGHT:
            self.vy *= -1
 
    def draw(self):
        arcade.draw_circle_outline(self.x, self.y,
                                   self.r, arcade.color.BLACK)

def on_draw(delta_time):
    arcade.start_render()
 
    for c in circles:
        c.move()
        c.draw()
        if player.is_hit(c)==True:
            arcade.render_text(arcade.create_text('LOSE',arcade.color.RED,100),300,300)
            time.sleep(1)

    player.control(keys)
    player.draw()

def main():
    initialize()
 
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                       "Circles")
    arcade.set_background_color(arcade.color.WHITE)

    arcade.get_window().push_handlers(keys)
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()

if __name__ == '__main__':
    main()
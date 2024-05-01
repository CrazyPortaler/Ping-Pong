from pygame import *

class Sprite_entity():
    def __init__(self, x: int, y: int, scale: tuple, image_name: str):
        self.image = transform.scale(image.load(image_name), (scale[0], scale[1]))
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, scale[0], scale[1])

    def draw(self):
        mw.blit(self.image, (self.x, self.y))
    
    def move(self, vector_x: int, vector_y: int):
        self.x += vector_x
        self.y += vector_y
        self.rect.x = self.x
        self.rect.y = self.y

is_shooting = False

class Player(Sprite_entity):
    def control_tick(self):
        global player_speed
        vector_x = 0
        vector_y = 0
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.x < 600:
            vector_x += player_speed
        if keys[K_LEFT] and self.x > 0:
            vector_x -= player_speed
        self.move(vector_x, vector_y)
    def control_tick2(self):
        global player_speed
        vector_x = 0
        vector_y = 0
        keys = key.get_pressed()
        if keys[K_d] and self.x < 600:
            vector_x += player_speed
        if keys[K_a] and self.x > 0:
            vector_x -= player_speed
        self.move(vector_x, vector_y)


class Ball(Sprite_entity):
    def check_collide(self, rect_to_check):
        return self.rect.colliderect(rect_to_check)
        
    def tick(self):
        if self.check_collide(p1) or self.check_collide(p2):
            self.speed_y *= -1
        if self.x < 0 or self.x > 750:
            self.speed_x *= -1
        self.move(self.speed_x, self.speed_y)
        if self.y < 50:
            p2_scored()
            self.x, self.y = 500, 500
        if self.y > 650:
            p1_scored()
            self.x,self.y = 500, 500
    def check_collide(self, collide):
        return self.rect.colliderect(collide.rect)

def p2_scored():
    pass
def p1_scored():
    pass

p1 = Player(300, 575, (200, 100), 'platform.png')
p2 = Player(300, 25, (200, 100), 'platform2.png')

ball = Ball(500, 500, (50,50), 'Ball.png')
ball.speed_x, ball.speed_y = 2,2

mw = display.set_mode((800, 700))
mw.fill((0, 253, 255))
display.set_caption('Пинг-понг')

clock = time.Clock()
FPS = 50
game = True

player_speed = 4

while game:
    mw.fill((0, 253, 255))
    p1.draw()
    p2.draw()
    p1.control_tick()
    p2.control_tick2()
    ball.draw()
    ball.tick()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
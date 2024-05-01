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


class Enemy(Sprite_entity):
    def check_collide(self, rect_to_check):
        return self.rect.colliderect(rect_to_check)
        
    def tick(self):
        global kd
        if self.active:
            self.move(0, self.speed)
            if self.y > 500:
                self.get_out()

mw = display.set_mode((1000, 700))
mw.fill((0, 253, 255))
display.set_caption('Пинг-понг')

clock = time.Clock()
FPS = 50
game = True

while game:
    mw.fill((0, 253, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
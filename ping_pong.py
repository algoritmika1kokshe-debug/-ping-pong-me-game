#Создай собственный Шутер!
from pygame import *
from random import randint
from time import time as timer
window = display.set_mode((700,500),RESIZABLE)
display.set_caption('шутер')
background = (0,191,255)

game = True
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, playerImage, playerx, playery, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(playerImage), (size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = playerx
        self.rect.y = playery
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



x1 = 20
y1 = 430
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 355:
            self.rect.y += self.speed

lost = 0
killed = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80,620)
            self.rect.y = 0
            lost = lost +1


x1 =10 
y1 = 136

x2 =650
y2= 200
finish = False
player = Player('racket.png', x1, y1, 39,136, 7)
player2 = Player('racket.png', x2, y2, 39,136, 7)
while game != False:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(background)
                    

                    


    if finish != True:
        player.reset()
        player2.reset()
        player.update()
        player2.update_2()
        fps = 60 
        clock.tick(fps)
        display.update()

    else:
        finish = False

        
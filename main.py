from pygame import *
from random import randint
from time import time as timer


img_grass = 'grass.png'
img_zombi = 'zombi.png'
img_bullet = 'bullet.png'
img_tur = 'tur.png'
img_tur1 = 'tur1.png'

win_width = 700
win_height = 500
display.set_caption("Apocaliptoins")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_grass), (win_width, win_height))

game = True
finish = False

mixer.init()
fire_sound = mixer.Sound('fire.ogg')


font.init()
font2 = font.Font(None, 36)
font1 = font.SysFont(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
emoji_font = font.SysFont("Segoe UI Emoji", 40)

goal = 200
lvl2 = 20
lvl3 = 50
rel_time = False
num_fire = 0
life = 3





class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  # один рядок
                 size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(  # один рядок
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        pass

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

class Enemy(GameSprite):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        global lost
        # зникає, якщо дійде до краю екрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            # lost = lost + 1

tur = Player(img_tur, (win_width - 120)//2, win_height - 157, 120, 120, 0)
tur1 = Player(img_tur1, (win_width - 100)//2, win_height - 148, 100, 100, 0)
zombis = sprite.Group()
for i in range(5):
    zombi = Enemy(img_zombi, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    zombis.add(zombi)



bullets = sprite.Group()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))

        tur.update()
        tur.reset()

        tur1.update()
        tur1.reset()

        zombis.update()
        zombis.draw(window)

    display.update()
    time.delay(60)


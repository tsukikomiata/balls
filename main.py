import pygame as pg
import random


class Ball(pg.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all)
        self.radius = radius
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA, 16)
        pg.draw.circle(self.image, pg.Color(0, 255, 127), (radius, radius), radius)
        self.rect = pg.Rect(x, y, radius * 2, radius * 2)
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)

    def update(self):
            self.rect = self.rect.move(self.vx, self.vy)
            if pg.sprite.spritecollideany(self, y_bord):
                self.vy = -self.vy
            if pg.sprite.spritecollideany(self, x_bord):
                self.vx = -self.vx

            hits = pg.sprite.spritecollide(self, all, False, pg.sprite.collide_circle)
            hits.remove(self)
            for other in hits:
                if isinstance(other, Ball):
                    self.vx = -self.vx
                    self.vy = -self.vy
                    other.vx = -other.vx
                    other.vy = -other.vy


y_bord = pg.sprite.Group()
x_bord = pg.sprite.Group()


class Border(pg.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all)
        if x1 == x2:
            self.add(x_bord)
            self.image = pg.Surface([1, y2 - y1])
            self.rect = pg.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(y_bord)
            self.image = pg.Surface([x2 - x1, 1])
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)


size = width, height = 500, 500
screen = pg.display.set_mode(size)
all = pg.sprite.Group()
Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
radius = 20

for i in range(10):
    Ball(radius, 100, 100)
running = True
screen.fill((0, 0, 0))
while running:
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            Ball(radius, x, y)
    screen.fill((0, 0, 0))
    all.draw(screen)
    all.update()
    pg.display.flip()

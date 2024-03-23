import pygame as pg
from phylka import Pylka

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 400
        self.y = 260
        self.pulki = []

    def draw(self):
        pg.draw.circle(self.screen, (255, 0, 0), (self.x, self.y),   20)
        if len(self.pulki) > 0:
            for i in self.pulki:
                i.draw()

    def move(self, keys):
        if keys[pg.K_a]:
            self.x -= 10
        if keys[pg.K_d]:
            self.x += 10
        if keys[pg.K_SPACE]:
            self.pulki.append(Pylka(self.screen))


    def update(self):
        if len(self.pulki) > 0:
            for i in self.pulki:
                i.update()
        pg.display.update()


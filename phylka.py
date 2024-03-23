import pygame as pg

class Pylka:
    def __init__(self, screen):
        self.screen = screen
        self.x = 400
        self.y = 260


    def draw(self):
        pg.draw.circle(self.screen, (255, 255, 0), (self.player.move, self.player.move),   7.7)
        

    def update(self):
        self.y -= 10
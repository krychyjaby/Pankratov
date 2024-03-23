import pygame as pg
from player import Player
from phylka import Pylka


class Game:
    def __init__(self): 
        pg.init()
        self.screen = pg.display.set_mode((800, 450))
        self.clock = pg.time.Clock()
        self.pylka = Pylka(self.screen) 
        self.player = Player(self.screen) 

    def game(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            keys = pg.key.get_pressed()
            self.player.move(keys)
            self.draw() 
            self.update()
            self.clock.tick(30)

        pg.quit()

    def move(self, keys):
        if keys[pg.K_a]:
            self.x -= 10
        if keys[pg.K_d]:
            self.x += 10
        if keys[pg.K_SPACE]:
            self.pulki.append(Pylka())

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.player.draw()

    def update(self):
        pg.display.update()
        self.player.update()

game = Game()
game.game()
import pygame as pg



class Game:
    def __init__(self): 
        pg.init()
        self.screen = pg.display.set_mode((600, 600))
        self.back_surf = pg.image.load('sources/gachafon.jpg')
        self.clock = pg.type.Clock()

    def game(self):
        while True:
            self.draw()
            self.move()
            self.update()
            self.clock.tick(30)

    def draw(self):
        self.screen.blit(self.back_surf, (0, 0))

    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

    def update(self):
        pg.display.update()


game = Game()
game.game()
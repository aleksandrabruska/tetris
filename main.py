import pygame, sys
from figure import Figure_base, Figure1, Figure2, Figure3

class Tetris(object):
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1280,720))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        self.figures = [Figure1(self), Figure2(self), Figure3(self), Figure2(self),
                        Figure3(self), Figure1(self)]

        while True:
            x = 1
            for fig in self.figures:
                x+=1
                while(not fig.is_done()):
                    self.screen.fill((0,0,0))
                    for f in self.figures[0:x]:
                        self.draw(f)
                    pygame.display.flip()
                    self.tick(fig)
                    self.events(fig)
        

    def draw(self,fig):
        fig.draw()

    def tick(self, fig):
        fig.tick()

    def events(self, fig):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                fig.move_left()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                fig.move_right()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                fig.rotate_left()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                fig.rotate_right()

        
        
            
if __name__ == '__main__':
    Tetris()

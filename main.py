import pygame, sys
from figure import Figure_base, Figure1, Figure2, Figure3, Figure4, Figure5
from grid import Grid
import random

"""
    to do:
        -points displaying
        -can draw() and coord() methods me inherited?
        -przyspieszanie? - problem ze zmienianiem predkosci
        -error: moving figures into each other
        -comments?


    changes made:
        -figure shapes
        -end of game
        -fix error when you move the figure outside the screen
"""

class Tetris(object):
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((720,720))

        self.colors = [(200,0,0), (0,200,0), (0,0,200), (200,200,0),
                       (0,200,200), (200,0,200)]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        self.figures = [Figure1, Figure2, Figure3, Figure4, Figure5]

        self.gr = Grid(self)

        self.points = 0

      

        while True:
            fig = random.choice(self.figures)(self)

            while(not fig.is_done()):
                    
                self.screen.fill((0,0,0))
                    
                self.draw(fig)
                self.gr.draw()
                
                pygame.display.flip()
                
                self.tick(fig)
                self.events(fig)
            coord = fig.coord()
            for c in coord:
                self.gr.fill(c.x, c.y, fig.color)

            if self.gr.plus_point():
                self.gr.del_row(self.gr.plus_point() - 1)
                print(self.points)

            if self.gr.end_of_game():
                break


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

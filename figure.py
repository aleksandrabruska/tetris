import pygame
from pygame.math import Vector2

class Figure_base(object):
    """
        abstrakcyjna klasa bazowa?
        bo nie ma points
    """
    def __init__(self, game):
        self.color = (200,0,0)
        self.game = game
        self.size = self.game.screen.get_size()
        self.height = 20
        self.width = 20
        self.angle = 0


        self.vel = 0.25
        self.pos = Vector2(self.size[0]/2,0)


    def tick(self):
        self.pos = Vector2(self.pos.x, self.pos.y + self.vel)
        for point in self.points:
            if point.y == self.size[1] or point.y > self.size[1]:
                self.vel = 0
        
    def draw(self):
        #self.points = [Vector2(0,0), Vector2(20,0), Vector2(20,20), Vector2(0,20)]
        self.points = [p.rotate(self.angle) for p in self.points]
        self.points = [p + self.pos for p in self.points]
        pygame.draw.polygon(self.game.screen, self.color, self.points)

    def move_left(self):
        if self.vel != 0:
            self.pos = Vector2(self.pos.x - self.width, self.pos.y)
            
    def move_right(self):
        if self.vel != 0:
            self.pos = Vector2(self.pos.x + self.width, self.pos.y)

    def rotate_left(self):
        if self.vel != 0:
            self.angle += 90

    def rotate_right(self):
        if self.vel != 0:
            self.angle -= 90

    def is_done(self):
        return (True if self.vel == 0 else False)

    
        

class Figure1(Figure_base):
        
    
    def draw(self):
        
        self.points = [Vector2(0,0), Vector2(self.width * 3,0), Vector2(self.width * 3, self.height),
                  Vector2(self.width * 2,20), Vector2(self.width * 2, self.height * 2), Vector2(self.width,self.height * 2),
                  Vector2(self.width, self.height),Vector2(0,self.height)]

        Figure_base.draw(self)

class Figure2(Figure_base):
    def draw(self):
        self.points = [Vector2(0,0), Vector2(3*self.width,0),
                       Vector2(3* self.width, self.height), Vector2(0, self.height)]

        Figure_base.draw(self)

class Figure3(Figure_base):
    def draw(self):
        self.points = [Vector2(0,0), Vector2(2 * self.width,0),
                       Vector2(2 * self.width, 2 * self.height), Vector2(self.width, 2* self.height),
                       Vector2(self.width, self.height), Vector2(0, self.height)]

        Figure_base.draw(self)
    

 

   
    
       
        

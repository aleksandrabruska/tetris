import pygame, random
from pygame.math import Vector2

class Figure_base(object):
    """
        abstract base class
        (no points attribute)
    """

    def __init__(self, game):
        
        
        self.game = game
        self.color = random.choice(self.game.colors)
        self.size = self.game.screen.get_size()
        self.height = 40                #could be from Game object
        self.width = 40
        self.angle = 0


        self.vel = 0.25
        self.pos = Vector2(self.size[0]/2,0)



    def tick(self):
        self.pos = Vector2(self.pos.x, self.pos.y + self.vel)
    
        if self.pos.y % self.width == 0:

            """
                Checking for lower left corner
                (which has its coordinates
                like the block under)
                of each block of the figure
                if there is a filled block on the gird
                under this point (down ald right)
                
            """

            coord = [Vector2(c.x - self.width / 2, c.y + self.width / 2) for c in self.coord()]

            for point in coord:
                if point.y == self.size[1] or point.y > self.size[1]:
                    self.vel = 0
                if self.game.gr.check((point.x/self.width), (point.y/self.width)):
                    self.vel = 0 
        
    def draw(self):
        #self.points = [Vector2(0,0), Vector2(20,0), Vector2(20,20), Vector2(0,20)]
        self.points = [p.rotate(self.angle) for p in self.points]
        self.points = [p + self.pos for p in self.points]
        pygame.draw.polygon(self.game.screen, self.color, self.points)

    def move_left(self):

        f_width = min(vec.x for vec in self.points)
        """
        for vec in self.points:
            if vec.x == f_width:
                if self.game.gr.grid[int(vec.y//self.height)][int(f_width//self.width)] != 0:
                    return
        """
        
        if self.vel != 0 and f_width >= self.width:
                self.pos = Vector2(self.pos.x - self.width, self.pos.y)
            
    def move_right(self):
        f_width = max(vec.x for vec in self.points)
        if self.vel != 0 and f_width < self.game.screen.get_size()[0]:
            self.pos = Vector2(self.pos.x + self.width, self.pos.y)

        else:
            print(self.pos.x + f_width, self.game.screen.get_size()[0])

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
                  Vector2(self.width * 2,self.height), Vector2(self.width * 2, self.height * 2), Vector2(self.width,self.height * 2),
                  Vector2(self.width, self.height),Vector2(0,self.height)]

        Figure_base.draw(self)

    def coord(self):
        vecs = [Vector2(0,0), Vector2(self.width, 0), Vector2(self.width * 2, 0), Vector2(self.width, self.height)]
        vecs = [v + Vector2(self.width/2, self.width/2) for v in vecs]  #środki blocków
        vecs = [v.rotate(self.angle) for v in vecs]
        return [((v + self.pos)) for v in vecs]

    

class Figure2(Figure_base):

        
    def draw(self):
        self.points = [Vector2(0,0), Vector2(3*self.width,0),
                       Vector2(3* self.width, self.height), Vector2(0, self.height)]

        Figure_base.draw(self)

    def coord(self): 
        vecs = [Vector2(0,0), Vector2(self.width, 0), Vector2(self.width * 2, 0),]
        vecs = [v + Vector2(self.width/2, self.width/2) for v in vecs]  #środki blocków
        vecs = [v.rotate(self.angle) for v in vecs]
        return [((v + self.pos)) for v in vecs]
        

class Figure3(Figure_base):


        
    def draw(self):
        self.points = [Vector2(0,0), Vector2(2 * self.width,0),
                       Vector2(2 * self.width, 2 * self.height), Vector2(self.width, 2* self.height),
                       Vector2(self.width, self.height), Vector2(0, self.height)]

        Figure_base.draw(self)

    def coord(self): 
        vecs = [Vector2(0,0), Vector2(self.width, 0), Vector2(self.width, self.height)]
        vecs = [v + Vector2(self.width/2, self.width/2) for v in vecs]  #środki blocków
        vecs = [v.rotate(self.angle) for v in vecs]
        return [((v + self.pos)) for v in vecs]

class Figure4(Figure_base):

  
        
    def draw(self):
        self.points = [Vector2(0,0), Vector2(self.width * 2, 0), Vector2(self.width * 2, self.height * 2), Vector2(0, self.height * 2)]

        Figure_base.draw(self)


    def coord(self): 
        vecs = [Vector2(0,0), Vector2(self.width, 0), Vector2(0, self.height), Vector2(self.width, self.height)]
        vecs = [v + Vector2(self.width/2, self.width/2) for v in vecs]  #środki blocków
        vecs = [v.rotate(self.angle) for v in vecs]
        return [((v + self.pos)) for v in vecs]



class Figure5(Figure_base):

    def init(self):
        self.f_width = 3
        Figure_base.init(self)
        
    def draw(self):
        self.points = [Vector2(0,0), Vector2(self.width * 2, 0), Vector2(self.width * 2, self.height), Vector2(self.width * 3, self.height),
                       Vector2(self.width*3, self.height * 2), Vector2(self.width, self.height * 2), Vector2(self.width, self.height),
                       Vector2(0, self.height)]

        Figure_base.draw(self)


    def coord(self): 
        vecs = [Vector2(0,0), Vector2(self.width, 0), Vector2(self.width, self.height), Vector2(self.width * 2, self.height)]
        vecs = [v + Vector2(self.width/2, self.width/2) for v in vecs]  #środki blocków
        vecs = [v.rotate(self.angle) for v in vecs]
        return [((v + self.pos)) for v in vecs]

        
    

 

   
    
       
        

import pygame

class Grid(object):
    def __init__(self, game):
        self.width = 40         #could be from game object
        self.height = 40
        self.game = game
        self.w_num = self.game.screen.get_size()[0]//self.width
        self.h_num = self.game.screen.get_size()[1]//self.height
  
        self.grid = [[0 for i in range(self.w_num)] for i in range(self.h_num)]         #first coordinate is y


    def fill(self, x, y, color):
        x -= (self.width//2)
        y -= (self.width//2)
        x = int(x//self.width)
        y = int(y//self.width)
        self.grid[y][x] = self.game.colors.index(color) + 1


    def draw(self):
        for y in range(self.h_num):
            for x in range(self.w_num):
                if self.grid[y][x] != 0:
                    my_rect = pygame.Rect(self.width * x, self.height * y,self.width,self.height)
                    pygame.draw.rect(self.game.screen, self.game.colors[self.grid[y][x] - 1], my_rect)

    def check(self, x, y):                  #popraw, zeby bylo ladniejsze
    
        if y < 18:
            """
            coordinates of the square
            are connected with its
            upper left corner
            """

            if self.grid[int(y)][int(x)] != 0:
                
                return True
        else:
            return False

    def plus_point(self):
        for row in range(self.h_num):
            full = True
            for column in range(self.w_num):
                if self.grid[row][column] == 0:
                    full = False
            if full == True:
                return row + 1
        return 0

    def del_row(self, n):
        self.game.points += 10
        for column in range(self.w_num):
            self.grid[n][column] = 0
        for row in range(n,0, -1):
            for column in range(0,self.w_num):
                if self.grid[row - 1][column] != 0:
                    self.grid[row][column] = self.grid[row - 1][column]
                else:
                    self.grid[row][column] = 0
            
        
            

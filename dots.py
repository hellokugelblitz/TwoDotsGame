from ast import Pass
import pygame

class Dots:
    #Constructor
    def __init__(self, pos_x, pos_y, pos_2_x, pos_2_y, radius, color):
        self.id = id
        self.one_x = pos_x
        self.one_y = pos_y
        self.two_x = pos_2_x
        self.two_y = pos_2_y
        self.radius = radius
        self.color = color
        self.complete = False

    def drawDots(self, screen):
        #Draw our two dots
        pygame.draw.circle(screen, self.color,
                   [self.one_x, self.one_y], self.radius, 0)
        
        pygame.draw.circle(screen, self.color,
                   [self.two_x, self.two_y], self.radius, 0)


    def checkIfMouseOver(self, screen):
        dotName = ""
        pass

        return True

    def __str__(self):
        return self.id

import pygame

class Level:

    #Constructor
    def __init__(self, id):
        self.id = id

    def drawLevel(self, screen):
        pygame.draw.circle(screen, (0, 255, 0),
                   [300, 300], 170, 0)


    def __str__(self):
        return self.id

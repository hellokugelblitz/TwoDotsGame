import pygame
import level
import dots

LEVELS = []
level_one = level.Level(1)
LEVELS.append(level_one)


def main():
    #Responsible for handling the game loop.
    gameLoopActive = True

    #Background color for game
    background_color = (199, 199, 199)
    #Width and height of the game
    (width, height) = (600, 600)
    #Set the screen to width and height
    screen = pygame.display.set_mode((width, height))
    #Screen caption
    pygame.display.set_caption('Two Dots')

    while gameLoopActive:

        screen.fill(background_color)

        #For the future when I have levels to implement
        #level_one.drawLevel(screen)

        # pygame.draw.circle(screen, (121, 161, 224), [100, 475], 20, 0)

        # pygame.draw.circle(screen, (121, 161, 224), [100, 475], 20, 0)

        dots.Dots(100,475,457,100,20,(121, 161, 224)).drawDots(screen)

        #Handles events and quitting the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoopActive = False

        pygame.display.flip()

if __name__ == "__main__":
    main()

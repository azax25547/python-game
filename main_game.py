import pygame
from pygame.locals import *


def main():
    # initialisation of the screen
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    pygame.display.set_caption('Learning Pygame from Documentation')

    #filling Background
    background = pygame.Surface(screen.get_size())
    background = background.convert() #convert the Surface to a single pixel format. 
    background.fill((250,250,250))

    #Display Some Text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There",1,(10,10,10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    #Blit everything on screen
    screen.blit(background, (0,0))
    pygame.display.flip()

    # Event Loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        #screen.blit(background,(0,0))
        #pygame.display.flip()

if __name__ == "__main__":
    main()
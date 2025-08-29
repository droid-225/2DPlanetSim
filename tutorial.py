import pygame
import math
pygame.init() # initilaizes pygame

WIDTH, HEIGHT = 800, 800 # window size values
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # sets the window, or pygame surface, size
pygame.display.set_caption("Planet Simulator") # sets header for window

WHITE = (255, 255, 255)

def main(): 
    run = True
    clock = pygame.time.Clock() # keeps everything on a constant synchronized time regardless of actual individial system execution time; in game clock

    while run: # main game loop loop
        clock.tick(60) # limits the updates rate to upto 60 per second (or whatever the value is in the params per second)
        #WIN.fill(WHITE)
        #pygame.display.update() # updates the display

        for event in pygame.event.get(): # returns all events that occur in the pygame window (e.g. key press, mouse movement, etc.)
            if event.type == pygame.QUIT:
                run = False # stops game loop
    
    pygame.quit() # quits game

main()
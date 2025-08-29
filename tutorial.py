import pygame
import math
pygame.init() # initilaizes pygame

WIDTH, HEIGHT = 800, 800 # window size values
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # sets the window, or pygame surface, size
pygame.display.set_caption("Planet Simulator") # sets header for window

# Notes:
# (0, 0) is in the top left corner

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Planet:
    AU = 149.6e6 * 1000 # represents one astronomical unit in meters
    G = 6.67428e-11 # gravitational contant between planets
    SCALE = 250 / AU # 1 AU = about 100 px in pygame window
    TIMESTEP = 3600 * 24 # how much time has passed between each update frame; represents 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x # represents distance in meters away from sun in x plane
        self.y = y # represents distance in meters away from sun in y plane
        self.radius = radius
        self.color = color
        self.mass = mass # in kg

        self.orbit = [] # tracks points the planet has traveled along to draw orbit
        self.sun = False # if the planet is a sun
        self.dist_to_sun = 0 # distance to the sun

        self.x_vel = 0 # x velocity
        self.y_vel = 0 # y velocity

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        # here width / 2 and height / 2 makes the values are centered

        pygame.draw.circle(win, self.color, (x, y), self.radius);

def main(): 
    run = True
    clock = pygame.time.Clock() # keeps everything on a constant synchronized time regardless of actual individial system execution time; in game clock

    while run: # main game loop loop
        clock.tick(60) # limits the updates rate to upto 60 per second (or whatever the value is in the params per second)
        #WIN.fill(WHITE)
        #pygame.display.update() # updates the display

        sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
        sun.sun = True

        for event in pygame.event.get(): # returns all events that occur in the pygame window (e.g. key press, mouse movement, etc.)
            if event.type == pygame.QUIT:
                run = False # stops game loop
    
    pygame.quit() # quits game

main()
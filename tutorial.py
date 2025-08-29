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
BLUE = (100, 149, 237) # light blue
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

class Planet:
    AU = 149.6e6 * 1000 # represents one astronomical unit in meters
    G = 6.67428e-11 # gravitational contant between planets
    SCALE = 250 / AU # if numerator is 250, 1 AU = about 100 px in pygame window; to zoom out make the numerator less 
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

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]

    while run: # main game loop loop
        clock.tick(60) # limits the updates rate to upto 60 per second (or whatever the value is in the params per second)
        #WIN.fill(WHITE)

        for event in pygame.event.get(): # returns all events that occur in the pygame window (e.g. key press, mouse movement, etc.)
            if event.type == pygame.QUIT:
                run = False # stops game loop
    
        for planet in planets:
            planet.draw(WIN)

        pygame.display.update() # updates the display

    pygame.quit() # quits game

main()
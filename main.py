from email.mime import image
import pygame
import os
import time
import random

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")
#load images
RED_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
RED_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
RED_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))

#player ship
RED_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))

#lasers
RED_LASER = pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
RED_LASER = pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
RED_LASER = pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
RED_LASER = pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

# Background

BG = pygame.image.load(os.path.join("assets","background-black.png"))


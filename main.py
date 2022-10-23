from email.mime import image
import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")
#load images
RED_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
GREEN_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
YELLOW_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))

#player ship
BLUE_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))

#lasers
RED_LASER = pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

# Background

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")),(WIDTH,HEIGHT))

class Ship:
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self,window):
        window.blit(self.ship_img,(self.x,self.y))

class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img = BLUE_SPACESHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans",30)
    # player speed
    player_speed = 5
    player = Player(300,650)
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG,(0,0))
        #draw text
        lives_label = main_font.render(f"Health: {level}",1,(255,255,255))
        level_label = main_font.render(f"Level: {level}",1,(255,255,255))
        WIN.blit(lives_label,(10,10))
        WIN.blit(level_label,(WIDTH-level_label.get_width()-10,10))
        player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # move player
        keys= pygame.key.get_pressed()
        if keys[pygame.K_a]and player.x -player_speed > 0:  #left
            player.x -=player_speed
        
        if keys[pygame.K_d] and player.x + player_speed < WIDTH:  #right
            player.x +=player_speed
        
        if keys[pygame.K_w] and player.y - player_speed > 0:  #up
            player.y -=player_speed
        
        if keys[pygame.K_s] and player.y + player_speed < HEIGHT:  #down
            player.y +=player_speed
        

main()

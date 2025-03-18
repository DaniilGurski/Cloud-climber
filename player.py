
import pygame 
from settings import *

class Player(): 
    def __init__(self, x, y, jumpy_image, platform_group, screen):
        self.image = pygame.transform.smoothscale(jumpy_image, (45, 60))
        self.width = 25
        self.height = 55
        self.platform_group = platform_group
        self.screen = screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        # reset variables
        scroll = 0
        dx = 0 
        dy = 0 

        # process keypresses 
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10
            self.flip = True
        if key[pygame.K_d]:
            dx = 10
            self.flip = False

        # gravity
        self.vel_y += GRAVITY
        dy += self.vel_y


        # ensure player doesn't go off the edgde of the screen 
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right
        
        self.check_collision(dy)

        # check if the player has bounced to the top of the screen
        if self.rect.top <= SCROLL_THRESH: 
            
            # move everything down only if player jumps 
            if self.vel_y < 0:
                scroll = -dy

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll
    
    def check_collision(self, dy):
        for platform in self.platform_group:
            # collision in the y direction
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height): 
                # check if above the platform
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top # avoid clipping
                        dy = 0
                        self.vel_y = -20


    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))
import pygame
import random
from settings import *
from player import Player
from platform_obj import Platform
from utils import draw_bg, draw_panel, draw_text

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cloud Climber")

# set frame rate 
clock = pygame.time.Clock()
FPS = 60

# Assets
bg_image = pygame.image.load("assets/background.png").convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
jumpy_image = pygame.image.load("assets/jumpy.png").convert_alpha()
platform_image = pygame.image.load("assets/platform.png").convert_alpha()

# define font 
font_small = pygame.font.SysFont("Lucida Sans", 20)
font_big = pygame.font.SysFont("Lucida Sans", 24)

platform_group = pygame.sprite.Group()
jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150, jumpy_image, platform_group, screen)

# create starting platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, platform_image, 100, False)
platform_group.add(platform)


# Game loop
run = True
while run:
    clock.tick(FPS)
    if game_over == False and game_won == False:

        scroll = jumpy.move()

        # draw background 
        bg_scroll += scroll
        if bg_scroll >= 223:
            bg_scroll = 0
        draw_bg(screen, bg_image, scroll)

        # generate platforms
        if len(platform_group) < MAX_PLATFORMS:
            p_w = random.randint(40, 60)
            p_x = random.randint(0, SCREEN_WIDTH - p_w)
            p_y = platform.rect.y - random.randint(80, 120)
            p_type = random.randint(1, 2)

            if p_type == 1 and score > 500:
                p_moving = True
            else:
                p_moving = False
            platform = Platform(p_x, p_y, platform_image, p_w, p_moving)
            platform_group.add(platform)

        # update platforms
        platform_group.update(scroll)

        # update score
        if scroll > 0:
            score += scroll

        # draw sprites
        platform_group.draw(screen)
        jumpy.draw()

        draw_panel(screen, font_small, score)

        # check game over
        if jumpy.rect.top > SCREEN_HEIGHT: 
            game_over = True
        
        # check game won
        if score >= 1000:
            game_won = True
    
    elif game_won == True:
        if fade_counter < SCREEN_WIDTH:
            fade_counter += 5

            for y in range(0, 6, 2):
                pygame.draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
                pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1) * 100, SCREEN_WIDTH, 100))
        draw_text(screen, "You reached the end !", font_big, WHITE, 40, 300)
        draw_text(screen, f"SCORE: {score}", font_big, WHITE, 130, 250)
        draw_text(screen, f"PRESS SPACE TO PLAY AGAIN", font_big, WHITE, 40, 350)

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            # reset variables
            game_over = False
            game_won = False
            score = 0 
            scroll = 0
            fade_counter = 0
            # reposition jumpy 
            jumpy.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
            # reset platforms
            platform_group.empty()

            # create starting platforms
            platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, platform_image, 100, False)
            platform_group.add(platform)
    
    else:
        if fade_counter < SCREEN_WIDTH:
            fade_counter += 5

            for y in range(0, 6, 2):
                pygame.draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
                pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1) * 100, SCREEN_WIDTH, 100))

        draw_text(screen, "GAME OVER !", font_big, WHITE, 130, 200)
        draw_text(screen, f"SCORE: {score}", font_big, WHITE, 130, 250)
        draw_text(screen, f"PRESS SPACE TO PLAY AGAIN", font_big, WHITE, 40, 300)

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            # reset variables
            game_over = False
            game_won = False
            score = 0 
            scroll = 0
            fade_counter = 0
            # reposition jumpy 
            jumpy.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
            # reset platforms
            platform_group.empty()

            # create starting platforms
            platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, platform_image, 100, False)
            platform_group.add(platform)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update game screen
    pygame.display.update()


pygame.quit()


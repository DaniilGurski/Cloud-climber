import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cloud Climber")

# Assets
# TODO: Change background to a more quality image
bg_image = pygame.image.load("assets/background.png").convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Game loop
run = True
while run:
    # draw background 
    screen.blit(bg_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update game screen
    pygame.display.update()


pygame.quit()


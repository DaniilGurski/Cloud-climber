import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cloud Climber")

# set frame rate 
clock = pygame.time.Clock()
FPS = 60

# game variables
GRAVITY = 1
MAX_PLATFORMS = 10

# define colors 
WHITE = (255, 255, 255)

# Assets
# TODO: Change background to a more quality image
bg_image = pygame.image.load("assets/background.png").convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
jumpy_image = pygame.image.load("assets/jumpy.png").convert_alpha()
platform_image = pygame.image.load("assets/platform.png").convert_alpha()

# player class 
class Player(): 
    def __init__(self, x, y):
        self.image = pygame.transform.smoothscale(jumpy_image, (45, 60))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        # reset variables
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


        # check collision with platforms
        for platform in platform_group:
            # collision in the y direction
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height): 
                # check if above the platform
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top # avoid clipping
                        dy = 0
                        self.vel_y = -20

        # check collision with ground
        if self.rect.bottom + dy > SCREEN_HEIGHT: 
            dy = 0
            self.vel_y = -20

        # update rextangle position
        self.rect.x += dx
        self.rect.y += dy


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))
        pygame.draw.rect(screen, WHITE, self.rect, 2)

class Platform(pygame.sprite.Sprite): 
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.transform.smoothscale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    


jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
platform_group = pygame.sprite.Group()

# create temporary platforms
for p in range(MAX_PLATFORMS):
    p_w = random.randint(40, 60) # platform width
    p_x = random.randint(0, SCREEN_WIDTH - p_w) # do not let the platform go off the screen
    p_y = p * random.randint(80, 120)

    platform = Platform(p_x, p_y, p_w)
    platform_group.add(platform)

# Game loop
run = True
while run:

    clock.tick(FPS)

    jumpy.move()

    # draw background 
    screen.blit(bg_image, (0, 0))

    # draw sprites
    platform_group.draw(screen)
    jumpy.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update game screen
    pygame.display.update()


pygame.quit()

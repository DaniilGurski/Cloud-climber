import pygame
from settings import *

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_panel(screen, font_small, score):
    pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, 30))
    pygame.draw.line(screen, WHITE, (0, 30), (SCREEN_WIDTH, 30), 2)
    draw_text(screen, f"SCORE: {score}", font_small, WHITE, 0, 0)

def draw_bg(screen, bg_image, scroll):
    screen.blit(bg_image, (0, 0 + scroll))
    screen.blit(bg_image, (0, -223 + scroll))
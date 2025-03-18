import pygame
import os 
import sys
from settings import *

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_panel(screen, font_small, score):
    pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, 30))
    pygame.draw.line(screen, WHITE, (0, 30), (SCREEN_WIDTH, 30), 2)
    draw_text(screen, f"SCORE: {score}", font_small, WHITE, 0, 0)
    draw_text(screen, "Reach 5000m!", font_small, WHITE, SCREEN_WIDTH - 150, 5)

def draw_bg(screen, bg_image, scroll):
    screen.blit(bg_image, (0, 0 + scroll))
    screen.blit(bg_image, (0, -223 + scroll))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


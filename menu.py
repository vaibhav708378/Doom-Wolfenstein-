import pygame as pg
import sys
from main import *
from menu_settings import *

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Doom Menu")

button_font = pg.font.Font(None, 60)
title_font = pg.font.Font(None, 80)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 30, 30)
DARK_RED = (120, 0, 0)

bg_image = pg.image.load("resources/menu/background.jpg")
bg_image = pg.transform.scale(bg_image, (WIDTH, HEIGHT))

class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pg.Rect(x, y, width, height)
        self.callback = callback
        self.base_width = width
        self.base_height = height
        self.hover_scale = 1.2
        self.current_scale = 1.0

    def draw(self, surface):
        mouse_pos = pg.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse_pos)
        if is_hover:
            self.current_scale += (self.hover_scale - self.current_scale) * 0.2
            color = BLACK
        else:
            self.current_scale += (1.0 - self.current_scale) * 0.2
            color = DARK_RED
        new_width = int(self.base_width * self.current_scale)
        new_height = int(self.base_height * self.current_scale)
        new_rect = pg.Rect(
            self.rect.centerx - new_width // 2,
            self.rect.centery - new_height // 2,
            new_width,
            new_height,
        )
        pg.draw.rect(surface, color, new_rect, border_radius=15)
        pg.draw.rect(surface, WHITE, new_rect, 3, border_radius=15)
        text_surf = button_font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=new_rect.center)
        surface.blit(text_surf, text_rect)

    def check_click(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

def start_game():
    pg.quit()  
    game = Game()
    game.run()

def settings_menu():
    back_button = Button("⬅ Back", WIDTH//2 - 150, HEIGHT//2 + 150, 300, 80, lambda: menu_settings(screen, bg_image, WIDTH, HEIGHT, Button))
    clock = pg.time.Clock()
    running = True
    while running:
        screen.blit(bg_image, (0, 0))
        coming_text = title_font.render("COMING SOON", True, WHITE)
        shadow_text = title_font.render("COMING SOON", True, BLACK)
        screen.blit(shadow_text, (WIDTH//2 - shadow_text.get_width()//2 + 3, HEIGHT//3 + 3))
        screen.blit(coming_text, (WIDTH//2 - coming_text.get_width()//2, HEIGHT//3))
        back_button.draw(screen)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            back_button.check_click(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    running = False
        clock.tick(60)

def quit_game():
    pg.quit()
    sys.exit()

buttons = [
    Button("Start Game", WIDTH//2 - 150, HEIGHT//2 - 120, 300, 80, start_game),
    Button("Settings", WIDTH//2 - 150, HEIGHT//2, 300, 80, lambda: menu_settings(screen, bg_image, WIDTH, HEIGHT, Button)),
    Button("Quit", WIDTH//2 - 150, HEIGHT//2 + 120, 300, 80, quit_game)
]

def main_menu():
    clock = pg.time.Clock()
    while True:
        screen.blit(bg_image, (0, 0))
        for button in buttons:
            button.draw(screen)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
            for button in buttons:
                button.check_click(event)
        clock.tick(60)

if __name__ == "__main__":
    main_menu()

    

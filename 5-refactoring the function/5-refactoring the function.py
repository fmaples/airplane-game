import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    # initializing the game and creat a object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings,screen)
    # Make a bullet group
    bullets = Group()


    # star a loop for game
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
        gf.update_bullet(bullets)


run_game()
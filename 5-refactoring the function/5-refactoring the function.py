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
    # Make a count
    frame_count = 0

    # star a loop for game
    while True:
        frame_count += 1
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.fire_bullet(ai_settings,screen,ship,bullets,frame_count)
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
        gf.update_bullet(ai_settings,bullets)


run_game()
import pygame
import sys

def check_events(ship):
    """monitor keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # keydown
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: # down right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT: # down left
                ship.moving_left = True
        # keyup
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: #up right
                ship.moving_right = False
            elif event.key == pygame.K_LEFT: #up left
                ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    # redraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # display the screen
    pygame.display.flip()

import pygame
import sys
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypress"""
    if event.key == pygame.K_RIGHT:  # down right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # down left.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE: # down space.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:  # up right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # up left
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """monitor keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # keydown
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:    # keyup
            check_keyup_events(event,ship)



def update_screen(ai_settings,screen,ship,bullets):
    # redraw the screen
    screen.fill(ai_settings.bg_color)
    # redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullet(bullets):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullet that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)


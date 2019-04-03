import pygame
import sys
from bullet import Bullet

fire_on = False

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypress"""
    global fire_on
    if event.key == pygame.K_RIGHT:  # down right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # down left.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE: # down space.
        fire_on = True



def check_keyup_events(event, ship):
    """Respond to key releases"""
    global fire_on
    if event.key == pygame.K_RIGHT:  # up right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # up left
        ship.moving_left = False
    elif event.key == pygame.K_SPACE: # down space.
        fire_on = False


def check_events(ai_settings, screen, ship, bullets):
    """monitor keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # keydown
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:    # keyup
            check_keyup_events(event,ship)

def fire_bullet(ai_settings, screen, ship, bullets, frame_count):
    if fire_on and frame_count%10==0:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def update_screen(ai_settings,screen,ship,bullets):
    # redraw the screen
    screen.fill(ai_settings.bg_color)
    # redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullet(ai_settings,bullets):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullet that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)


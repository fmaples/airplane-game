import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship. """
    def __init__(self, ai_settings, screen, ship):
        """ Creates a bullet object at ship's current position """
        super(Bullet, self).__init__()
        self.screen = screen

        # Creat a bullet rect at (0,0),then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.bullets = [self.rect]
        if ai_settings.fire_level >1:
            for i in range(1,3):
                bullet_left = self.rect.copy()
                bullet_right = self.rect.copy()
                bullet_left.centerx -= 8*i
                bullet_right.centerx += 8*i
                self.bullets.append(bullet_left)
                self.bullets.append(bullet_right)
                print(i)


        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        #self.rect.y = self.y
        for i in range(len(self.bullets)):
            self.bullets[i].y = self.y


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        #pygame.draw.rect(self.screen, self.color, self.rect)
        for i in range(len(self.bullets)):
            pygame.draw.rect(self.screen, self.color, self.bullets[i])

        #pygame.draw.rect(self.screen,self.color,self.bullets[3])
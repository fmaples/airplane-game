import pygame
import settings

class Ship():
    def __init__(self,ai_settings,screen):
        """ initializing a ship and setting its initializetion position """
        self.screen = screen
        self.ai_settings = ai_settings
        # reading the picture of ship and its rectangle
        self.image = pygame.image.load('../images/ship.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # position of ship
        self.centerX = float(self.rect.centerx)
        # flag of moving
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerX += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.centerX -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerX

    def blitme(self):
        self.screen.blit(self.image,self.rect)
import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_settings

        # Load the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien near top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien exact position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

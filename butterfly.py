import pygame

class Butterfly():

    def __init__(self, screen):
        """Initialize the butterfly and set its starting position."""
        self.screen = screen
        
        # Load the butterfly image and get its rect
        self.image = pygame.image.load('images/alienButterfly.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new butterfly at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the butterfly at its current location"""
        self.screen.blit(self.image, self.rect)
            
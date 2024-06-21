import pygame

class Butterfly():

    def __init__(self, ai_settings, screen):
        """Initialize the butterfly and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the butterfly image and get its rect
        self.image = pygame.image.load('images/alienButterfly.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new butterfly at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        #self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the butterfly's center
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the butterfly's position based on the movement flag.""" 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.butterfly_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.butterfly_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.butterfly_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.butterfly_speed_factor    
                       

        # Update rect object from self.center
        self.rect.centerx = self.center  
        self.rect.centery = self.centery  

    def blitme(self):
        """Draw the butterfly at its current location"""
        self.screen.blit(self.image, self.rect)

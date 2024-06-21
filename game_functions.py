import sys

import pygame
from bullet import Bullet

def check_events(ai_settings, screen, butterfly, bullets):
    """Respond to keypresses and mouse events"""
    #Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.key)
            check_keydown_events(event, ai_settings, screen, butterfly, bullets)   

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, butterfly)

def check_keydown_events(event, ai_settings, screen, butterfly, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        # move butterfly to right
        butterfly.moving_right = True
    elif event.key == pygame.K_LEFT:
        butterfly.moving_left = True
    elif event.key == pygame.K_UP:
        butterfly.moving_up = True
    elif event.key == pygame.K_DOWN:
        butterfly.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(ai_settings, screen, butterfly)
        bullets.add(new_bullet)              

def check_keyup_events(event, butterfly):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        butterfly.moving_right = False 
    elif event.key == pygame.K_LEFT:
        butterfly.moving_left = False
    elif event.key == pygame.K_UP:
        butterfly.moving_up = False
    elif event.key == pygame.K_DOWN:
        butterfly.moving_down = False                 

def update_screen(ai_settings, screen, butterfly, bullets):
    """Update images on the screen and flip to the new screen"""

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    butterfly.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
import sys

import pygame

def check_events(butterfly):
    """Respond to keypresses and mouse events"""
    #Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.key)
            check_keydown_events(event, butterfly)   

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, butterfly)

def check_keydown_events(event, butterfly):
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

def update_screen(ai_settings, screen, butterfly):
    """Update images on the screen and flip to the new screen"""

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    butterfly.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
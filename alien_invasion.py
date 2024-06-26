import pygame
from pygame.sprite import Group

from settings import Settings
from butterfly import Butterfly
import game_functions as gf

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a butterfly
    butterfly = Butterfly(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, butterfly, bullets)
        butterfly.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, butterfly, bullets)
       
run_game()
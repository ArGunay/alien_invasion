import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings,  screen object.
    pygame.init()

    pygame.display.set_caption("Alien Invasion")

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings, screen)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)



run_game()
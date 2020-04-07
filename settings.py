
class Settings():
    """class to store all setting s from Alien Invasion"""

    def __init__(self):
        """initialize game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230 ,230)

        # ship settings
        self.ship_speed_factor = 21
        self.ship_limit = 3

        # Bullett settings
        self.bullet_speed_factor = 9
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 7
        self.fleet_drop_speed = 20
        # fleet_direction: 1 for right ; -1 for left
        self.fleet_direction = 1


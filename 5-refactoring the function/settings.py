class Settings():
    """ stores all the setting class about Alien Invasion """
    def __init__(self):
        """ initialization the setting of the game """

        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship setting
        self.ship_speed_factor = 1.2

        # Bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3


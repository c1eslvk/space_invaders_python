import pygame


class Laser:
    '''
    Used to create laser object.
    '''
    def __init__(self, config, engine, player, left_gun):
        '''
        Initializes laser object.

        Parameters
        ----------------
        config : Configuration()
        engine : GameEngine()
        player : Player()
        left_gun : bool
        '''
        self.engine = engine
        self.config = config
        self.player = player
        self.laser = pygame.image.load("laser.png")
        self.laser_box = self.laser.get_rect()
        self.laser_box.center = self.player.box.center
        shift_x = 34

        if left_gun:
            shift_x = -34

        self.laser_box.x += shift_x
        self.laser_box.y -= 28
        self.laser_speed = -4
        self.cooldown_counter = 0

    def move(self):
        '''
        Causes laser to move.
        '''
        self.laser_box = self.laser_box.move(0, self.laser_speed)

    def off_screen(self):
        '''
        Deletes laser from laser list if laser is not on the creen.
        '''
        off = False
        if self.laser_box.y + self.config.laser_y < 0:
            off = True
        return off

import pygame


class GameEngine:
    '''
    Is responsible for proper working of program.
    '''
    def __init__(self, config):
        '''
        Initializes game engine.

        Parameters
        ------------
        config : Configuration()
        '''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((config.window_width,
                                               config.window_height))
        self.arena = self.window.get_rect()
        self.back = pygame.image.load("background.png").convert()
        self.running = True
        self.screen = None

    def set_screen(self, screen):
        '''
        Sets screen to the one that should be shown.
        '''
        self.screen = screen

    def run(self):
        '''
        Main game loop.
        '''
        while self.running:
            self.wait_for_key()
            self.screen.refresh()

    def wait_for_key(self):
        '''
        Waits for key to be pressed.
        If ECS is pressed the game shuts down.
        If anything else is pressed it returns
        a list of keys that has been pressed
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.stop()
        else:
            self.screen.on_key(keys)

    def stop(self):
        '''
        Shuts down the game.
        '''
        pygame.quit()
        self.running = False
        exit()

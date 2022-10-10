import pygame
import game_screen


class MenuScreen:
    '''
    Used to create menu screen.
    '''
    def __init__(self, engine, config):
        '''
        Initializes menu screen.

        Parameters
        ----------------
        engine : GameEngine()
        config: Configuration()
        '''
        self.engine = engine
        self.config = config
        self.title_font = pygame.font.Font('pixel_font.ttf',
                                           self.config.title_size)
        self.text_font = pygame.font.Font('pixel_font.ttf',
                                          self.config.text_size)
        self.title = self.title_font.render("Space Invaders", True,
                                            self.config.white)
        self.start = self.text_font.render("Press SPACE to Start", True,
                                           self.config.white)
        self.quit = self.text_font.render("Press ESC to Quit", True,
                                          self.config.white)
        self.title_box = self.title.get_rect()
        self.start_box = self.start.get_rect()
        self.quit_box = self.quit.get_rect()
        self.title_box.midbottom = self.engine.arena.center
        self.start_box.midtop = self.engine.arena.center
        self.quit_box.midtop = self.start_box.midbottom
        self.pick_sound = pygame.mixer.Sound("pick.wav")

    def on_key(self, keys):
        '''
        Waits for key to be pressed.
        If SPACE is pressed it plays a sound
        and changes screen to game screen
        which starts the game
        '''
        if keys[pygame.K_SPACE]:
            self.pick_sound.play()
            self.engine.set_screen(game_screen.GameScreen(self.engine,
                                   self.config))

    def refresh(self):
        '''
        Refreshes screen in every loop.
        Shows text.
        '''
        window = self.engine.window
        window.blit(self.engine.back, (0, 0))
        window.blit(self.title, self.title_box)
        window.blit(self.start, self.start_box)
        window.blit(self.quit, self.quit_box)
        pygame.display.flip()
        self.engine.clock.tick(self.config.fps)

import pygame
import game_screen


class FailScreen:
    '''
    Used to create fail screen.
    '''
    def __init__(self, engine, config, score):
        '''
        Initializes fail screen.

        Parameters
        -----------
        engine : GameEngine()
        config : Configuration()
        score : (int)
        '''
        self.engine = engine
        self.config = config
        self.score = score
        self.fail_font = pygame.font.Font('pixel_font.ttf',
                                          self.config.title_size)
        self.text_font = pygame.font.Font('pixel_font.ttf',
                                          self.config.text_size)
        self.fail = self.fail_font.render("GAME OVER", True, self.config.white)
        self.final_score = self.text_font.render("Score: " + str(self.score),
                                                 True, self.config.white)
        self.restart = self.text_font.render("Press R to restart", True,
                                             self.config.white)
        self.quit = self.text_font.render("Press ESC to Quit", True,
                                          self.config.white)
        self.fail_box = self.fail.get_rect()
        self.final_score_box = self.final_score.get_rect()
        self.restart_box = self.restart.get_rect()
        self.quit_box = self.quit.get_rect()
        self.fail_box.midbottom = self.engine.arena.center
        self.final_score_box.midtop = self.engine.arena.center
        self.restart_box.midtop = self.final_score_box.midbottom
        self.quit_box.midtop = self.restart_box.midbottom
        self.pick_sound = pygame.mixer.Sound("pick.wav")

    def refresh(self):
        '''
        Refreshes screen in every loop.
        Shows text.
        '''
        window = self.engine.window
        window.blit(self.engine.back, (0, 0))
        window.blit(self.fail, self.fail_box)
        window.blit(self.final_score, self.final_score_box)
        window.blit(self.restart, self.restart_box)
        window.blit(self.quit, self.quit_box)
        pygame.display.flip()
        self.engine.clock.tick(self.config.fps)

    def on_key(self, keys):
        '''
        Waits for a key to be pressed.
        If R is pressed game starts again.
        If ESC is pressed game shuts down.
        '''
        if keys[pygame.K_r]:
            self.engine.set_screen(game_screen.GameScreen(self.engine,
                                   self.config))
            self.pick_sound.play()

        if keys[pygame.K_ESCAPE]:
            self.engine.stop()

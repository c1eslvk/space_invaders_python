import pygame
import laser
import player
import enemy
import fail_screen


class GameScreen:
    '''
    Used to create game screen.
    '''

    COOLDOWN = 50
    TIME = 0

    def __init__(self, engine, config):
        '''
        Initializes game screen.

        Parameters
        ----------------
        engine : GameEngine()
        config : Configuration()
        '''
        self.engine = engine
        self.config = config
        self.player = player.Player(config, engine, self)
        self.lasers = []
        self.enemies = []
        self.y = 0
        self.left_gun = True
        self.cooldown_counter = 0
        self.shot_counter = 0
        self.score = 0
        self.counter = 1
        self.score_font = pygame.font.Font('pixel_font.ttf',
                                           self.config.score_size)
        self.laser_sound = pygame.mixer.Sound("laser.wav")
        self.explosion_sound = pygame.mixer.Sound("explosion.wav")
        self.game_over_sound = pygame.mixer.Sound("game_over.wav")
        self.score_sound = pygame.mixer.Sound("score.wav")

        self.run = True

    def on_key(self, keys):
        '''
        Waits for keys.
        If left arrow is pressed it moves player to the left.
        If right arrow is pressed it moves player to the right.
        If space is pressed it shoots a laser.
        '''
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_SPACE]:
            if self.cooldown_counter == 0:
                self.laser_sound.play()
                self.lasers.append(laser.Laser(self.config, self.engine,
                                               self.player, self.left_gun))
                self.left_gun = not self.left_gun
                self.cooldown_counter = 1

    def cooldown(self):
        '''
        Determine the shooting cooldown.
        '''
        if self.cooldown_counter >= self.COOLDOWN:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

    def generate_enemy(self):
        '''
        Generates enemies in random order.
        Generates more enemies as score is rising.
        '''
        if self.score < 10 * self.counter:
            if self.TIME % int(200/self.counter) == 0:
                self.enemies.append(enemy.Enemy(self.config, self.engine, self))
        else:
            self.counter += 1
            self.score_sound.play()

    def refresh(self):
        '''
        Calls every refreshing function in game screen and print everything.
        '''
        self.TIME += 1
        self.refresh_background()
        self.player.refresh()
        self.refresh_lasers()
        self.refresh_enemies()
        self.print_score()
        pygame.display.flip()
        self.engine.clock.tick(self.config.fps)

    def refresh_background(self):
        '''
        Refreshes background in every loop and makes it move.
        '''
        window = self.engine.window
        back = self.engine.back
        rel_y = self.y % back.get_rect().height
        window.blit(back, (0, rel_y - back.get_rect().height))
        if rel_y < self.config.window_height:
            window.blit(back, (0, rel_y))
        self.y += 1.5

    def refresh_lasers(self):
        '''
        Refreshes lasers in every loop.
        '''
        self.cooldown()
        for shot in self.lasers:
            if shot.off_screen():
                self.lasers.remove(shot)
            self.engine.window.blit(shot.laser, (shot.laser_box.x,
                                    shot.laser_box.y))
            shot.move()

    def refresh_enemies(self):
        '''
        Refreshes enemies in every loop.
        '''
        self.generate_enemy()
        for ship in self.enemies:
            ship.refresh()
        self.kill_enemy()

    def kill_enemy(self):
        '''
        Detects if enemy has been killed by collision with laser.
        '''
        for shot in self.lasers:
            for ship in self.enemies:
                if shot.laser_box.colliderect(ship.box):
                    self.lasers.remove(shot)
                    ship.set_hit(True)
                    self.explosion_sound.play()
                    self.score += 1

    def print_score(self):
        '''
        Prints score.
        '''
        score_text = self.score_font.render("SCORE: " + str(self.score),
                                            True, self.config.white)
        score_text_box = (10, 10)
        self.engine.window.blit(score_text, score_text_box)

    def end_game(self):
        '''
        Plays sound and changes screen to fail screen after losing a game.
        '''
        self.engine.set_screen(fail_screen.FailScreen(self.engine,
                               self.config, self.score))
        self.game_over_sound.play()

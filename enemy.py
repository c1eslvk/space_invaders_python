import pygame
import random


class Enemy:
    '''
    Used to create enemy object.
    '''
    def __init__(self, config, engine, game_screen):
        '''
        Initializes enemy object.

        Parameters
        --------------
        config : Configuration()
        engine : GameEngine()
        game_screen : GameScreen()
        '''
        self.config = config
        self.engine = engine
        self.game_screen = game_screen
        self.speed = 2
        self.enemy = pygame.image.load("enemy_ship.png")
        self.box = self.enemy.get_rect()
        self.box.midbottom = self.engine.arena.midtop
        self.box.x = random.randint(0, self.config.window_width
                                    - self.config.enemy_x)
        self.sprites = []
        self.current_sprite = 0
        self.hit = False

        self.init_sprites()

    def init_sprites(self):
        '''
        Initializes list of images of explosion.
        '''
        self.sprites.append(pygame.image.load('explosion_0.png'))
        self.sprites.append(pygame.image.load('explosion_1.png'))
        self.sprites.append(pygame.image.load('explosion_2.png'))
        self.sprites.append(pygame.image.load('explosion_3.png'))
        self.sprites.append(pygame.image.load('explosion_4.png'))
        self.sprites.append(pygame.image.load('explosion_5.png'))
        self.sprites.append(pygame.image.load('explosion_6.png'))
        self.sprites.append(pygame.image.load('explosion_7.png'))
        self.sprites.append(pygame.image.load('explosion_8.png'))

    def move(self, enemy_speed):
        '''
        Moves enemy.
        '''
        self.box = self.box.move(0, enemy_speed)

    def hit_bottom(self):
        '''
        Detects collision between enemy and bottom of the screen.
        '''
        hit_bot = False
        if self.box.y + self.config.enemy_y > self.config.window_height:
            hit_bot = True
        return hit_bot

    def refresh(self):
        '''
        Refreshes enemies in every loop.
        Change image to explosion after collision.
        '''
        if self.hit_bottom():
            self.game_screen.end_game()
        image = self.enemy

        if self.hit is True:
            image = self.sprites[int(self.current_sprite/4)]
            self.current_sprite += 1

            if self.current_sprite >= 4*(len(self.sprites)):
                self.game_screen.enemies.remove(self)

        self.engine.window.blit(image, (self.box.x, self.box.y))

        if self.box.colliderect(self.game_screen.player.box):
            self.set_hit(True)
            self.game_screen.player.set_hit(True)
            self.game_screen.explosion_sound.play()
            self.game_screen.player.is_dead = True

        self.move(self.speed)

    def set_hit(self, hit):
        '''
        It sets hit to True and speed to 0 after collision with player or laser.
        '''
        self.hit = hit
        self.speed = 0

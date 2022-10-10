import pygame


class Player:
    '''
    Used to create player object.
    '''
    def __init__(self, config, engine, game_screen):
        '''
        Initializes player object.

        Parameters
        -----------
        config : Configuration()
        engine: GameEngine()
        game_screen: GameScreen()
        '''
        self.config = config
        self.engine = engine
        self.game_screen = game_screen
        self.ship = pygame.image.load("spaceship.png")
        self.box = self.ship.get_rect()
        self.box.midbottom = self.engine.arena.midbottom
        self.speed = 3
        self.is_dead = False
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

    def move_right(self):
        '''
        Is responsible for moving player to the right.
        '''
        self.speed = 3
        self.box = self.box.move(self.speed, 0)
        if self.box.x > (self.config.window_width - self.config.ship_x):
            self.box.x = (self.config.window_width - self.config.ship_x)

    def move_left(self):
        '''
        Is responsible for moving player to the left.
        '''
        self.speed = -3
        self.box = self.box.move(self.speed, 0)
        if self.box.x < 0:
            self.box.x = 0

    def refresh(self):
        '''
        It refreshes player in every loop.
        Change image to explosion after collision.
        '''
        image = self.ship

        if self.hit is True:
            image = self.sprites[int(self.current_sprite/4)]
            self.current_sprite += 1

        if self.current_sprite >= 4*(len(self.sprites)):
            self.game_screen.end_game()

        self.engine.window.blit(image, (self.box.x, self.box.y - 15))

    def set_hit(self, hit):
        '''
        It sets hit to True and speed to 0 after collision with enemy.
        '''
        self.hit = hit
        self.speed = 0

    def hit_enemy(self, enemy_box):
        '''
        It detects collision between enemy and player.
        '''
        if self.box.colliderect(enemy_box):
            self.is_dead = True

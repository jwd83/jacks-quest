import pygame
from scene import Scene


class Level(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.camera = (-400, -400)

        # create sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # load town1.png
        self.img_background = self.game.load_asset("town3.png")

    def update(self):
        if self.game.pressed[pygame.K_LEFT]:
            self.camera = (self.camera[0] + 1, self.camera[1])
        if self.game.pressed[pygame.K_RIGHT]:
            self.camera = (self.camera[0] - 1, self.camera[1])
        if self.game.pressed[pygame.K_UP]:
            self.camera = (self.camera[0], self.camera[1] + 1)
        if self.game.pressed[pygame.K_DOWN]:
            self.camera = (self.camera[0], self.camera[1] - 1)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.img_background, self.camera)

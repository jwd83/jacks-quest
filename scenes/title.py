import pygame
from scene import Scene


class Title(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.title_image = self.game.load_asset("dragon-title-180p.png")
        # draw a black fade in over the title
        self.fade = pygame.Surface((320, 180))
        self.fade.fill((0, 0, 0))
        self.fade_delay = 0.5
        self.fade_speed = 100

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_image, (0, 0))

        if self.elapsed() > self.fade_delay:
            self.fade.set_alpha(
                255 - min((self.elapsed() - self.fade_delay) * self.fade_speed, 255)
            )
        self.screen.blit(self.fade, (0, 0))

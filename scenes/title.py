import pygame
from scene import Scene


class Title(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.title_image = self.game.load_asset("dragon-title-180p.png")

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_image, (0, 0))

        # draw a black fade in over the title
        fade = pygame.Surface((320, 180))
        fade.fill((0, 0, 0))
        fade.set_alpha(255 - min(self.elapsed() * 100, 255))
        self.screen.blit(fade, (0, 0))

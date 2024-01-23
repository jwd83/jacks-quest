import pygame
from scene import Scene


class Logo(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.title_image = self.game.load_asset("dragon-title-180p.png")
        # draw a black fade in over the title
        self.fade = pygame.Surface((320, 180))
        self.fade.fill((0, 0, 0))
        self.fade_delay = 0.5
        self.fade_speed = 250
        self.timeout = 3.5

    def update(self):
        if self.elapsed() > self.timeout:
            self.game.scene_replace = "Title"

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_image, (0, 0))

        # fade in
        if self.elapsed() > self.fade_delay:
            self.fade.set_alpha(
                255 - min((self.elapsed() - self.fade_delay) * self.fade_speed, 255)
            )

        # fade out
        if self.elapsed() > self.timeout - 255 / self.fade_speed:
            self.fade.set_alpha(
                self.constrain(
                    255
                    - (self.timeout - self.elapsed()) / (255 / self.fade_speed) * 255,
                    0,
                    255,
                )
            )
        self.screen.blit(self.fade, (0, 0))

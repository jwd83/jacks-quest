import pygame
import math
from scene import Scene


class Title(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.title_image = self.game.load_asset("jacks-quest-title-screen.png")
        # draw a black fade in over the title
        self.fade = pygame.Surface((320, 180))
        self.fade.fill((0, 0, 0))
        self.fade_delay = 0
        self.fade_speed = 400

        self.text_press_start = self.game.make_text(
            text="Press Start",
            color="WHITE",
            fontSize=64,
        )

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_image, (0, 0))
        self.text_press_start.set_alpha(180 + math.sin(self.elapsed() * 2) * 60)
        self.game.place_text_centered(self.text_press_start, self.screen, (1, 1.5))

        # wait to start the fade in from pure black
        if self.elapsed() > self.fade_delay:
            self.fade.set_alpha(
                255 - min((self.elapsed() - self.fade_delay) * self.fade_speed, 255)
            )
        self.screen.blit(self.fade, (0, 0))

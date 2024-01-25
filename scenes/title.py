import pygame
import math
from scene import Scene


class Title(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.img_title = self.game.load_asset("jacks-quest-title-screen.png")
        # draw a black fade in over the title
        self.fade = pygame.Surface((320, 180))
        self.fade.fill((0, 0, 0))
        self.fade_delay = 0
        self.fade_speed = 400

        self.text_press_start = self.game.make_text(
            text="Press Enter",
            color="WHITE",
            fontSize=24,
        )

    def update(self):
        if pygame.K_RETURN in self.game.just_pressed:
            self.game.scene_push = "MainMenu"

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.img_title, (0, 0))

        # fade the press start text in and out
        self.text_press_start.set_alpha(
            self.constrain(127 + math.sin(self.elapsed() * 2) * 128, 0, 255)
        )
        self.game.blit_centered(self.text_press_start, self.screen, (0.5, 0.75))

        # wait to start the fade in from pure black
        if self.elapsed() > self.fade_delay:
            self.fade.set_alpha(
                255 - min((self.elapsed() - self.fade_delay) * self.fade_speed, 255)
            )
        self.screen.blit(self.fade, (0, 0))

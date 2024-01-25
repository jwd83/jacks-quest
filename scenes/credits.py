import pygame
from scene import Scene


class Credits(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.text_top = 200
        self.credits = [
            "Jack's Quest",
            "",
            "Copyright 2024 Binary Dragon Studios",
            "",
            "Art",
            "",
            "Jack Fisher",
            "Jared De Blander",
            "",
            "Programming",
            "",
            "Jared De Blander",
            "",
            "Special Thanks To",
            "",
            "Adobe Photoshop",
            "Aseprite",
            "Audacity",
            "jsfxr",
            "Pygame",
            "Stable Diffusion",
        ]

        self.text_credits = []

        # render all the credits text
        for i, line in enumerate(self.credits):
            self.text_credits.append(self.game.make_text(line, "WHITE", 8))

    def update(self):
        pass

    def draw(self):
        self.game.screen.fill((0, 0, 0))

        # draw the credits text to the screen, scroll them up based on elapsed time
        self.text_top -= 1
        for i, text in enumerate(self.text_credits):
            self.game.screen.blit(
                text, (160 - text.get_width() / 2, self.text_top + i * 16)
            )

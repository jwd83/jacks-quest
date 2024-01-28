import pygame
from scene import Scene


class Credits(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.text_top = 400
        self.credits = [
            "Jack's Quest",
            "",
            "Copyright 2004 Jack Games",
            "",
            "Jack's Quest Remaster",
            "Copyright 2024",
            "",
            "Binary Dragon Studios",
            "",
            "Story, Art & Programming",
            "",
            "Jack Fisher",
            "Jared De Blander",
            "",
            "Special Thanks To",
            "",
            "Adobe Photoshop",
            "Amuse & Stable Diffusion",
            "Aseprite",
            "Audacity",
            "codeman38 (font)",
            "jsfxr (sound effects)",
            "Pygame & Pygame-ce",
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
                text, (160 - text.get_width() / 2, round(self.text_top / 2) + i * 16)
            )

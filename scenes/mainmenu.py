import pygame
from scene import Scene


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        if pygame.K_RETURN in self.game.just_pressed:
            self.game.scene_pop = True

    def draw(self):
        # draw a blue box with a white border
        pygame.draw.rect(self.game.screen, (0, 0, 255), (50, 50, 320 - 50, 180 - 50), 0)
        pygame.draw.rect(
            self.game.screen, (255, 255, 255), (50, 50, 320 - 50, 180 - 50), 2
        )

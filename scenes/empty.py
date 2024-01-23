import pygame
from scene import Scene


class Empty(Scene):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        pass

    def draw(self):
        pass

import pygame
from scene import Scene


class Options(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.box_delay = 0.18
        self.delay_complete = False
        self.text_options = self.game.make_text("Options", "WHITE", 24)
        self.text_new_game = self.game.make_text("New Game", "WHITE", 8)
        self.text_continue = self.game.make_text("Continue", "GREY", 8)
        self.text_options = self.game.make_text("Options", "WHITE", 8)
        self.img_cursor = self.game.load_asset("cursor-4x7.png")
        self.selected_row = 0
        self.rows = 3
        self.rows_y = [100, 116, 132]

    def update(self):
        pass

    def draw(self):
        self.draw_box_centered((160, 80), (120, 90))

        if self.elapsed() < self.box_delay:
            return

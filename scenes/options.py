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
        self.img_hand = self.game.load_asset("cursor-4x7.png")
        self.selected_row = 0
        self.rows = 3
        self.rows_y = [100, 116, 132]

    def update(self):
        pass

    def draw(self):
        self.draw_box_centered((160, 50), (90, 40))

        if self.elapsed() < self.box_delay:
            return

    def draw_box(self, position: tuple, size: tuple):
        if self.elapsed() < self.box_delay:
            # expand the box from it's center to it's full size
            position = (
                position[0] + size[0] / 2 * (1 - self.elapsed() / self.box_delay),
                position[1] + size[1] / 2 * (1 - self.elapsed() / self.box_delay),
            )

            size = (
                size[0] * self.elapsed() / self.box_delay,
                size[1] * self.elapsed() / self.box_delay,
            )

            # draw the blue background
            pygame.draw.rect(
                self.game.screen,
                (0, 0, 255),
                (position[0], position[1], size[0], size[1]),
                width=0,
            )

            # draw the white border
            pygame.draw.rect(
                self.game.screen,
                (255, 255, 255),
                (position[0], position[1], size[0], size[1]),
                width=2,
            )
            return

        # draw the blue background
        pygame.draw.rect(
            self.game.screen,
            (0, 0, 255),
            (position[0], position[1], size[0], size[1]),
            width=0,
        )

        # draw the white border
        pygame.draw.rect(
            self.game.screen,
            (255, 255, 255),
            (position[0], position[1], size[0], size[1]),
            width=2,
        )

    def draw_box_centered(self, position: tuple, size: tuple):
        if self.elapsed() < self.box_delay:
            # expand the box from it's center to it's full size

            size = (
                size[0] * self.elapsed() / self.box_delay,
                size[1] * self.elapsed() / self.box_delay,
            )

            # draw the blue background
            pygame.draw.rect(
                self.game.screen,
                (0, 0, 255),
                (
                    position[0] - size[0] / 2,
                    position[1] - size[1] / 2,
                    size[0],
                    size[1],
                ),
                width=0,
            )

            # draw the white border
            pygame.draw.rect(
                self.game.screen,
                (255, 255, 255),
                (
                    position[0] - size[0] / 2,
                    position[1] - size[1] / 2,
                    size[0],
                    size[1],
                ),
                width=2,
            )

            return

        # draw the blue background
        pygame.draw.rect(
            self.game.screen,
            (0, 0, 255),
            (position[0] - size[0] / 2, position[1] - size[1] / 2, size[0], size[1]),
            width=0,
        )

        # draw the white border
        pygame.draw.rect(
            self.game.screen,
            (255, 255, 255),
            (position[0] - size[0] / 2, position[1] - size[1] / 2, size[0], size[1]),
            width=2,
        )

import pygame
from scene import Scene


class Options(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.box_delay = 0.18
        self.delay_complete = False
        self.text_title = self.game.make_text("Options", "WHITE", 16)
        self.text_sound = self.game.make_text("Sound", "WHITE", 8)

        self.img_cursor = self.game.load_asset("cursor-4x7.png")
        self.selected_row = 0
        self.rows = 3
        self.rows_y = [60, 76, 92]

    def update(self):
        if self.delay_complete:
            if pygame.K_RETURN in self.game.just_pressed:
                print("selected row: ", self.selected_row)
                # self.game.scene_pop = True
                if self.selected_row == 2:
                    self.game.scene_push = "MainMenu"

            if pygame.K_UP in self.game.just_pressed:
                self.selected_row -= 1
                self.game.play_sound("click.wav")

            if pygame.K_DOWN in self.game.just_pressed:
                self.selected_row += 1
                self.game.play_sound("click.wav")

            self.selected_row %= self.rows

        else:
            if self.elapsed() > self.box_delay:
                self.game.play_sound("click.wav")
                self.delay_complete = True

    def draw(self):
        self.draw_box_centered((160, 80), (120, 90))

        if self.elapsed() < self.box_delay:
            return

        self.game.screen.blit(self.text_title, (100, 40))

        if self.active:
            self.game.screen.blit(
                self.img_cursor, (108, self.rows_y[self.selected_row])
            )

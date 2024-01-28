import pygame
from scene import Scene


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.box_delay = 0.18
        self.delay_complete = False
        self.text_new_game = self.game.make_text("New Game", "WHITE", 8)
        self.text_continue = self.game.make_text("Continue", "GREY", 8)
        self.text_options = self.game.make_text("Options", "WHITE", 8)
        self.img_cursor = self.game.load_asset("cursor-4x7.png")
        self.selected_row = 0
        self.rows = 3
        self.rows_y = [100, 116, 132]

    def update(self):
        if self.delay_complete:
            if pygame.K_RETURN in self.game.just_pressed:
                print("selected row: ", self.selected_row)
                # self.game.scene_pop = True
                if self.selected_row == 0:
                    self.game.scene_replace = "Level"
                if self.selected_row == 2:
                    self.game.scene_push = "Options"

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
        self.draw_box_centered((160, 120), (90, 60))

        if not self.delay_complete:
            return

        self.game.screen.blit(self.text_new_game, (135, self.rows_y[0]))
        self.game.screen.blit(self.text_continue, (135, self.rows_y[1]))
        self.game.screen.blit(self.text_options, (135, self.rows_y[2]))

        # only draw the cursor if we are the active scene
        if self.active:
            self.game.screen.blit(
                self.img_cursor, (125, self.rows_y[self.selected_row])
            )

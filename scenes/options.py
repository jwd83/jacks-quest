import pygame
from scene import Scene


class Options(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.box_delay = 0.18
        self.delay_complete = False
        self.text_title = self.game.make_text("Options", "WHITE", 16)
        self.text_music = self.game.make_text("Music", "WHITE", 8)
        self.text_effects = self.game.make_text("Effects", "WHITE", 8)
        self.text_credits = self.game.make_text("Credits", "WHITE", 8)

        self.img_cursor = self.game.load_asset("cursor-4x7.png")
        self.selected_row = 0
        self.rows = 3
        self.rows_y = [62, 78, 94]

    def update(self):
        if self.delay_complete:
            if pygame.K_RETURN in self.game.just_pressed:
                print("selected row: ", self.selected_row)
                if self.selected_row == 2:
                    self.game.scene_push = "Credits"

            if pygame.K_UP in self.game.just_pressed:
                self.selected_row -= 1
                self.game.play_sound("click.wav")

            if pygame.K_DOWN in self.game.just_pressed:
                self.selected_row += 1
                self.game.play_sound("click.wav")

            if pygame.K_LEFT in self.game.just_pressed:
                if self.selected_row == 0:
                    self.game.volume_music = max(0, self.game.volume_music - 10)
                elif self.selected_row == 1:
                    self.game.volume_effects = max(0, self.game.volume_effects - 10)
                self.game.play_sound("click.wav")

            if pygame.K_RIGHT in self.game.just_pressed:
                if self.selected_row == 0:
                    self.game.volume_music = min(100, self.game.volume_music + 10)
                elif self.selected_row == 1:
                    self.game.volume_effects = min(100, self.game.volume_effects + 10)
                self.game.play_sound("click.wav")

            self.selected_row %= self.rows

        else:
            if self.elapsed() > self.box_delay:
                self.game.play_sound("click.wav")
                self.delay_complete = True

    def draw(self):
        self.draw_box_centered((160, 80), (120, 94))

        if self.elapsed() < self.box_delay:
            return

        self.game.blit_centered(self.text_title, self.screen, (0.5, 0.27))

        self.game.screen.blit(self.text_music, (116, self.rows_y[0]))
        self.game.screen.blit(self.text_effects, (116, self.rows_y[1]))
        self.game.screen.blit(self.text_credits, (116, self.rows_y[2]))

        music_level = self.game.make_text(str(self.game.volume_music), "WHITE", 8)
        effects_level = self.game.make_text(str(self.game.volume_effects), "WHITE", 8)

        self.game.screen.blit(music_level, (185, self.rows_y[0]))
        self.game.screen.blit(effects_level, (185, self.rows_y[1]))

        if self.active:
            self.game.screen.blit(
                self.img_cursor, (108, self.rows_y[self.selected_row])
            )

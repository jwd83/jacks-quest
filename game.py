import pygame
from scene import Scene
from scenes.title import Title


class Game:
    def __init__(self):
        # set the quit flag
        self.quit = False

        pygame.init()

        # create a window
        self.screen = pygame.display.set_mode((320, 180))
        pygame.display.set_caption("Jack's Quest")
        self.clock = pygame.time.Clock()

        # create a stack for scenes to be updated and drawn
        self.scene = []

        # add the title scene to the stack
        self.scene.append(Title(self))

    def run(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit = True

            # process update for the top scene in the stack
            self.scene[-1].update()

            # draw all scenes in the stack from bottom to top
            for scene in self.scene:
                scene.draw()

            # update the display
            pygame.display.flip()

            # limit the game to 60 fps
            self.clock.tick(60)

    def load_asset(self, asset_path: str):
        return pygame.image.load("assets/" + asset_path).convert_alpha()

import os
import pygame
from scene import Scene
from scenes.empty import Empty
from scenes.title import Title


class Game:
    def __init__(self):
        # set the quit flag to false at the start
        self.quit = False
        self.pressed = []
        self.just_pressed = []

        # initialize pygame
        pygame.init()

        # create a window
        self.screen = pygame.display.set_mode((320, 180))
        pygame.display.set_caption("Jack's Quest")

        # create a pygame clock to limit the game to 60 fps
        self.clock = pygame.time.Clock()

        # create a stack for scenes to be updated and drawn
        # and add the title scene to the stack
        self.scene = []  # type: list[Scene]
        self.scene_list = ["Title"]
        self.scene.append(Title(self))

        # create variables to handle scene changes
        self.scene_replace = None
        self.scene_push = None
        self.scene_pop = None

    def run(self):
        while not self.quit:
            # handle events and input
            self.get_events_and_input()

            # process update for the top scene in the stack
            self.scene[-1].update()

            # draw all scenes in the stack from bottom to top
            for scene in self.scene:
                scene.draw()

            # update the display
            pygame.display.flip()

            # process scene change requests (if any)
            self.change_scenes()

            # limit the game to 60 fps
            self.clock.tick(60)

    def get_events_and_input(self):
        # get input
        self.pressed = pygame.key.get_pressed()
        self.just_pressed = []

        # get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                self.just_pressed.append(event.key)

    def load_asset(self, asset_path: str):
        return pygame.image.load("assets/" + asset_path).convert_alpha()

    def change_scenes(self):
        # check for scene changes
        if self.scene_replace is not None:
            if self.scene_replace in self.scene_list:
                self.scene = []
                self.scene.append(self.load_scene(self.scene_replace))
            self.scene_replace = None

        elif self.scene_push is not None:
            if self.scene_push in self.scene_list:
                self.scene.append(self.load_scene(self.scene_push))
            self.scene_push = None

        elif self.scene_pop is not None:
            if len(self.scene) > 1:
                self.scene.pop()
            else:
                print("WARNING: Cannot pop last scene! Exiting!")
                self.quit = True
            self.scene_pop = None

    def load_scene(self, scene: str):
        if scene in self.scene_list:
            # use an eval to return the scene based on the scene string
            return eval(scene + "(self)")
        else:
            return Title(self)

    # from the pygame tutorial:
    # https://www.pygame.org/docs/tut/tom_games3.html
    def load_png(self, name):
        """Load image and return image object"""
        fullname = os.path.join("data", name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except FileNotFoundError:
            print(f"Cannot load image: {fullname}")
            raise SystemExit
        return image, image.get_rect()

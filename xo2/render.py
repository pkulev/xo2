"""EAF Renderer implementation for pygame graphics backend."""

import eaf
import pygame
from eaf.core import Vec3


pygame.display.init()


class Renderable(eaf.Renderable):
    """Pygame Renderable implementation."""


class SpriteRenderer(eaf.Renderer):
    """Pygame Renderer implementation for sprite graphics."""

    def __init__(self, window, fill_color=pygame.Color(0, 0, 0, 255)):
        super().__init__(window)

        self._fill_color = fill_color

    @property
    def fill_color(self):
        return self._fill_color

    @fill_color.setter
    def fill_color(self, values):
        self._fill_color = pygame.Color(*values)

    def clear(self):
        self.screen.fill(self.fill_color)

    def render_objects(self, objects):
        for obj in objects:
            self.screen.blit(obj.image, obj.pos.as_tuple2())

    def present(self):
        pygame.display.flip()

    def get_width(self):
        return self.screen.get_width()

    def get_height(self):
        return self.screen.get_height()

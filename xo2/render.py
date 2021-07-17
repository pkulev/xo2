"""EAF Renderer implementation for pygame graphics backend."""

import logging

import eaf
import pygame
from eaf.core import Vec3


LOG = logging.getLogger()

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


class ObjectRenderer3D(eaf.Renderer):
    """Pygame Renderer implementation for 3D graphics."""

    def __init__(self, window, fill_color=pygame.Color(0, 0, 0, 255)):
        super().__init__(window)

        self._fill_color = fill_color

        self._wireframe = False

    @property
    def wireframe(self):
        return self._wireframe

    def toggle_wireframe(self, state=None):
        if state is None:
            state = not self._wireframe

        self._wireframe = state

    @property
    def fill_color(self):
        return self._fill_color

    @fill_color.setter
    def fill_color(self, values):
        self._fill_color = pygame.Color(*values)

    def putpixel(self, xy, color):
        self.screen.set_at(xy, color)

    def line(self, x1, y1, x2, y2, color):
        print("Line({0}, {1}, {2}, {3})".format(x1, y1, x2, y2), end="\n\n")
        steep = False
        if abs(x1 - x2) < abs(y1 - y2):  # transpose
            x1, y1 = y1, x1
            x2, y2 = y2, x2
            steep = True
            print("steep = false")

        if x1 > x2:
            x1, x2 = x2, x1  # left-to-right
            y1, y2 = y2, y1
            print("transposed", end="\n\n")

        dx = x2 - x1
        dy = y2 - y1

        for x in range(x1, x2 + 1):
            t = float(x - x1) / float(dx)
            y = round(y1 * (1.0 - t) + y2 * t)
            self.putpixel((y, x) if steep else (x, y), color)
            print("{0} {1} ({2})".format(x, y, t))
        print("\n\n")

    def clear(self):
        self.screen.fill(self.fill_color)

    def render(self, obj):
        pass

    def render_objects(self, objects):
        for obj in objects:
            for vertex in obj.vertices:
                x = round(vertex.x * 120 + self.get_width() / 2.0)
                y = round(self.get_height() - (vertex.y * 120 + self.get_width() / 2.0))
                print(f"HUI {x} :: {y}")
                self.screen.set_at((x + obj.pos.x, y + obj.pos.y), obj.vertex_color)

    def present(self):
        pygame.display.flip()

    def get_width(self):
        return self.screen.get_width()

    def get_height(self):
        return self.screen.get_height()

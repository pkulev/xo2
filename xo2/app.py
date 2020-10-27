"""EAF application implementation with pygame support."""

from typing import Optional

import eaf.app
import pygame

from xo2.render import SpriteRenderer


class Application(eaf.app.Application):
    """Pygame-powered application class."""

    def __init__(self, resolution=(0, 0), flags=0, depth=0):
        window = pygame.display.set_mode(resolution, flags, depth)
        renderer = SpriteRenderer(window)

        super().__init__(renderer)

    def set_caption(self, caption: str, icontitle: str = ""):
        """Set window caption.

        :param caption: window caption
        :param icontitle: short title
        """

        pygame.display.set_caption(caption, icontitle)

    def stop(self):
        self._ioloop.add_callback(pygame.quit)
        super().stop()

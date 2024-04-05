import pygame
from game.entity_groups import ALL_ENTITIES


class Entity(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface):
        super().__init__()

        self.surf = surface
        self.rect = self.surf.get_rect()
        self.hidden = False

        ALL_ENTITIES.add(self)

    def hide(self):
        if not self.hidden:
            ALL_ENTITIES.remove(self)
            self.hidden = True

    def show(self):
        if self.hidden:
            ALL_ENTITIES.add(self)
            self.hidden = False

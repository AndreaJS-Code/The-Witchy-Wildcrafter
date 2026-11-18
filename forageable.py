from random import randint
from pygame.sprite import Sprite

from settings import *

class Forageable(Sprite):
    """Create objects collectable by the player"""

    def __init__(self, game, subtype):
        """Initialize gatherable objects"""

        super().__init__()
        self.screen = game.screen
        self.object_spawn_limit = game.player.object_spawn_limit
        self.forage = game.forage
        self.subtype = subtype

        # To make sure that forageable items don't spawn on impassable blocks
        self.terrain_collisions = game.terrain_collisions

        self.image = self.load_images()
        self.rect = self.image.get_frect()

        self.x_pos = randint(1, 18) * TILE_SIZE + 32
        self.y_pos = randint(1, 18) * TILE_SIZE + 32
        self.check_position()

        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    def load_images(self):
        """Load image of item depending on type"""

        if self.subtype == 'herb':
            self.image = pygame.image.load('images/forage/plant.png').convert_alpha()
        if self.subtype == 'mushroom':
            self.image = pygame.image.load('images/forage/mushroom.png').convert_alpha()

        return self.image

    def check_position(self):
        """Check the position of the item against terrain blocks"""

        # Flag
        overlap = False

        # Check for overlap with terrain
        for sprite in self.terrain_collisions.sprites():
            if sprite.rect.colliderect(self.rect):
                overlap = True
                break

        # Check for overlap with other forageable sprites
        if not overlap:
            for sprite in self.forage:
                if sprite != self and sprite.rect.colliderect(self.rect):
                    overlap = True
                    break

        # Make sure position adjustment didn't cause another overlap elsewhere
        if overlap:
            self.x_pos = randint(1, 18) * TILE_SIZE + 32
            self.y_pos = randint(1, 18) * TILE_SIZE + 32
            self.rect.centerx = self.x_pos
            self.rect.centery = self.y_pos
            self.check_position()

    def display_forage(self):
        """Display collectable item on screen"""

        self.screen.blit(self.image, self.rect)


from settings import *

class TerrainSprite(pygame.sprite.Sprite):
    """Create sprite objects that can be interacted with"""

    def __init__(self, position, image, groups):
        """Initialize terrain object for collision detection"""

        super().__init__(groups)
        self.x_pos, self.y_pos = position
        self.image = image
        self.rect = self.image.get_frect(topleft = position)
        self.prev_rect = self.rect.copy()
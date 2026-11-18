from settings import *

class Player:
    """Class to manage player actions"""

    def __init__(self, game):
        """Initialize the player class"""

        self.screen = game.screen
        self.terrain_collisions = game.terrain_collisions

        # Load player sprite
        self.player_image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.player_image.get_frect()
        self.prev_rect = self.rect.copy()

        # Start player at the top-center of the screen
        self.rect.y = TILE_SIZE - self.rect.height
        self.rect.centerx = WINDOW_WIDTH / 2

        # Player attributes
        self.player_speed = 5
        self.object_spawn_limit = 5
        self.carry_capacity = 3

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_player(self):
        """Update player position"""

        # Update horizontal movement
        if self.moving_right:
            self.rect.x += self.player_speed
        if self.moving_left:
            self.rect.x -= self.player_speed
        self.detect_collision('horizontal')

        # Update vertical movement
        if self.moving_up:
            self.rect.y -= self.player_speed
        if self.moving_down:
            self.rect.y += self.player_speed
        self.detect_collision('vertical')

    def detect_collision(self, axis):
        """Detect player collision with other objects"""

        self.current_rect = self.rect.copy()

        for sprite in self.terrain_collisions.sprites():
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    # Left side
                    if (self.rect.left <= sprite.rect.right and
                            self.prev_rect.left >= sprite.prev_rect.right):
                        self.rect.left = sprite.rect.right
                    # Right side
                    if (self.rect.right >= sprite.rect.left and
                            self.prev_rect.right <= sprite.prev_rect.left):
                        self.rect.right = sprite.rect.left
                elif axis == 'vertical':
                    # Top
                    if (self.rect.top <= sprite.rect.bottom and
                            self.prev_rect.top >= sprite.prev_rect.bottom):
                        self.rect.top = sprite.rect.bottom
                    # Bottom
                    if (self.rect.bottom >= sprite.rect.top and
                            self.prev_rect.bottom <= sprite.prev_rect.top):
                        self.rect.bottom = sprite.rect.top

        self.prev_rect = self.current_rect.copy()

    def display_player(self):
        """Draw player on screen"""

        self.screen.blit(self.player_image, self.rect)

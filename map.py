import csv

from terrain_sprite import TerrainSprite
from settings import *

class Map:
    """Create map displays for player to navigate"""

    def __init__(self, game):
        """Initialize maps"""

        self.screen = game.screen
        self.terrain_collisions = game.terrain_collisions

        # Stores map variants
        self.map_list = []

        # Pull map data from text files
        for map_num in range(0, 4):
            with open("maps/game_map_" + str(map_num) + ".txt", "r") as csvfile:
                reader = csv.reader(csvfile, delimiter='\t')
                game_map = [[int(val) for val in row] for row in reader]
                self.map_list.append(game_map)

        # Import tile images
        self.dirt_block = pygame.image.load("images/terrain/dirt.png").convert_alpha()
        self.bush_block = pygame.image.load("images/terrain/bushes.png").convert_alpha()

        # Set active map (default)
        self.active_map = self.set_active_map(0)

        # Build default map
        self.new_map_flag = True
        self.build_map()

    def set_active_map(self, map_num):
        """Sets the active map"""

        self.active_map = self.map_list[map_num]
        return self.active_map

    def build_map(self):
        """Build the map for display"""

        y_pos = 0
        for row in self.active_map:
            x_pos = 0
            for tile in row:
                if tile == 0:
                    self.screen.blit(self.dirt_block, (x_pos * TILE_SIZE,
                                                       y_pos * TILE_SIZE))
                if tile == 1:
                    self.screen.blit(self.bush_block, (x_pos * TILE_SIZE,
                                                       y_pos * TILE_SIZE))
                    if self.new_map_flag:
                        # Tiles need to be registered to detect collision
                        TerrainSprite((x_pos * TILE_SIZE, y_pos *
                                           TILE_SIZE),
                                      self.bush_block, self.terrain_collisions)
                x_pos += 1
            y_pos += 1
        self.new_map_flag = False
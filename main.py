from random import randint

from settings import *
from map import Map
from player import Player
from forageable import Forageable

class Game:
    """Class to manage game execution"""

    def __init__(self):
        """Initialize game and set up screen"""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.terrain_collisions = pygame.sprite.Group()

        # Game window and title
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("The Witch's Wildcrafter")

        # Create assets
        self.map = Map(self)
        self.player = Player(self)
        self.forage = pygame.sprite.Group()
        self._spawn_forage()

    def _spawn_forage(self):
        """Create forageable items"""

        while len(self.forage) < self.player.object_spawn_limit:
            plant_type = randint(0, 1)

            if plant_type == 0:
                self.forage.add(Forageable(self, 'herb'))
            elif plant_type == 1:
                self.forage.add(Forageable(self, 'mushroom'))

    def _check_events(self):
        """Check for player input events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_events(mouse_pos)

    def _check_keydown_events(self, event):
        """Check for key presses"""
        if event.key == pygame.K_d:
            self.player.moving_right = True
        if event.key == pygame.K_a:
            self.player.moving_left = True
        if event.key == pygame.K_w:
            self.player.moving_up = True
        if event.key == pygame.K_s:
            self.player.moving_down = True

    def _check_keyup_events(self, event):
        """Check for released keys"""

        if event.key == pygame.K_d:
            self.player.moving_right = False
        if event.key == pygame.K_a:
            self.player.moving_left = False
        if event.key == pygame.K_w:
            self.player.moving_up = False
        if event.key == pygame.K_s:
            self.player.moving_down = False

    def _check_mouse_events(self, mouse_pos):
        pass

    def _update_positions(self):
        """Update asset positions"""

        self.player.update_player()

    def _update_display(self):
        """Update screen to reflect changes in positions"""

        self.player.display_player()
        for plant in self.forage:
            plant.display_forage()

        pygame.display.update()

    def run(self):
        """Main game loop"""

        while True:
            self.clock.tick(FPS)
            self._check_events()

            self.map.build_map()
            self._update_positions()
            self._update_display()

if __name__ == '__main__':
    game = Game()
    game.run()

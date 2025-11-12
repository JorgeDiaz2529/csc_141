import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()
        self.bg_color = self.settings.bg_color

        self.ship = Ship(self)

    def run_game(self):
        #starts the main loop
        while True:
            self._check_events()
            
            #move ship
            self.ship.update()

            #redraw the screen
            self._update_screen()

            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
                
    
    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.direction[0] += 1 # move right
        if event.key == pygame.K_LEFT:
            self.ship.direction[0] -= 1

        if event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.direction[0] -= 1
        if event.key == pygame.K_LEFT:
            self.ship.direction[0] += 1
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

                

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
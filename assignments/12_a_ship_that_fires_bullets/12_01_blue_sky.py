import pygame
import sys

class BlueSky():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640,640))
        pygame.display.set_caption("Blue Sky (except not really)")

        self.clock = pygame.time.Clock()
        self.bg_color = (135, 206, 235)
    
    def run_game(self):
        while True:
            self._check_events()

            self.screen.fill(self.bg_color)

            pygame.display.flip()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    ai = BlueSky()
    ai.run_game()
import pygame
import sys

class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640,640))
        pygame.display.set_caption("Game Character")

        self.clock = pygame.time.Clock()
        self.bg_color = (135, 206, 235)

        self.garry = Garry(self)
    
    def run_game(self):
        while True:
            self._check_events()

            self._update_screen()

            pygame.display.flip()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        self.screen.fill((255,255,255)) # matches the sprite bg
        self.garry.blitme()

class Garry:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("12_a_ship_that_fires_bullets/images/garry.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

if __name__ == "__main__":
    ai = Game()
    ai.run_game()
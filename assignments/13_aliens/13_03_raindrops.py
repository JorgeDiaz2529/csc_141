import pygame
from pygame.sprite import Sprite
import sys

class Rain:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640,640))
        pygame.display.set_caption("Rain")

        self.bg_color = (255,255,0)
        self.raindrops = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self._create_raindrops()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self._update_screen()
            self._update_raindrops()

            pygame.display.flip()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)
    
    def _create_raindrops(self):
        rain = Raindrop(self)
        rain_width, rain_height = rain.rect.size

        current_x, current_y = rain_width, rain_height
        while current_y < (640 - rain_height):
            while current_x < (640 - rain_width):
                self._create_raindrop(current_x, current_y)
                current_x += 1.5 * rain_width
            
            current_x = rain_width
            current_y += 1.5 * rain_height

    def _create_raindrop(self, xPos, yPos):
        rain = Raindrop(self)
        rain.x = xPos
        rain.rect.x = xPos
        rain.rect.y = yPos
        self.raindrops.add(rain)
    
    def _update_raindrops(self):
        self._raindrop_fall()

    def _raindrop_fall(self):
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += 1

class Raindrop(Sprite):
    def __init__(self, program):
        super().__init__()
        self.screen = program.screen

        self.image = pygame.image.load("images/raindrop.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

if __name__ == '__main__':
    program = Rain()
    program.run()
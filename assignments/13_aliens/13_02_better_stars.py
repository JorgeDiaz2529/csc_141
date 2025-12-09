import pygame
from pygame.sprite import Sprite
import sys
from random import randint

class Starfield:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640,640))
        pygame.display.set_caption("Starfield")

        self.bg_color = (255,255,0)
        self.stars = pygame.sprite.Group()

        self._create_starfield()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self._update_screen()

            pygame.display.flip()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
    
    def _create_starfield(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (640 - star_height):
            while current_x < (640 - star_width):
                self._create_star(current_x, current_y)
                current_x += (randint(0,4)/ randint(2,4)) * star_width
            
            current_x = star_width
            current_y += (randint(12,16)/10) * star_height

    def _create_star(self, xPos, yPos):
        star = Star(self)
        star.x = xPos
        star.rect.x = xPos
        star.rect.y = yPos
        self.stars.add(star)

class Star(Sprite):
    def __init__(self, program):
        super().__init__()
        self.screen = program.screen

        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

if __name__ == '__main__':
    program = Starfield()
    program.run()
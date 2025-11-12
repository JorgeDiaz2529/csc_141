import pygame
import sys

class KeyEventTest:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((512,512))
        pygame.display.set_caption("Key Event Test")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                if event.type == pygame.QUIT:
                    sys.exit()
    
if __name__ == '__main__':
    program = KeyEventTest()
    program.run()
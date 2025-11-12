import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((512,512))
        pygame.display.set_caption("The Rocket Game")

        self.clock = pygame.time.Clock()

        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self._check_events()

            self.rocket.update()

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
            self.rocket.direction[0] += 1 # move right
        if event.key == pygame.K_LEFT:
            self.rocket.direction[0] -= 1 # move left
        
        if event.key == pygame.K_UP:
            self.rocket.direction[1] += 1
        if event.key == pygame.K_DOWN:
            self.rocket.direction[1] -= 1

        if event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_event(self, event):
        #x direction
        if event.key == pygame.K_RIGHT:
            self.rocket.direction[0] -= 1
        if event.key == pygame.K_LEFT:
            self.rocket.direction[0] += 1
        
        #y direction
        if event.key == pygame.K_UP:
            self.rocket.direction[1] -= 1
        if event.key == pygame.K_DOWN:
            self.rocket.direction[1] += 1
    
    def _update_screen(self):
        self.screen.fill((255,255,255))
        self.rocket.blitme()

class Rocket:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("12_a_ship_that_fires_bullets/images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.direction = [0,0] # x & y
        self.speed = 2
    
    def blitme(self):
        #draws the ship
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        # x direction
        if self.direction[0] == 1 and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.direction[0] == -1 and self.rect.left > 0:
            self.rect.x -= self.speed
        
        #y direction
        if self.direction[1] == 1 and self.rect.top > 0:
            self.rect.y -= self.speed #up
        if self.direction[1] == -1 and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed #down
        
        #note: maybe find a way to normalize diagonal moving in pygame

if __name__ == '__main__':
    ai = Game()
    ai.run_game()
import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("12_a_ship_that_fires_bullets/images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.direction = [0,0] # x & y
        self.speed = ai_game.settings.ship_speed
    
    def blitme(self):
        #draws the ship
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        # no going out of bounds!!
        if self.direction[0] == 1 and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.direction[0] == -1 and self.rect.left > 0:
            self.rect.x -= self.speed

        #x direction
        # self.rect.x += self.direction[0] * self.speed


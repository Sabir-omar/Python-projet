import pygame
import random

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 7
        self.player=player
        self.image = pygame.image.load('assets/projectile/projectile.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 150
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectil
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #verifier monster avec projetcil
        for monster in self.player.game.check_collision(self,self.player.game.all_monster):
            #remove projetctile
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

        # check projectile
        if self.rect.x > 1080:
            #remove projectile
            self.remove()

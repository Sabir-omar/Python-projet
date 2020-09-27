import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self,game):

        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect =self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = random.randint(1,3)

    def damage(self,amount):
        self.health -= amount

        #verifer la vie inferieur ou agale a 0
        if self.health <= 0:
            #redeplacer
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health


    def update_health_bar(self,surface):

        #show bar
        pygame.draw.rect(surface, (98, 118, 121), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface,(55, 217, 239),[self.rect.x + 10 ,self.rect.y - 20,self.health,5])

    def forward(self):
        #deplacement only if there are not coller(monster & player)
        if not self.game.check_collision(self,self.game.all_player):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

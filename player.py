import pygame
from projectile import Projectile

class player(pygame.sprite.Sprite) :

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_helth = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self,amount):
        if self.health - amount > amount:
         self.health -= amount
        else:
            #if the player deat
            self.game.game_over()

    def update_health_bar(self,surface):

        #show bar
        pygame.draw.rect(surface, (98, 118, 121), [self.rect.x + 50, self.rect.y + 20, self.max_helth, 7])
        pygame.draw.rect(surface,(55, 217, 239),[self.rect.x + 50 ,self.rect.y + 20,self.health,7])

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
    def move_right(self):
        #si le joueur n'est pas coller avec un monster
        if not self.game.check_collision(self,self.game.all_monster):
         self.rect.x += self.velocity

    def move_Left(self):
        self.rect.x -= self.velocity

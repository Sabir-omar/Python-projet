import pygame
from player import player
from monster import Monster

class Game:
    def __init__(self):
        self.player = player(self)
        self.all_player = pygame.sprite.Group()
        self.player = player(self)
        self.all_player.add(self.player)
        #group of monster
        self.all_monster=pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def check_collision(selfself ,sprite ,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)
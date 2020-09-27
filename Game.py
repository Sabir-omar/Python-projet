import pygame
from player import player
from monster import Monster

class Game:

    def __init__(self):
        #check if the game is on
        self.is_playing = False
        # group of player
        self.player = player(self)
        self.all_player = pygame.sprite.Group()
        self.player = player(self)
        self.all_player.add(self.player)
        #group of monster
        self.all_monster=pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_helth
        self.is_playing = False

    def update(self, screen):
        # appliquer de joueur
        screen.blit(self.player.image, self.player.rect)

        # upgarde life player
        self.player.update_health_bar(screen)

        # recuperer les projec du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # move monster
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer les projectile
        self.player.all_projectiles.draw(screen)

        # appliquer les monster
        self.all_monster.draw(screen)

        # check player left or right
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_Left()

    def check_collision(selfself ,sprite ,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)
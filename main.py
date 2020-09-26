import pygame
from Game import Game
import player

pygame.init()

#generer le game

pygame.display.set_caption("Luminix Game")
screen = pygame.display.set_mode((1080,720))

# importer et charger le bg
background =pygame.image.load('assets/bg.jpg')

#charger le jeu

game=Game()

running = True

while running:
    #appliquer l'arriere plan

    screen.blit(background,(0,-200))

    # appliquer de joueur
    screen.blit(game.player.image,game.player.rect)

    #recuperer les projec du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #move monster
    for monster in game.all_monster:
        monster.forward()

    #appliquer les projectile
    game.player.all_projectiles.draw(screen)

    # appliquer les monster
    game.all_monster.draw(screen)

    #check player left or right
    if game.pressed.get(pygame.K_RIGHT)and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0:
        game.player.move_Left()

    #mettre à jour l'ecran

    pygame.display.flip()

    #Exit the game
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #Connect player whit keyboard
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key]=True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key]=False
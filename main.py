import pygame
import math
from Game import Game
import player

pygame.init()

#generer le game

pygame.display.set_caption("Luminix Game")
screen = pygame.display.set_mode((1080,720))

# importer et charger le bg
background =pygame.image.load('assets/bg.jpg')

# charger banneire
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# charger Button
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#charger le jeu

game=Game()

running = True

while running:
    #appliquer l'arriere plan

    screen.blit(background,(0,-200))

    #check if game is on
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, (play_button_rect))
        screen.blit(banner,banner_rect)

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

        elif event.type == pygame.MOUSEBUTTONDOWN :
            #check is clicked
            if play_button_rect.collidepoint(event.pos):
                game.start()
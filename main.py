import pygame
pygame.init()

#generer le game

pygame.display.set_caption("Luminix Game")
screen = pygame.display.set_mode((1080,720))
# importer et charger le bg

background =pygame.image.load('assets/bg.jpg')
running = True

while running:
    #appliquer l'arriere plan

    screen.blit(background,(0,-200))

    #mettre à jour l'ecran

    pygame.display.flip()

    #Exit the game
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

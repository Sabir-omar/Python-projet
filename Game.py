import pygame
from player import player

class Game:
    def __init__(self):
        self.player = player()
        self.pressed = {}
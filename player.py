# Importing libraries
import pygame

# Importing files
import game
import scale


class Player:
    def __init__(self):
        self.color = (0, 0, 235)
        self.life = 100
        self.sizeY = 20
        self.sizeX = 20
        self.positionX = 935
        self.positionY = 515
        self.speed = 2

    def draw(self):
        pygame.draw.rect(game.screen, self.color, (self.positionX, self.positionY, self.sizeX, self.sizeY))

    def move_up(self):
        self.positionY = self.positionY + scale.fps(-self.speed)

    def move_down(self):
        self.positionY = self.positionY + scale.fps(self.speed)

    def move_left(self):
        self.positionX = self.positionX + scale.fps(-self.speed)

    def move_right(self):
        self.positionX = self.positionX + scale.fps(self.speed)

# Importing libraries
import pygame

# Importing files
import game
import scale


class Player:
    def __init__(self):
        self.color = (0, 0, 235)
        self.life = 100
        self.sizeY = scale.y(20)
        self.sizeX = scale.x(20)
        self.positionX = scale.x(935)
        self.positionY = scale.y(515)
        self.speed = scale.fps(scale.movement(2))

    def draw(self):
        pygame.draw.rect(game.screen, self.color, (self.positionX, self.positionY, self.sizeX, self.sizeY))

    def move_up(self):
        self.positionY = self.positionY + -self.speed

    def move_down(self):
        self.positionY = self.positionY + self.speed

    def move_left(self):
        self.positionX = self.positionX + -self.speed

    def move_right(self):
        self.positionX = self.positionX + self.speed

    def positionX(self):
        return self.positionX
    
    def positionY(self):
        return self.positionY
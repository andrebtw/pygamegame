# Importing libraries
import pygame
import random

# Importing files
import game
import math
import scale


class Zombie:
    def __init__(self, round):
        self.color = (235, 0, 0)
        self.life = random.randint(50, 150)*round 
        self.sizeY = scale.y(int(((20*self.life)/100)/round))
        self.sizeX = scale.x(int(((20*self.life)/100)/round))
        self.positionX = scale.x(random.randint(0, 1920))
        self.positionY = scale.y(random.randint(0, 1080))
        self.speed = scale.fps(scale.movement(int(((2*self.life)/100)/round)))
        
    def draw(self):
        pygame.draw.rect(game.screen, self.color, (int(self.positionX), int(self.positionY), self.sizeX, self.sizeY))

    def follow(self, player_positionX, player_positionY):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player_positionX - self.positionX, player_positionY - self.positionY
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.positionX += dx * self.speed
        self.positionY += dy * self.speed
        print(self.positionX, self.positionY)
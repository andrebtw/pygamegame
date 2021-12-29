# Importing libraries
import pygame
from pygame.locals import *
import time
import random
import math
import sys
import re
import os

# Importing files
import constants
import scale
import rounds

# Configuration

path = ""

data_file = open(f"{path}files/data/data.txt", "r")  # Opening the data file
data = data_file.readlines()  # Making a list from every line

pygame.init()
main_clock = pygame.time.Clock()

fps = int(re.sub("[^0-9]", "", data[3]))

width = int(re.sub("[^0-9]", "", data[1]))  # re.sub("[^0-9]", "",") removes all non numeric characters from the data
height = int(re.sub("[^0-9]", "", data[2]))

points = int(re.sub("[^0-9]", "", data[6]))

if "FALSE" in data[0]:
    fullscreen = False
    screen = pygame.display.set_mode((width, height))
else:
    fullscreen = True
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


def update():
    pygame.display.update()


class Player:
    def __init__(self):
        self.color = (0, 0, 235)
        self.life = 100
        self.sizeY = 50
        self.sizeX = 50
        self.positionX = 935
        self.positionY = 515

    def spawn(self):
        pygame.draw.rect(screen, self.color, (self.positionX, self.positionY, self.sizeX, self.sizeY))


class Obstacle:
    def __init__(self):
        pass


class Zombie:
    def __init__(self):
        pass


def main_game():
    screen.fill(constants.black)
    update()

    round = 1

    running = True

    rounds.round_start(round)

    player = Player()

    player.spawn()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                quit()

        update()
        main_clock.tick(fps)

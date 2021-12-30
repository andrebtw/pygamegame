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
from player import Player
from obstacle import Obstacle
from zombie import Zombie
from logs import log

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


def main_game():
    screen.fill(constants.black)
    update()

    round = 1

    running = True

    rounds.round_start(round)

    player = Player()

    moving_up = None
    moving_down = None
    moving_left = None
    moving_right = None

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    moving_up = True
                if event.key == pygame.K_s:
                    moving_down = True
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    moving_up = False
                if event.key == pygame.K_s:
                    moving_down = False
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False

        print(moving_up)
        if moving_up:
            player.move_up()

        if moving_down:
            player.move_down()

        if moving_left:
            player.move_left()

        if moving_right:
            player.move_right()

        screen.fill(constants.black)
        player.draw()
        update()
        main_clock.tick(fps)

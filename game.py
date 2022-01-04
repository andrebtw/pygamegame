# Importing libraries
import pygame
from pygame.locals import *
import json

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

pygame.init()

main_clock = pygame.time.Clock()

# JSON Files opening

with open("files/data/settings.json") as jsonSettings:
    jsonSettingsObject = json.load(jsonSettings)
    jsonSettings.close()

with open("files/data/controls.json") as jsonControls:
    jsonControlsObject = json.load(jsonControls)
    jsonControls.close()

fps = jsonSettingsObject['fps']

width = jsonSettingsObject['width']
height = jsonSettingsObject['height']
fullscreen = jsonSettingsObject['fullscreen']

if fullscreen == False:
    screen = pygame.display.set_mode((width, height))
else:
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
    
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                quit()

        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[jsonControlsObject['move_up']]:
            player.move_up()

        if pressed_keys[jsonControlsObject['move_down']]:
            player.move_down()

        if pressed_keys[jsonControlsObject['move_left']]:
            player.move_left()

        if pressed_keys[jsonControlsObject['move_right']]:
            player.move_right()

        screen.fill(constants.black)
        player.draw()
        update()
        main_clock.tick(fps)
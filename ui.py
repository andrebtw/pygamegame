# Importing libraries
import pygame
from pygame.locals import *

# Importing files
import game
import constants
import scale
import rounds
from player import Player
from obstacle import Obstacle
from zombie import Zombie
from logs import log

def background():
    pygame.draw.rect(game.screen, constants.black, (scale.x(0), scale.y(980), scale.x(1920), scale.y(100)))
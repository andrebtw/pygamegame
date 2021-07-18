#Importing libraries
import pygame
from pygame.locals import *
import time
import random
import math
import sys
import re

data_file = open("files/data/data.txt", "r") #Opening the data file
data = data_file.readlines() #Making a list from every line 

pygame.init()
main_clock = pygame.time.Clock()
fps = int(re.sub("[^0-9]", "", data[3]))


width = int(re.sub("[^0-9]", "", data[1])) #re.sub("[^0-9]", "",") removes all non numeric characters from the data
height = int(re.sub("[^0-9]", "", data[2]))

if "FALSE" in data[0]:
    fullscreen=False
    screen = pygame.display.set_mode((width, height))
else : 
    fullscreen=True
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)



def scale_x (x):
    surface = pygame.display.get_surface() #get the surface of the current active display
    x=(x*surface.get_width())/1920
    x = int (x)
    return x

def scale_y (y):
    surface = pygame.display.get_surface() #get the surface of the current active display
    y=(y*surface.get_height())/1080
    y = int (y)
    return y


def game():
    screen.fill((0,0,0))
    running = True
    while running == True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                running = False
    
        pygame.display.update()
        main_clock.tick(fps)
    
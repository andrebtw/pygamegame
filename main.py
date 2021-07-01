#Importing libraries
import pygame
from pygame.locals import *
import time
import random
import math
import sys
import re


#Importing python files
from menu import menu
#from files.python.game import game

pygame.init() #Initalising pygame

data_file = open("files\data\data.txt", "r") #Opening the data file
data = data_file.readlines() #Making a list from every line 


width = int(re.sub("[^0-9]", "", data[1])) #re.sub("[^0-9]", "",") removes all non numeric characters from the data
height = int(re.sub("[^0-9]", "", data[2]))
fps = int(re.sub("[^0-9]", "", data[3]))

if "FALSE" in data[0]:
    fullscreen=False
    screen = pygame.display.set_mode((width, height))
else : 
    fullscreen=True
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


main_clock = pygame.time.Clock()
running = True

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


while running == True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            running = False

    menu() 
    pygame.display.update()
    main_clock.tick(fps)





pygame.quit()
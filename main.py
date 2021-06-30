#Importing libraries
import pygame
from pygame.locals import *
import time
import random
import math
import sys
import re


#Importing python files
from files.python.menu import menu
#from files.python.game import game

pygame.init() #Initalising pygame

data_file = open("files\data\data.txt", "r") #Opening the data file
data = data_file.readlines() #Making a list from every line 


width = int(re.sub("[^0-9]", "", data[1])) #re.sub("[^0-9]", "",") removes all non numeric characters from the data
height = int(re.sub("[^0-9]", "", data[2]))

if "FALSE" in data[0]:
    fullscreen=False
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
else : 
    fullscreen=True
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


main_clock = pygame.time.Clock()
running = True


while running == True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            running = False

        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
    pygame.display.update()
    main_clock.tick(60)
    menu()


pygame.quit()
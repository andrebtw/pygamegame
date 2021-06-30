#Importing libraries
import pygame
from pygame.locals import *
import time
import random
import math
import sys
import re


data_file = open("files\data\data.txt", "r") #Opening the data file
data = data_file.readlines() #Making a list from every line 


width = int(re.sub("[^0-9]", "", data[1])) #re.sub("[^0-9]", "",") removes all non numeric characters from the data
height = int(re.sub("[^0-9]", "", data[2]))

if "FALSE" in data[0]:
    fullscreen=False
    screen = pygame.display.set_mode((width, height))
else : 
    fullscreen=True
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


main_clock = pygame.time.Clock()
running = True



def menu ():
    surface = pygame.display.get_surface() #get the surface of the current active display
    #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500*surface.get_width()/1920,500*surface.get_height()/1080,500*surface.get_width()/1920,500*surface.get_height()/1080))
    









if __name__ == "__main__":
    menu()
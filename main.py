#Importing libraries
import pygame
from pygame.locals import *
import time
import random
import math 

pygame.init() #Initalising pygame

width = 1920
height = 1080

screen = pygame.display.set_mode((width, height))

running = True

while running == True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            running = False
    
    


pygame.quit()
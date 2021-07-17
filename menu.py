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


main_clock = pygame.time.Clock()



def menu ():
    running = True
    while running == True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                running = False


        ###DEFINING FONTS###
        neon_font_play = pygame.font.Font("files/assets/fonts/NEON GLOW.otf", scale_x(150))
        neon_font_settings_exit = pygame.font.Font("files/assets/fonts/NEON GLOW.otf", scale_y(100))


        ###PLACING FONTS###
        text_settings = neon_font_settings_exit.render("SETTINGS", True, (0,128,0))
        text_play = neon_font_play.render("PLAY", True, (176, 38, 255))
        text_exit = neon_font_settings_exit.render("QUIT", True, (0,128,0))
        
        surface = pygame.display.get_surface() #get the surface of the current active display
        #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500*surface.get_width()/1920,500*surface.get_height()/1080,500*surface.get_width()/1920,500*surface.get_height()/1080))
        screen.blit(text_settings,(scale_x(960) - text_settings.get_width() // 2, scale_y(200)))
        screen.blit(text_play,(scale_x(960) - text_play.get_width() // 2, scale_y(462)))
        screen.blit(text_exit,(scale_x(960) - text_exit.get_width() // 2, scale_y(774)))
    


if __name__ == "__main__":
    menu()
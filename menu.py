#Importing libraries
import pygame
from pygame.locals import *
import time
import random
import math
import sys
import re

#Importing python files
from settings import settings
from game import game


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



def menu ():
    ###DEFINING FONTS###
    neon_font_play = pygame.font.Font("files/assets/fonts/NEON GLOW.otf", scale_x(150))
    neon_font_settings_exit = pygame.font.Font("files/assets/fonts/NEON GLOW.otf", scale_y(100))
    
     ###Making the texts###
    text_settings = neon_font_settings_exit.render("SETTINGS", True, (199,79,230))
    text_play = neon_font_play.render("PLAY", True, (84, 79, 240))
    text_exit = neon_font_settings_exit.render("QUIT", True, (199,79,230))

    running = True
    screen.fill((0,0,0))

    while running == True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                running = False
        
        surface = pygame.display.get_surface() #get the surface of the current active display

        ###Defining fonts positions on the screen###
        text_settings_pos = (scale_x(960) - text_settings.get_width() // 2, scale_y(200))
        text_play_pos = (scale_x(960) - text_play.get_width() // 2, scale_y(462))
        text_exit_pos = (scale_x(960) - text_exit.get_width() // 2, scale_y(774)) 
        
        ###Displaying the texts###
        screen.blit(text_settings,(text_settings_pos))
        screen.blit(text_play,(text_play_pos))
        screen.blit(text_exit,(text_exit_pos))
        
        ###Getting the rectangle position of each text###
        text_settings_rect = text_settings.get_rect()
        text_settings_rect.x = scale_x(960) - text_settings.get_width() // 2
        text_settings_rect.y = scale_y(200)

        text_play_rect = text_play.get_rect()
        text_play_rect.x = scale_x(960) - text_play.get_width() // 2
        text_play_rect.y = scale_y(462)

        text_exit_rect = text_exit.get_rect()
        text_exit_rect.x = scale_x(960) - text_exit.get_width() // 2
        text_exit_rect.y = scale_y(774)

        mouse_pos = pygame.mouse.get_pos() # Get mouse position


        if text_settings_rect.collidepoint(mouse_pos): # Check if position is in the rect
            print("Settings hovered")
            text_settings = neon_font_settings_exit.render("SETTINGS", True, (255,255,255))
        else:
            text_settings = neon_font_settings_exit.render("SETTINGS", True, (199,79,230))

        if text_play_rect.collidepoint(mouse_pos): # Check if position is in the rect
            print("Play hovered")
            text_play = neon_font_play.render("PLAY", True, (255, 255, 255))
        else:
            text_play = neon_font_play.render("PLAY", True, (84, 79, 240))

        if text_exit_rect.collidepoint(mouse_pos): # Check if position is in the rect
            print("Quit hovered")
            text_exit = neon_font_settings_exit.render("QUIT", True, (255,255,255))
        else:
            text_exit = neon_font_settings_exit.render("QUIT", True, (199,79,230))

        
        if event.type == pygame.MOUSEBUTTONUP:
            if text_settings_rect.collidepoint(mouse_pos):
                running = False
                settings()

            if text_play_rect.collidepoint(mouse_pos):
                game()

            if text_exit_rect.collidepoint(mouse_pos):
                running = False

        pygame.display.update()
        main_clock.tick(fps)


if __name__ == "__main__":
    menu()
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



###COLORS###
blue1 = (84, 79, 240)
purple1 = (199,79,230)
white = (255,255,255)


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



###SETTINGS###
def audio_settings():
    screen.fill((0,0,0))
    running = True

    ###Defining fonts###
    neon_font_text = pygame.font.Font("files/assets/fonts/NEON GLOW.otf", scale_y(100))

    ###Making the texts
    back_text = neon_font_text.render("BACK", True, (purple1))

    while running == True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                running = False
            

            surface = pygame.display.get_surface() #get the surface of the current active display

            ###Defining fonts positions on the screen###
            back_text_pos = (scale_x(125), scale_y(75))

            #Displaying the text
            screen.blit(back_text,(back_text_pos))

            ###Getting the rectangle position of each text###
            back_text_rect = back_text.get_rect()
            back_text_rect.x = scale_x(125)
            back_text_rect.y = scale_y(75)

            mouse_pos = pygame.mouse.get_pos() # Get mouse position

            if back_text_rect.collidepoint(mouse_pos): # Check if position is in the rect
                print("Back hovered")
                back_text = neon_font_text.render("BACK", True, (white))
            else:
                back_text = neon_font_text.render("BACK", True, (purple1))

            
            if event.type == pygame.MOUSEBUTTONUP:
                if back_text_rect.collidepoint(mouse_pos):
                    running = False
                    settings()
            
        pygame.display.update()
        main_clock.tick(fps)




def video_settings():
    screen.fill((0,0,0))
    running = True

    while running == True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                running = False
            
        pygame.display.update()
        main_clock.tick(fps)



def about_settings():
    screen.fill((0,0,0))
    running = True

    while running == True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                running = False

        pygame.display.update()
        main_clock.tick(fps)



def settings():
    screen.fill((0,0,0))
    running = True

    ###Defining fonts###
    neon_font_text = pygame.font.Font("files/assets/fonts/NEON GLOW.otf", scale_y(100))


    ###Making the texts
    audio_text = neon_font_text.render("AUDIO", True, (purple1))
    video_text = neon_font_text.render("VIDEO", True, (blue1))
    about_text = neon_font_text.render("ABOUT", True, (purple1))
    back_text = neon_font_text.render("BACK", True, (purple1))

    while running == True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                running = False
        

            surface = pygame.display.get_surface() #get the surface of the current active display

            ###Defining fonts positions on the screen###
            audio_text_pos = (scale_x(960) - audio_text.get_width() // 2, scale_y(200))
            video_text_pos = (scale_x(960) - video_text.get_width() // 2, scale_y(462))
            about_text_pos = (scale_x(960) - about_text.get_width() // 2, scale_y(724)) 
            back_text_pos = (scale_x(125), scale_y(75))
            
            ###Displaying the texts###
            screen.blit(audio_text,(audio_text_pos))
            screen.blit(video_text,(video_text_pos))
            screen.blit(about_text,(about_text_pos))
            screen.blit(back_text,(back_text_pos))

            ###Getting the rectangle position of each text###
            audio_text_rect = audio_text.get_rect()
            audio_text_rect.x = scale_x(960) - audio_text.get_width() // 2
            audio_text_rect.y = scale_y(200)

            video_text_rect = video_text.get_rect()
            video_text_rect.x = scale_x(960) - video_text.get_width() // 2
            video_text_rect.y = scale_y(462)

            about_text_rect = about_text.get_rect()
            about_text_rect.x = scale_x(960) - about_text.get_width() // 2
            about_text_rect.y = scale_y(724)

            back_text_rect = back_text.get_rect()
            back_text_rect.x = scale_x(125)
            back_text_rect.y = scale_y(75)

            mouse_pos = pygame.mouse.get_pos() # Get mouse position


            if audio_text_rect.collidepoint(mouse_pos): # Check if position is in the rect
                print("Audio hovered")
                audio_text = neon_font_text.render("AUDIO", True, (white))
            else:
                audio_text = neon_font_text.render("AUDIO", True, (purple1))

            if video_text_rect.collidepoint(mouse_pos): # Check if position is in the rect
                print("Video hovered")
                video_text = neon_font_text.render("VIDEO", True, (white))
            else:
                video_text = neon_font_text.render("VIDEO", True, (blue1))

            if about_text_rect.collidepoint(mouse_pos): # Check if position is in the rect
                print("About hovered")
                about_text = neon_font_text.render("ABOUT", True, (white))
            else:
                about_text = neon_font_text.render("ABOUT", True, (purple1))
            if back_text_rect.collidepoint(mouse_pos): # Check if position is in the rect
                print("Back hovered")
                back_text = neon_font_text.render("BACK", True, (white))
            else:
                back_text = neon_font_text.render("BACK", True, (purple1))


            if event.type == pygame.MOUSEBUTTONUP:
                if audio_text_rect.collidepoint(mouse_pos):
                    running = False
                    audio_settings()

                if video_text_rect.collidepoint(mouse_pos):
                    running = False
                    video_settings()

                if about_text_rect.collidepoint(mouse_pos):
                    running = False
                    about_settings()
                
                if back_text_rect.collidepoint(mouse_pos):
                    running = False
                    main()

        pygame.display.update()
        main_clock.tick(fps)




###MENU###

def main ():
    ###DEFINING FONTS###
    neon_font_play = pygame.font.Font("files/assets/fonts/NEON GLOW.otf", scale_x(150))
    neon_font_settings_exit = pygame.font.Font("files/assets/fonts/NEON GLOW.otf", scale_y(100))
    
     ###Making the texts###
    text_settings = neon_font_settings_exit.render("SETTINGS", True, (purple1))
    text_play = neon_font_play.render("PLAY", True, (blue1))
    text_exit = neon_font_settings_exit.render("QUIT", True, (purple1))

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
                text_settings = neon_font_settings_exit.render("SETTINGS", True, (white))
            else:
                text_settings = neon_font_settings_exit.render("SETTINGS", True, (purple1))

            if text_play_rect.collidepoint(mouse_pos): # Check if position is in the rect
                print("Play hovered")
                text_play = neon_font_play.render("PLAY", True, (white))
            else:
                text_play = neon_font_play.render("PLAY", True, (blue1))

            if text_exit_rect.collidepoint(mouse_pos): # Check if position is in the rect
                print("Quit hovered")
                text_exit = neon_font_settings_exit.render("QUIT", True, (white))
            else:
                text_exit = neon_font_settings_exit.render("QUIT", True, (purple1))

            
            if event.type == pygame.MOUSEBUTTONUP:
                if text_settings_rect.collidepoint(mouse_pos):
                    running = False
                    settings()

                if text_play_rect.collidepoint(mouse_pos):
                    running = False
                    game()

                if text_exit_rect.collidepoint(mouse_pos):
                    running = False

        pygame.display.update()
        main_clock.tick(fps)





###GAME###
def game():
    screen.fill((0,0,0))
    running = True
    while running == True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                running = False

    
        pygame.display.update()
        main_clock.tick(fps)





if __name__ == "__main__":
    main()
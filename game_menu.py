# Importing libraries
import pygame

# Importing python files
import game
import scale
import constants
import player_choice


# Main menu
def main_menu():
    # Defining fonts
    neon_font_play = pygame.font.Font(f"{game.path}files/assets/fonts/NEON GLOW.otf", scale.x(150))
    neon_font_settings_exit = pygame.font.Font(f"{game.path}files/assets/fonts/NEON GLOW.otf", scale.y(100))

    # Making the texts
    text_settings = neon_font_settings_exit.render("SETTINGS", True, constants.red1)
    text_play = neon_font_play.render("PLAY", True, constants.red2)
    text_exit = neon_font_settings_exit.render("QUIT", True, constants.red1)

    running = True
    game.screen.fill((0, 0, 0))

    while running:

        # Defining fonts positions on the screen
        text_settings_pos = (scale.x(960) - text_settings.get_width() // 2, scale.y(200))
        text_play_pos = (scale.x(960) - text_play.get_width() // 2, scale.y(462))
        text_exit_pos = (scale.x(960) - text_exit.get_width() // 2, scale.y(774))

        # Displaying the texts
        game.screen.blit(text_settings, text_settings_pos)
        game.screen.blit(text_play, text_play_pos)
        game.screen.blit(text_exit, text_exit_pos)

        for event in pygame.event.get():
            if event.type == game.QUIT:
                running = False

            surface = pygame.display.get_surface()  # get the surface of the current active display

            # Getting the rectangle position of each text
            text_settings_rect = text_settings.get_rect()
            text_settings_rect.x = scale.x(960) - text_settings.get_width() // 2
            text_settings_rect.y = scale.y(200)

            text_play_rect = text_play.get_rect()
            text_play_rect.x = scale.x(960) - text_play.get_width() // 2
            text_play_rect.y = scale.y(462)

            text_exit_rect = text_exit.get_rect()
            text_exit_rect.x = scale.x(960) - text_exit.get_width() // 2
            text_exit_rect.y = scale.y(774)

            mouse_pos = pygame.mouse.get_pos()  # Get mouse position

            if text_settings_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Settings hovered")
                text_settings = neon_font_settings_exit.render("SETTINGS", True, constants.white)
            else:
                text_settings = neon_font_settings_exit.render("SETTINGS", True, constants.red1)

            if text_play_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Play hovered")
                text_play = neon_font_play.render("PLAY", True, constants.white)
            else:
                text_play = neon_font_play.render("PLAY", True, constants.red2)

            if text_exit_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Quit hovered")
                text_exit = neon_font_settings_exit.render("QUIT", True, constants.white)
            else:
                text_exit = neon_font_settings_exit.render("QUIT", True, constants.red1)

            if event.type == pygame.MOUSEBUTTONUP:
                if text_settings_rect.collidepoint(mouse_pos):
                    running = False
                    settings()

                if text_play_rect.collidepoint(mouse_pos):
                    running = False
                    player_choice.player_choice()

                if text_exit_rect.collidepoint(mouse_pos):
                    running = False

        game.update()
        game.main_clock.tick(game.fps)


# Settings menu
def settings():
    game.screen.fill((0, 0, 0))
    running = True

    # Defining fonts
    neon_font_text = pygame.font.Font(f"{game.path}files/assets/fonts/NEON GLOW.otf", scale.y(100))

    # Making the texts
    audio_text = neon_font_text.render("AUDIO", True, constants.red1)
    video_text = neon_font_text.render("VIDEO", True, constants.red2)
    about_text = neon_font_text.render("ABOUT", True, constants.red1)
    back_text = neon_font_text.render("BACK", True, constants.red1)
    controls_text = neon_font_text.render("CONTROLS", True, constants.red2)

    while running:

        # Defining fonts positions on the screen
        audio_text_pos = (scale.x(960) - audio_text.get_width() // 2, scale.y(95))
        video_text_pos = (scale.x(960) - video_text.get_width() // 2, scale.y(365))
        controls_text_pos = (scale.x(960) - controls_text.get_width() // 2, scale.y(635))
        about_text_pos = (scale.x(960) - about_text.get_width() // 2, scale.y(905))
        back_text_pos = (scale.x(125), scale.y(75))

        # Displaying the texts
        game.screen.blit(audio_text, audio_text_pos)
        game.screen.blit(video_text, video_text_pos)
        game.screen.blit(about_text, about_text_pos)
        game.screen.blit(back_text, back_text_pos)
        game.screen.blit(controls_text, controls_text_pos)

        for event in pygame.event.get():
            if event.type == game.QUIT:
                running = False

            surface = pygame.display.get_surface()  # get the surface of the current active display

            # Getting the rectangle position of each text
            audio_text_rect = audio_text.get_rect()
            audio_text_rect.x = scale.x(960) - audio_text.get_width() // 2
            audio_text_rect.y = scale.y(95)

            video_text_rect = video_text.get_rect()
            video_text_rect.x = scale.x(960) - video_text.get_width() // 2
            video_text_rect.y = scale.y(365)

            controls_text_rect = controls_text.get_rect()
            controls_text_rect.x = scale.x(960) - controls_text.get_width() // 2
            controls_text_rect.y = scale.y(635)

            about_text_rect = about_text.get_rect()
            about_text_rect.x = scale.x(960) - about_text.get_width() // 2
            about_text_rect.y = scale.y(905)

            back_text_rect = back_text.get_rect()
            back_text_rect.x = scale.x(125)
            back_text_rect.y = scale.y(75)

            mouse_pos = pygame.mouse.get_pos()  # Get mouse position

            if audio_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Audio hovered")
                audio_text = neon_font_text.render("AUDIO", True, constants.white)
            else:
                audio_text = neon_font_text.render("AUDIO", True, constants.red1)

            if video_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Video hovered")
                video_text = neon_font_text.render("VIDEO", True, constants.white)
            else:
                video_text = neon_font_text.render("VIDEO", True, constants.red2)

            if controls_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Controls hovered")
                controls_text = neon_font_text.render("CONTROLS", True, constants.white)
            else:
                controls_text = neon_font_text.render("CONTROLS", True, constants.red2)

            if about_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("About hovered")
                about_text = neon_font_text.render("ABOUT", True, constants.white)
            else:
                about_text = neon_font_text.render("ABOUT", True, constants.red1)

            if back_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Back hovered")
                back_text = neon_font_text.render("BACK", True, constants.white)
            else:
                back_text = neon_font_text.render("BACK", True, constants.red1)

            if event.type == pygame.MOUSEBUTTONUP:
                if audio_text_rect.collidepoint(mouse_pos):
                    running = False
                    audio_settings()

                if video_text_rect.collidepoint(mouse_pos):
                    running = False
                    video_settings()

                if controls_text_rect.collidepoint(mouse_pos):
                    running = False
                    controls_settings()

                if about_text_rect.collidepoint(mouse_pos):
                    running = False
                    about_settings()

                if back_text_rect.collidepoint(mouse_pos):
                    running = False
                    main_menu()

        game.update()
        game.main_clock.tick(game.fps)


# Audio settings
def audio_settings():
    game.screen.fill((0, 0, 0))
    running = True

    # Defining fonts
    neon_font_text = pygame.font.Font(f"{game.path}files/assets/fonts/NEON GLOW.otf", scale.y(100))

    # Making the texts
    back_text = neon_font_text.render("BACK", True, constants.red1)

    while running:
        # Defining fonts positions on the screen
        back_text_pos = (scale.x(125), scale.y(75))

        # Displaying the text
        game.screen.blit(back_text, back_text_pos)

        for event in pygame.event.get():
            if event.type == game.QUIT:
                running = False

            surface = pygame.display.get_surface()  # get the surface of the current active display

            # Getting the rectangle position of each text
            back_text_rect = back_text.get_rect()
            back_text_rect.x = scale.x(125)
            back_text_rect.y = scale.y(75)

            mouse_pos = pygame.mouse.get_pos()  # Get mouse position

            if back_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Back hovered")
                back_text = neon_font_text.render("BACK", True, constants.white)
            else:
                back_text = neon_font_text.render("BACK", True, constants.red1)

            if event.type == pygame.MOUSEBUTTONUP:
                if back_text_rect.collidepoint(mouse_pos):
                    running = False
                    settings()

        game.update()
        game.main_clock.tick(game.fps)


# Video settings
def video_settings():
    game.screen.fill((0, 0, 0))
    running = True

    # Defining fonts
    neon_font_text = pygame.font.Font(f"{game.path}files/assets/fonts/NEON GLOW.otf", scale.y(100))

    # Making the texts
    back_text = neon_font_text.render("BACK", True, constants.red1)

    while running:

        # Defining fonts positions on the screen
        back_text_pos = (scale.x(125), scale.y(75))

        # Displaying the text
        game.screen.blit(back_text, back_text_pos)

        for event in pygame.event.get():

            if event.type == game.QUIT:
                running = False

            surface = pygame.display.get_surface()  # get the surface of the current active display

            # Getting the rectangle position of each text
            back_text_rect = back_text.get_rect()
            back_text_rect.x = scale.x(125)
            back_text_rect.y = scale.y(75)

            mouse_pos = pygame.mouse.get_pos()  # Get mouse position

            if back_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Back hovered")
                back_text = neon_font_text.render("BACK", True, constants.white)
            else:
                back_text = neon_font_text.render("BACK", True, constants.red1)

            if event.type == pygame.MOUSEBUTTONUP:
                if back_text_rect.collidepoint(mouse_pos):
                    running = False
                    settings()

        game.update()
        game.main_clock.tick(game.fps)


# About settings
def about_settings():
    game.screen.fill((0, 0, 0))
    running = True

    # Defining fonts
    neon_font_text = pygame.font.Font(f"{game.path}files/assets/fonts/NEON GLOW.otf", scale.y(100))

    # Making the texts
    back_text = neon_font_text.render("BACK", True, constants.red1)

    while running:

        # Defining fonts positions on the screen
        back_text_pos = (scale.x(125), scale.y(75))

        # Displaying the text
        game.screen.blit(back_text, back_text_pos)

        for event in pygame.event.get():
            if event.type == game.QUIT:
                running = False

            surface = pygame.display.get_surface()  # get the surface of the current active display

            # Getting the rectangle position of each text
            back_text_rect = back_text.get_rect()
            back_text_rect.x = scale.x(125)
            back_text_rect.y = scale.y(75)

            mouse_pos = pygame.mouse.get_pos()  # Get mouse position

            if back_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Back hovered")
                back_text = neon_font_text.render("BACK", True, constants.white)
            else:
                back_text = neon_font_text.render("BACK", True, constants.red1)

            if event.type == pygame.MOUSEBUTTONUP:
                if back_text_rect.collidepoint(mouse_pos):
                    running = False
                    settings()

        game.update()
        game.main_clock.tick(game.fps)


# Controls settings
def controls_settings():
    game.screen.fill((0, 0, 0))
    running = True

    # Defining fonts
    neon_font_text = pygame.font.Font(f"{game.path}files/assets/fonts/NEON GLOW.otf", scale.y(100))

    # Making the texts
    back_text = neon_font_text.render("BACK", True, constants.red1)

    while running:
        # Defining fonts positions on the screen
        back_text_pos = (scale.x(125), scale.y(75))

        # Displaying the text
        game.screen.blit(back_text, back_text_pos)

        for event in pygame.event.get():
            if event.type == game.QUIT:
                running = False

            surface = pygame.display.get_surface()  # get the surface of the current active display

            # Getting the rectangle position of each text
            back_text_rect = back_text.get_rect()
            back_text_rect.x = scale.x(125)
            back_text_rect.y = scale.y(75)

            mouse_pos = pygame.mouse.get_pos()  # Get mouse position

            if back_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Back hovered")
                back_text = neon_font_text.render("BACK", True, constants.white)
            else:
                back_text = neon_font_text.render("BACK", True, constants.red1)

            if event.type == pygame.MOUSEBUTTONUP:
                if back_text_rect.collidepoint(mouse_pos):
                    running = False
                    settings()

        game.update()
        game.main_clock.tick(game.fps)

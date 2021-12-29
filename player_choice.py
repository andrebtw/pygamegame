# Importing libraries
import pygame

# Importing python files
import game
import scale
import constants


# Player choice
def player_choice():
    # Make a menu where the user can choose what player to choose, each player will have different skin and
    # different speed, damage health etc...

    game.screen.fill((0, 0, 0))
    game.update()

    running = True

    # Defining fonts
    neon_font_text = pygame.font.Font(f"{game.path}files/assets/fonts/NEON GLOW.otf", scale.y(125))

    # Making the texts
    start_text = neon_font_text.render("START", True, constants.red1)

    while running:
        # Defining fonts positions on the screen
        start_text_pos = (scale.x(960) - start_text.get_width() // 2, scale.y(900))

        # Displaying the text
        game.screen.blit(start_text, start_text_pos)

        for event in pygame.event.get():
            if event.type == game.QUIT:
                running = False
                quit()

            surface = pygame.display.get_surface()  # get the surface of the current active display

            # Getting the rectangle position of each text
            start_text_rect = start_text.get_rect()
            start_text_rect.x = scale.x(960) - start_text.get_width() // 2
            start_text_rect.y = scale.y(900)

            mouse_pos = pygame.mouse.get_pos()  # Get mouse position

            if start_text_rect.collidepoint(mouse_pos):  # Check if position is in the rect
                print("Start hovered")
                start_text = neon_font_text.render("START", True, constants.white)
            else:
                start_text = neon_font_text.render("START", True, constants.red1)

            if event.type == pygame.MOUSEBUTTONUP:
                if start_text_rect.collidepoint(mouse_pos):
                    running = False
                    game.main_game()

        game.update()
        game.main_clock.tick(game.fps)
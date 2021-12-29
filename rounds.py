# Importing libraries
import pygame

# Importing python files
import game
import scale
import constants


def round_start(round):
    # Defining the color
    fading_color = (0, 0, 0)
    fading_red = 0

    # Defining fonts
    font_text = pygame.font.Font(f"{game.path}files/assets/fonts/CFGlitchCity-Regular.ttf", scale.y(200))

    # Making the texts
    round_text = font_text.render(f"ROUND {round}", True, fading_color)

    # Defining fonts positions on the screen
    start_text_pos = (scale.x(960) - round_text.get_width() // 2, (scale.y(540) - round_text.get_height() // 2))

    # Displaying the text
    game.screen.blit(round_text, start_text_pos)

    fading = True
    frames = 0

    fading_red_add = 2

    while fading:
        for event in pygame.event.get():
            if event.type == game.QUIT:
                running = False
                quit()

        fading_red = fading_red + fading_red_add
        fading_color = (fading_red, 0, 0)
        fps_scaling = scale.fps(1)
        frames = frames + fps_scaling

        if frames == 120:
            fading_red_add = 0
        if frames == 180:
            fading_red_add = -2

        if fading_red == 0:
            game.screen.fill(constants.black)
            fading = False

        round_text = font_text.render(f"ROUND {round}", True, fading_color)

        game.screen.blit(round_text, start_text_pos)

        game.update()
        game.main_clock.tick(game.fps)

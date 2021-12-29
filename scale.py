import game


def x(x):
    surface = game.pygame.display.get_surface()  # get the surface of the current active display
    x = (x * surface.get_width()) / 1920
    x = int(x)
    return x


def y(y):
    surface = game.pygame.display.get_surface()  # get the surface of the current active display
    y = (y * surface.get_height()) / 1080
    y = int(y)
    return y


def fps(scale_fps):
    scaled = (scale_fps * game.fps) / 60
    return scaled

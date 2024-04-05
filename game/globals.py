from enum import Enum
import pygame.image


class Dimensions:
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    CENTER_X = WINDOW_WIDTH/2
    CENTER_Y = WINDOW_HEIGHT/2


class Colours:
    PLAYER = (250, 120, 60)
    PAUSED_BG = (0, 0, 255)


class Textures:
    GROUND = pygame.image.load("res/ground.png")
    START_BUTTON_TEXTURE = pygame.image.load("res/start.png")
    GAME_BG = pygame.image.load("res/start_screen.png")
    MENU_BG = pygame.image.load("res/start_screen.png")
    NIGHT_BG = pygame.image.load("res/moon_stars.png")
    DAY_BG = pygame.image.load("res/sun_birds.png")


class MenuState(Enum):
    NONE = 0    # game is resumed basically
    MAIN_MENU = 1
    PAUSED = 2


class DayNight(Enum):
    DAY = 0
    NIGHT = 1

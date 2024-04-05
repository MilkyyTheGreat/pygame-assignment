import pygame
from game.globals import Dimensions, MenuState, Textures
from game.entities.player import Player
from game.objects.button import Button
from game.entity_groups import ALL_ENTITIES

# Initiation

pygame.init()

screen = pygame.display.set_mode(
    (Dimensions.WINDOW_WIDTH, Dimensions.WINDOW_HEIGHT))
pygame.display.set_caption("Jumping Block")
clock = pygame.time.Clock()

player = Player(Dimensions.CENTER_X, Dimensions.CENTER_Y)

start_button = Button(Dimensions.CENTER_X, Dimensions.CENTER_Y -
                      100, Textures.START_BUTTON_TEXTURE.convert_alpha())
resume_button = Button(Dimensions.CENTER_X, Dimensions.CENTER_Y,
                       Textures.START_BUTTON_TEXTURE.convert_alpha())

last_daylight_cycle = pygame.time.get_ticks()
is_night = False
# TODO: replace temp texture

# main loop
running = True
menustate = MenuState.MAIN_MENU

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            if menustate == MenuState.NONE:     # pause the game on ESC if nothing else open
                menustate = MenuState.PAUSED

    # draw screen and all entities
    screen.blit(Textures.GAME_BG, (0, 0))
    screen.blit(Textures.GROUND,
                (0, (Dimensions.WINDOW_HEIGHT / 2)))

    if pygame.time.get_ticks() - last_daylight_cycle >= 60_000:  # 1 minutes in milliseconds
        is_night = not is_night
        last_daylight_cycle = pygame.time.get_ticks()

    if is_night == True:
        screen.blit(Textures.NIGHT_BG, (0, 0))
    else:
        screen.blit(Textures.DAY_BG, (0, 0))

    if menustate == MenuState.NONE:             # update entities if no menus active
        player.show()
        player.update(pygame.key.get_pressed())
    elif menustate == MenuState.MAIN_MENU:      # main menu stuff
        player.hide()
        screen.blit(Textures.MENU_BG, (0, 0))
        start_button.draw(screen)

        if start_button.clicked == True:
            menustate = MenuState.NONE
    elif menustate == MenuState.PAUSED:
        player.hide()
        screen.blit(Textures.MENU_BG,
                    (Dimensions.WINDOW_WIDTH, Dimensions.WINDOW_HEIGHT))
        resume_button.draw(screen)

        if resume_button.clicked == True:
            menustate = MenuState.NONE

    # draw all entities
    for entity in ALL_ENTITIES:
        screen.blit(entity.surf, entity.rect)

    # game tick
    pygame.display.flip()
    clock.tick(60)
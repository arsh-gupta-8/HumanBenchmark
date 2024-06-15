import pygame
import math

pygame.init()

# Text
pygame.font.init()
title = pygame.font.SysFont('Raleway Bold', 45)   # For Cookie Amount Display
stat_display_font = pygame.font.SysFont('Comic Sans MS', 25)   # For Stat Display
multiplier_display_font = pygame.font.SysFont('Times New Roman', 25)   # For Multiplier Display

# Screen
screen = pygame.display.set_mode((1030, 500))
pygame.display.set_caption("Cookie Clicker")

# Loop Start
clock = pygame.time.Clock()
running = True
FPS = 30


def display_msg(string, str_type, colour, x, y):
    write_line = str_type.render(string, False, colour)
    line_width = write_line.get_width()
    screen.blit(write_line, (x - line_width//2, y))


while running:

    x, y = pygame.mouse.get_pos()
    if 75 <= x <= 325 and 90 <= y <= 340:
        enlarge = True
    else:
        enlarge = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    #     if event.type == pygame.MOUSEBUTTONUP:
    #
    #         if event.button == 1 and 75 <= x <= 325 and 90 <= y <= 340:
    #             cookies += 1
    #
    #         elif (event.button == 4 or event.button == 5) and 480 <= x <= 820:
    #             if event.button == 4 and shop_scroll < 0:
    #                 shop_scroll += 120
    #
    #             elif event.button == 5:
    #                 shop_scroll -= 120
    #
    #         elif event.button == 1 and 500 <= x <= 800 and y > 14:
    #             shop_keeper, cookies = shop_updater(shop_keeper, x, y, shop_scroll, cookies, multiplier)
    #
    #         elif event.button == 1 and 420 <= x <= 480 and 20 <= y <= 50:
    #             current_mult = multipliers.index(multiplier)
    #             if current_mult == 3:
    #                 current_mult = 0
    #             else:
    #                 current_mult += 1
    #             multiplier = multipliers[current_mult]

    screen.fill((43, 135, 209))
    display_msg("Human Benchmark", title, (255, 255, 255), 500, 10)
    pygame.display.update()
    clock.tick(FPS)



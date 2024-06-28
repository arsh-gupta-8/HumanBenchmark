import pygame

pygame.init()

# Text
pygame.font.init()
title = pygame.font.SysFont('Raleway Bold', 130)   # For Cookie Amount Display
stat_display_font = pygame.font.SysFont('Comic Sans MS', 25)   # For Stat Display
multiplier_display_font = pygame.font.SysFont('Times New Roman', 25)   # For Multiplier Display

# Screen
screen = pygame.display.set_mode((1003, 500))
pygame.display.set_caption("Human Benchmark")

# Images
Reaction = pygame.image.load("Games/ReactionTime.png")
Sequence = pygame.image.load("Games/SequenceMemory.png")
Aim = pygame.image.load("Games/AimTrainer.png")
Number = pygame.image.load("Games/NumberMemory.png")
Verbal = pygame.image.load("Games/VerbalMemory.png")
Chimp = pygame.image.load("Games/ChimpTest.png")
Visual = pygame.image.load("Games/VisualMemory.png")
Typing = pygame.image.load("Games/Typing.png")
GAME = [Reaction, Sequence, Aim, Number, Verbal, Chimp, Visual, Typing]

# Loop Start
clock = pygame.time.Clock()
running = True
FPS = 60

# Game settings
scroll = 0

def display_msg(string, str_type, colour, x, y):
    write_line = str_type.render(string, False, colour)
    line_width = write_line.get_width()
    screen.blit(write_line, (x - line_width//2, y))


while running:

    option = []
    for i in range(4):
        for j in range(2):
            rectangle = pygame.Rect(100 + (425 * j), 510 + (250 * i) + scroll, 375, 200)
            option.append(rectangle)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
    #
    #         if event.button == 1 and 75 <= x <= 325 and 90 <= y <= 340:
    #             cookies += 1
    #
            if (event.button == 4 or event.button == 5):
                if event.button == 4 and scroll < 0:
                    scroll += 65

                elif event.button == 5 and scroll > -1040:
                    scroll -= 65
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
    display_msg("Human Benchmark", title, (255, 255, 255), 500, scroll+170)
    pygame.draw.rect(screen, (230, 232, 244), pygame.Rect(0, scroll+410, 1003, 1200))
    for rect in option:
        if rect.collidepoint((x, y)):
            pygame.draw.rect(screen, (254,146,69), rect)
        else:
            pygame.draw.rect(screen, (149, 195, 232), rect)

    game_pic = 0
    for i in range(4):
        for j in range(2):
            screen.blit(GAME[game_pic], (105 + (425 * j), 515 + (250 * i) + scroll))
            game_pic += 1

    pygame.display.update()
    clock.tick(FPS)



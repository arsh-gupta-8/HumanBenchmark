import pygame
import random
import math

pygame.init()

# Text
pygame.font.init()
title = pygame.font.SysFont('Raleway Bold', 130)   # Big message
text = pygame.font.SysFont('Comic Sans MS', 25)   # Instruction
key_instr = pygame.font.SysFont('Times New Roman', 25)   # Further instructions

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
page = -1
active_timer = -1
hover = None
game_start = None
game_status = -1
reaction_time = -1
game_message = ''

def display_msg(string, str_type, colour, x, y):
    write_line = str_type.render(string, False, colour)
    line_width = write_line.get_width()
    screen.blit(write_line, (x - line_width//2, y))


while running:

    option = []

    if active_timer >= 0:
        active_timer += 1

    for i in range(4):
        for j in range(2):
            rectangle = pygame.Rect(100 + (425 * j), 510 + (250 * i) + scroll, 375, 200)
            option.append(rectangle)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and page != -1:
                game_start = True

                if game_status == 2:
                    game_start = False
                    game_status = -1

                else:
                    game_status = 0

            if event.key == pygame.K_ESCAPE:
                page = -1
                game_status = -1
                game_start = None
                reaction_time = -1
                active_timer = -1

        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
                if game_start:

                    if game_status == 0:
                        game_message = "Clicked too early"
                    elif game_status == 1:
                        game_message = str(math.floor((active_timer / FPS) * 1000)) + ' ms'
                    game_status = 2

                if hover != None:
                    page = hover
                    hover = None
                    game_start = False


            if (event.button == 4 or event.button == 5) and page == -1:
                if event.button == 4 and scroll < 0:
                    scroll += 65

                elif event.button == 5 and scroll > -1040:
                    scroll -= 65

    screen.fill((43, 135, 209))
    if page == -1:
        display_msg("Human Benchmark", title, (255, 255, 255), 500, scroll+170)
        pygame.draw.rect(screen, (230, 232, 244), pygame.Rect(0, scroll+410, 1003, 1200))
        for rect in range(8):
            if option[rect].collidepoint((x, y)):
                hover = rect
                pygame.draw.rect(screen, (254,146,69), option[rect])
            else:
                pygame.draw.rect(screen, (149, 195, 232), option[rect])

        game_pic = 0
        for i in range(4):
            for j in range(2):
                screen.blit(GAME[game_pic], (105 + (425 * j), 515 + (250 * i) + scroll))
                game_pic += 1

        if screen.get_at((x, y)) == (230, 232, 244):
            hover = None

    elif page == 0:

        if game_start:

            if game_status == 0:

                screen.fill((231, 13, 1))
                display_msg("Wait...", title, (255, 255, 255), 500, 200)

                if reaction_time < 0:
                    reaction_time = random.randint(60, 420)
                elif reaction_time == 0:
                    game_status = 1
                else:
                    reaction_time -= 1

            elif game_status == 1:

                screen.fill((62, 180, 137))
                display_msg("Click", title, (255, 255, 255), 500, 200)
                if active_timer < 0:
                    active_timer = 0
            else:
                display_msg(game_message, title, (255, 255, 255), 500, 200)
                display_msg("Press enter to continue", key_instr, (255, 255, 255), 500, 320)
                active_timer = -1
                reaction_time = -1
        else:
            display_msg("Reaction Time", title, (255, 255, 255), 500, 100)
            display_msg("Click when the screen turns green!", text, (255, 255, 255), 500, 220)
            display_msg("Press enter to start", key_instr, (255, 255, 255), 500, 320)
            display_msg("Press escape to go back", key_instr, (255, 255, 255), 500, 355)

    pygame.display.update()
    clock.tick(FPS)

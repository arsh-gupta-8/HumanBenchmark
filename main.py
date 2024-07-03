import pygame
import random
import math

pygame.init()

# Text
pygame.font.init()
title = pygame.font.SysFont('Raleway Bold', 130)   # Big message
text = pygame.font.SysFont('Comic Sans MS', 25)   # Instruction
key_instr = pygame.font.SysFont('Times New Roman', 25)   # Further instructions
back_text = pygame.font.SysFont('Comic Sans MS', 300)   # Background text
medium_text = pygame.font.SysFont('Comic Sans MS', 100)   # Big representation

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
score_keeper = -1
hover = None
game_start = None
game_status = -1
game_memory = -1
game_message = ''

# Sequence Memory Game exclusive settings
sequence_boxes = []
for i in range(3):
    for j in range(3):
        rectangle = pygame.Rect(320 + (125 * j), 110 + (125 * i), 110, 110)
        sequence_boxes.append(rectangle)

def display_msg(string, str_type, colour, x, y):
    write_line = str_type.render(string, False, colour)
    line_width = write_line.get_width()
    screen.blit(write_line, (x - line_width//2, y))


while running:

    option = []

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and page != -1:
                game_start = True

                if page == 3 and game_status == 1:
                    game_status = 0
                    score_keeper[4] = 1

                if game_status == 2:
                    game_start = False
                    game_status = -1

                else:
                    game_status = 0

            elif event.key == pygame.K_ESCAPE:
                page = -1
                game_status = -1
                game_start = None
                game_memory = -1
                score_keeper = -1

            elif page == 3 and game_status == 1:
                if event.key == pygame.K_1:
                    score_keeper[3] += "1"
                elif event.key == pygame.K_2:
                    score_keeper[3] += "2"
                elif event.key == pygame.K_3:
                    score_keeper[3] += "3"
                elif event.key == pygame.K_4:
                    score_keeper[3] += "4"
                elif event.key == pygame.K_5:
                    score_keeper[3] += "5"
                elif event.key == pygame.K_6:
                    score_keeper[3] += "6"
                elif event.key == pygame.K_7:
                    score_keeper[3] += "7"
                elif event.key == pygame.K_8:
                    score_keeper[3] += "8"
                elif event.key == pygame.K_9:
                    score_keeper[3] += "9"
                elif event.key == pygame.K_0:
                    score_keeper[3] += "0"
                elif event.key == pygame.K_BACKSPACE and len(score_keeper[3]) > 0:
                    score_keeper[3] = score_keeper[3][:-1]

        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
                if game_start:

                    if page == 0:
                        if game_status == 0:
                            game_message = "Clicked too early"
                        elif game_status == 1:
                            game_message = str(math.floor((score_keeper / FPS) * 1000)) + ' ms'
                        game_status = 2

                    elif page == 1:
                        if game_status == 1:

                            if score_keeper[3] != None:
                                score_keeper[4] += 1

                                if score_keeper[3] == game_memory[score_keeper[4]]:
                                    if score_keeper[4] + 1 == len(game_memory):
                                        score_keeper[0] = 0
                                        game_status = 0
                                        score_keeper[1] = 0
                                    else:
                                        score_keeper[2] = -2

                                else:
                                    game_message = "Level " + str(len(game_memory))
                                    score_keeper[2] = 0
                                    game_status = 2

                    elif page == 2:
                        if game_status == 1:
                            score_keeper[2] = 1

                elif hover != None:
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

        pygame.draw.rect(screen, (254,146,69), pygame.Rect(997, 0, 6, (scroll / 1040) * -500))

        for i in range(4):
            for j in range(2):
                rectangle = pygame.Rect(100 + (425 * j), 510 + (250 * i) + scroll, 375, 200)
                option.append(rectangle)

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

                if game_memory < 0:
                    game_memory = random.randint(60, 420)
                elif game_memory == 0:
                    game_status = 1
                else:
                    game_memory -= 1

            elif game_status == 1:

                screen.fill((62, 180, 137))
                display_msg("Click", title, (255, 255, 255), 500, 200)
                if score_keeper < 0:
                    score_keeper = 0
                else:
                    score_keeper += 1
            else:
                display_msg(game_message, title, (255, 255, 255), 500, 200)
                display_msg("Press enter to continue", key_instr, (255, 255, 255), 500, 320)
                score_keeper = -1
                game_memory = -1
        else:
            display_msg("Reaction Time", title, (255, 255, 255), 500, 100)
            display_msg("Click when the screen turns green!", text, (255, 255, 255), 500, 220)
            display_msg("Press enter to start", key_instr, (255, 255, 255), 500, 320)
            display_msg("Press escape to go back", key_instr, (255, 255, 255), 500, 355)

    elif page == 1:

        if game_start:
        
            if game_status == 0:

                if score_keeper[0] == 0:
                    new_square = random.randint(0, 8)
                    if len(game_memory) > 0:
                        while new_square == game_memory[-1]:
                            new_square = random.randint(0, 8)
                    game_memory.append(new_square)
                    score_keeper[0] = 1

                display_msg("Level " + str(len(game_memory)), text, (255, 255, 255), 500, 50)

                if score_keeper[2] == -1:
                    score_keeper[2] = 1
                elif score_keeper[2] % 40 == 0:
                    score_keeper[1] += 1
                    score_keeper[2] += 1
                else:
                    score_keeper[2] += 1

                if score_keeper[1] == len(game_memory):
                    score_keeper[4] = -1
                    game_status = 1
                    continue

                for rect in range(9):
                    if rect == game_memory[score_keeper[1]]:
                        pygame.draw.rect(screen, (230, 232, 244), sequence_boxes[rect])
                    else:
                        pygame.draw.rect(screen, (34,108,180), sequence_boxes[rect])

            elif game_status == 1:

                if score_keeper[2] >= 8:
                    screen.fill((43, 135, 209))
                elif score_keeper[2] == -2:
                    score_keeper[2] += 1
                else:
                    screen.fill((62, 180, 137))
                    score_keeper[2] += 1

                display_msg("Level " + str(len(game_memory)), text, (255, 255, 255), 500, 50)

                for square in range(9):
                    if sequence_boxes[square].collidepoint((x, y)):
                        score_keeper[3] = square
                        pygame.draw.rect(screen, (34,108,180), sequence_boxes[square])
                    else:
                        pygame.draw.rect(screen, (37,115,193), sequence_boxes[square])

                if screen.get_at((x, y)) == (43, 135, 209):
                    score_keeper[3] = None

            else:
                score_keeper[2] += 1
                if score_keeper[2] < 50:
                    screen.fill((231, 13, 1))

                display_msg(game_message, title, (255, 255, 255), 500, 200)
                display_msg("Press enter to continue", key_instr, (255, 255, 255), 500, 320)

        else:
            game_memory = []
            score_keeper = [0, 0, -1, 0, -1]
            display_msg("Sequence Memory", title, (255, 255, 255), 500, 100)
            display_msg("Memorise the increasing pattern!", text, (255, 255, 255), 500, 220)
            display_msg("Press enter to start", key_instr, (255, 255, 255), 500, 320)
            display_msg("Press escape to go back", key_instr, (255, 255, 255), 500, 355)

    elif page == 2:

        if game_start:

            if game_status == 0:

                score_keeper[1] += 1

                display_msg(str(3 - (score_keeper[1]//60)), back_text, (255, 255, 255), 500, 50)

                if score_keeper[1] == 180:
                    score_keeper[1] = 0
                    game_status = 1

            elif game_status == 1:

                display_msg(str(30 - game_memory), back_text, (149, 195, 232), 500, 50)
                score_keeper[1] += 1

                if score_keeper[0]:
                    target_x = random.randint(41, 959)
                    target_y = random.randint(26, 474)
                    score_keeper[0] = 0

                pygame.draw.circle(screen, (149, 195, 232), (target_x, target_y), 42)
                for i in range(1, 4):
                    pygame.draw.circle(screen, (255, 255, 255), (target_x, target_y), i * 14, 2 + i)

                if score_keeper[2]:
                    score_keeper[2] = 0
                    x_dif = (x - target_x) ** 2
                    y_dif = (y - target_y) ** 2
                    total_dif = math.sqrt(x_dif + y_dif)
                    if total_dif < 42:
                        game_memory += 1
                        score_keeper[0] = 1

                if game_memory == 30:
                    game_message = str(math.floor((score_keeper[1] * 100)/(FPS * 3))) + " ms"
                    game_status = 2

            else:
                display_msg(game_message, title, (255, 255, 255), 500, 200)
                display_msg("Press enter to continue", key_instr, (255, 255, 255), 500, 320)

        else:
            game_memory = 0
            score_keeper = [1, 0, 0]
            display_msg("Aim Trainer", title, (255, 255, 255), 500, 100)
            display_msg("Hit 30 targets as quickly as you can!", text, (255, 255, 255), 500, 220)
            display_msg("Press enter to start", key_instr, (255, 255, 255), 500, 320)
            display_msg("Press escape to go back", key_instr, (255, 255, 255), 500, 355)

    elif page == 3:

        if game_start:

            if game_status == 0:
                if score_keeper[4]:
                    print(len(score_keeper[3]) > 0 and game_memory == int(score_keeper[3]))
                    if len(score_keeper[3]) > 0 and game_memory == int(score_keeper[3]):
                        score_keeper[1] = 1
                        score_keeper[2] = 0
                        score_keeper[3] = ""
                        score_keeper[4] = 0
                    else:
                        game_status = 2
                        game_message = str(len(str(game_memory)) - 1) + " digits"
                else:

                    if score_keeper[1]:
                        score_keeper[1] = 0
                        score_keeper[0] += 1
                        min = int("1" + "0" * (score_keeper[0] - 1))
                        max = int("1" + "0" * score_keeper[0]) - 1
                        game_memory = random.randint(min, max)
                        time = 60 + score_keeper[0] * 30

                    score_keeper[2] += 1

                    display_msg(str(game_memory), medium_text, (255, 255, 255), 500, 150)
                    bar_length = math.floor(300 * (1 - (score_keeper[2] / time)))
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(350, 280, bar_length, 8))

                    if score_keeper[2] == time:
                        game_status = 1

            elif game_status == 1:
                display_msg("Type in the number", key_instr, (255, 255, 255), 500, 140)
                display_msg(score_keeper[3], medium_text, (255, 255, 255), 500, 150)

            else:
                display_msg(game_message, title, (255, 255, 255), 500, 200)
                display_msg("Press enter to continue", key_instr, (255, 255, 255), 500, 320)

        else:
            game_memory = 0
            score_keeper = [0, 1, -1, "", 0]
            display_msg("Number Memory", title, (255, 255, 255), 500, 100)
            display_msg("How many digits can you remember?", text, (255, 255, 255), 500, 220)
            display_msg("Press enter to start", key_instr, (255, 255, 255), 500, 320)
            display_msg("Press escape to go back", key_instr, (255, 255, 255), 500, 355)

    pygame.display.update()
    clock.tick(FPS)

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
words_rep = pygame.font.SysFont('Comic Sans MS', 75)   # Word show
box_num = pygame.font.SysFont('Raleway Bold', 60)   # Number in box

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
words_list = [
    "wanderlust", "enthusiasm", "sophisticated", "capricious", "equilibrium",
    "constellation", "megalopolis", "circumstance", "melancholy", "ambidextrous",
    "sophomore", "melodramatic", "catastrophe", "kaleidoscope", "hippopotamus",
    "serendipity", "phenomenon", "chronological", "photographic", "vegetarian",
    "appreciation", "magnificent", "metamorphosis", "photorealistic",
    "heterogeneous", "bibliophile", "gastronomy", "cryptocurrency",
    "sustainability", "meticulous", "pharmaceutical", "introspection",
    "megalithic", "philanthropic", "nostalgia", "constellation", "innovative",
    "compassionate", "meticulously", "photojournalist", "heterogeneity",
    "bibliomania", "gastronomic", "decentralized", "phenomenally",
    "introspectively", "megalith", "philanthropist", "photorealism",
    "heterocyclic", "bibliographer", "gourmet", "cryptographically",
    "phenomenality", "introverted", "megaliths", "philanthropy", "photosynthesis",
    "heterocyclics", "bibliography", "gastronomer", "cryptographer",
    "phenomenalize", "introversion", "megalithicly", "philanthropies",
    "photosynthetic", "heterocyclically", "bibliophilic", "epicurean",
    "cryptographic", "phenomenalizes", "introductory", "megalithicism",
    "philanthropically", "photosynthesized", "heterocyclicness",
    "bibliophobia", "gastronomically", "cryptographers", "phenomenalizing",
    "introspectiveness", "megalithicize", "philanthropization",
    "photosynthesizing", "heterocyclically", "bibliophileism",
    "gastronomies", "cryptographically", "phenomenalizations",
    "introspectivist", "megalithicization", "philanthropizations",
    "photosynthetically", "heterocyclicness", "bibliophobic",
    "gastronomist", "cryptographers", "phenomenalize",
    "introspectivity", "megalithicize",
]

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

                elif page == 5 and game_status == 1:
                    game_status = 0

                elif game_status == 2:
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

                    elif page == 4:
                        if game_status == 0:
                            if score_keeper[3]:
                                if score_keeper[2] in score_keeper[1]:
                                    game_memory -= 1
                                else:
                                    score_keeper[5] += 1
                            elif score_keeper[3] == 0:
                                if score_keeper[2] not in score_keeper[1]:
                                    game_memory -= 1
                                else:
                                    score_keeper[5] += 1

                            score_keeper[1].append(score_keeper[2])
                            score_keeper[0] = 1

                    elif page == 5:
                        if game_status == 0:
                            if score_keeper[3] is not None:
                                if score_keeper[3] == 0:
                                    cords_list.pop(0)
                                else:
                                    game_memory -= 1
                                    if game_memory != 0:
                                        game_status = 1
                                        score_keeper[0] = 1

                    elif page == 6:
                        if game_status == 1:
                            score_keeper[6].append(hover)
                            if hover in square_pos:
                                temp_pos.remove(hover)
                            else:
                                score_keeper[7] += 1

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

    elif page == 4:

        if game_start:

            if game_status == 0:
                if game_memory > 0:
                    if score_keeper[0]:
                        score_keeper[0] = 0
                        if len(score_keeper[1]) > 3 and random.randint(1, 4) == 1:
                            score_keeper[2] = random.choice(score_keeper[1])
                        else:
                            score_keeper[2] = random.choice(words_list)
                    else:
                        display_msg("lives: " + str(game_memory), key_instr, (255, 255, 255), 500, 130)
                        display_msg(score_keeper[2], words_rep, (255, 255, 255), 500, 170)
                        buttons = []
                        for i in range(2):
                            buttons.append(pygame.Rect(350 + i * 200, 310, 100, 40))

                        for button in range(2):
                            if buttons[button].collidepoint((x, y)):
                                pygame.draw.rect(screen, (239,195,72), buttons[button])
                                score_keeper[3] = button
                            else:
                                pygame.draw.rect(screen, (255,209,84), buttons[button])

                        display_msg("SEEN", key_instr, (0, 0, 0), 400, 316)
                        display_msg("NEW", key_instr, (0, 0, 0), 601, 316)

                        if screen.get_at((x, y)) == (43, 135, 209):
                            score_keeper[3] = None

                else:
                    game_message = str(score_keeper[5]) + " words"
                    game_status = 2

            else:
                display_msg(game_message, title, (255, 255, 255), 500, 200)
                display_msg("Press enter to continue", key_instr, (255, 255, 255), 500, 320)

        else:
            game_memory = 3
            score_keeper = [1, [], "", None, -1, 0]
            display_msg("Verbal Memory", title, (255, 255, 255), 500, 100)
            display_msg("Have you already seen this word or not?", text, (255, 255, 255), 500, 220)
            display_msg("Press enter to start", key_instr, (255, 255, 255), 500, 320)
            display_msg("Press escape to go back", key_instr, (255, 255, 255), 500, 355)

    elif page == 5:

        if game_start:

            if game_status == 0:
                if game_memory > 0:
                    if score_keeper[0]:
                        cords_list = []
                        score_keeper[0] = 0
                        repeat = True
                        while repeat:
                            x_cord = random.randint(0, 7)
                            y_cord = random.randint(0, 4)
                            if [x_cord, y_cord] not in cords_list:
                                cords_list.append([x_cord, y_cord])
                                if len(cords_list) == score_keeper[1]:
                                    repeat = False

                    else:
                        if len(cords_list) == score_keeper[1]:
                            score_keeper[2] = 1
                        else:
                            score_keeper[2] = 0

                        cords_xy = []
                        rects = []

                        for i in range(len(cords_list)):
                            x_pos = 145 + 90 * cords_list[i][0]
                            y_pos = 20 + 90 * cords_list[i][1]
                            cords_xy.append([x_pos, y_pos])

                        for i in range(len(cords_list)):
                            rects.append(pygame.Rect(cords_xy[i][0], cords_xy[i][1], 80, 80))

                        for draw in range(len(rects)):
                            if score_keeper[2]:
                                pygame.draw.rect(screen, (42, 134, 208), rects[draw], border_radius=8)
                                display_msg(str(draw + 1), box_num, (255, 255, 255), cords_xy[draw][0] + 40, cords_xy[draw][1] + 20)
                                if rects[draw].collidepoint((x, y)):
                                    pygame.draw.rect(screen, (149,195,232), rects[draw], 6, 8)
                                    score_keeper[3] = draw
                                else:
                                    pygame.draw.rect(screen, (65, 147, 214), rects[draw], 6, 8)

                            else:
                                if rects[draw].collidepoint((x, y)):
                                    pygame.draw.rect(screen, (245,245,245), rects[draw], border_radius = 8)
                                    score_keeper[3] = draw
                                else:
                                    pygame.draw.rect(screen, (255, 255, 255), rects[draw], border_radius= 8)

                        if screen.get_at((x, y)) == (43, 135, 209):
                            score_keeper[3] = None

                    if len(cords_list) == 0:
                        score_keeper[1] += 1
                        score_keeper[0] = 1

                else:
                    game_message = str(score_keeper[1]) + " numbers"
                    game_status = 2

            elif game_status == 1:
                display_msg(f"{game_memory} lives left", words_rep, (255, 255, 255), 500, 160)
                display_msg("Press enter to continue", key_instr, (255, 255, 255), 500, 320)

            else:
                display_msg(game_message, title, (255, 255, 255), 500, 200)
                display_msg("Press enter to continue", key_instr, (255, 255, 255), 500, 320)

        else:
            game_memory = 3
            score_keeper = [1, 4, 1, None]
            display_msg("Chimp Test", title, (255, 255, 255), 500, 100)
            display_msg("Remember the order of the squares", text, (255, 255, 255), 500, 220)
            display_msg("Press enter to start", key_instr, (255, 255, 255), 500, 320)
            display_msg("Press escape to go back", key_instr, (255, 255, 255), 500, 355)

    elif page == 6:

        if game_start:

            if game_status == 0:
                if game_memory > 0:

                    if score_keeper[2]:
                        score_keeper[0] += 1
                        score_keeper[1] += 1
                        if score_keeper[1] == 3:
                            score_keeper[1] = 0
                            score_keeper[3] += 1
                        squares = score_keeper[0] + 2
                        score_keeper[2] = 0


                    if score_keeper[5]:
                        square_pos = []
                        while len(square_pos) != squares:
                            new_num = random.randint(0, score_keeper[3]**2 - 1)
                            if new_num not in square_pos:
                                square_pos.append(new_num)
                        temp_pos = square_pos.copy()
                        score_keeper[5] = 0
                        cord_inter = (440 - score_keeper[3]*10) // score_keeper[3]

                    else:
                        g6_sp = []
                        for i in range(score_keeper[3]):
                            for j in range(score_keeper[3]):
                                g6_sp.append(pygame.Rect(275 + j * (cord_inter + 10), 60 + i * (cord_inter + 10), cord_inter, cord_inter))

                        for i in range(len(g6_sp)):

                            if i in square_pos:
                                pygame.draw.rect(screen, (255, 255, 255), g6_sp[i])
                            else:
                                pygame.draw.rect(screen, (37,115,193), g6_sp[i])

                        display_msg(f"Level {score_keeper[0]}", box_num, (255, 255, 255), 345, 10)
                        display_msg(f"Lives: {game_memory}", box_num, (255, 255, 255), 620, 10)

                    score_keeper[4] += 1
                    if score_keeper[4] == 90:
                        game_status = 1
                        score_keeper[4] = 0
                        score_keeper[5] = 1
                        score_keeper[6] = []
                        score_keeper[7] = 0

                else:
                    game_message = "Level " + str(score_keeper[0])
                    game_status = 2

            elif game_status == 1:
                g6_sp = []
                for i in range(score_keeper[3]):
                    for j in range(score_keeper[3]):
                        g6_sp.append(
                            pygame.Rect(275 + j * (cord_inter + 10), 60 + i * (cord_inter + 10), cord_inter, cord_inter))

                for i in range(len(g6_sp)):
                    if i in square_pos:
                        pygame.draw.rect(screen, (255, 255, 255), g6_sp[i])
                    else:
                        pygame.draw.rect(screen, (21,67,104), g6_sp[i])

                for i in range(len(g6_sp)):
                    if i in score_keeper[6]:
                        continue
                    elif g6_sp[i].collidepoint((x, y)):
                        pygame.draw.rect(screen, (47,125,203), g6_sp[i])
                        hover = i
                    else:
                        pygame.draw.rect(screen, (37, 115, 193), g6_sp[i])

                display_msg(f"Level {score_keeper[0]}", box_num, (255, 255, 255), 345, 10)
                display_msg(f"Lives: {game_memory}", box_num, (255, 255, 255), 620, 10)

                if screen.get_at((x, y)) == (43,135,209):
                    hover = None

                if len(temp_pos) == 0:
                    score_keeper[2] = 1
                    game_status = 0

                if score_keeper[7] == 3:
                    game_status = 0
                    game_memory -= 1

            else:
                display_msg(game_message, title, (255, 255, 255), 500, 200)
                display_msg("Press enter to continue", key_instr, (255, 255, 255), 500, 320)

        else:
            game_memory = 3
            score_keeper = [0, 1, 1, 3, 0, 1, [], 0]
            # level - continuous - new level - square output - timer - square positions - clicked
            display_msg("Visual Memory", title, (255, 255, 255), 500, 100)
            display_msg("Remember which squares were white", text, (255, 255, 255), 500, 220)
            display_msg("Press enter to start", key_instr, (255, 255, 255), 500, 320)
            display_msg("Press escape to go back", key_instr, (255, 255, 255), 500, 355)

    pygame.display.update()
    clock.tick(FPS)

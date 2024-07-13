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
typing_game = pygame.font.SysFont('Arial', 20)   # Typing game text

#Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_BLUE = (43, 135, 209)


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
type_text = ["Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then everything changed "
    , "when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them. But "
    , "when the world needed him most, he vanished. A hundred years passed and my brother and I "
    , "discovered the new Avatar, an airbender named Aang, and although his airbending skills are great, he "
    , "still has a lot to learn before he's ready to save anyone. But I believe Aang can save the world."]
LETTERS = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g
           , pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n
           , pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u
           , pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_SPACE
           , pygame.K_PERIOD, pygame.K_COMMA, pygame.K_BACKSPACE, pygame.K_QUOTE]

# Sequence Memory Game exclusive settings
sequence_boxes = []
for i in range(3):
    for j in range(3):
        rectangle = pygame.Rect(320 + (125 * j), 110 + (125 * i), 110, 110)
        sequence_boxes.append(rectangle)

def display_msg(string, str_type, colour, x, y, start=0):
    write_line = str_type.render(string, False, colour)
    line_width = write_line.get_width()
    if start == 0:
        start = x - line_width//2
    screen.blit(write_line, (start, y))


while running:

    option = []

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
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

            elif page == 7:
                for letter in range(len(LETTERS)):
                    if event.key == LETTERS[letter]:
                        if letter < 26:
                            if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                                game_memory += chr(letter + 65)
                            else:
                                game_memory += chr(letter + 97)

                        elif letter == 26:
                            game_memory += " "

                        elif letter == 27:
                            game_memory += "."

                        elif letter == 28:
                            game_memory += ","

                        elif letter == 29:
                             if len(game_memory) > 0:
                                 game_memory = game_memory[:-1]

                        else:
                            game_memory += "'"

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

    screen.fill(BG_BLUE)
    if page == -1:
        display_msg("Human Benchmark", title, WHITE, 500, scroll+170)
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
                display_msg("Wait...", title, WHITE, 500, 200)

                if game_memory < 0:
                    game_memory = random.randint(60, 420)
                elif game_memory == 0:
                    game_status = 1
                else:
                    game_memory -= 1

            elif game_status == 1:

                screen.fill((62, 180, 137))
                display_msg("Click", title, WHITE, 500, 200)
                if score_keeper < 0:
                    score_keeper = 0
                else:
                    score_keeper += 1
            else:
                display_msg(game_message, title, WHITE, 500, 200)
                display_msg("Press enter to continue", key_instr, WHITE, 500, 320)
                score_keeper = -1
                game_memory = -1
        else:
            display_msg("Reaction Time", title, WHITE, 500, 100)
            display_msg("Click when the screen turns green!", text, WHITE, 500, 220)
            display_msg("Press enter to start", key_instr, WHITE, 500, 320)
            display_msg("Press escape to go back", key_instr, WHITE, 500, 355)

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

                display_msg("Level " + str(len(game_memory)), text, WHITE, 500, 50)

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
                        pygame.draw.rect(screen, (34, 108, 180), sequence_boxes[rect])

            elif game_status == 1:

                if score_keeper[2] >= 8:
                    screen.fill(BG_BLUE)
                elif score_keeper[2] == -2:
                    score_keeper[2] += 1
                else:
                    screen.fill((62, 180, 137))
                    score_keeper[2] += 1

                display_msg("Level " + str(len(game_memory)), text, WHITE, 500, 50)

                for square in range(9):
                    if sequence_boxes[square].collidepoint((x, y)):
                        score_keeper[3] = square
                        pygame.draw.rect(screen, (34, 108, 180), sequence_boxes[square])
                    else:
                        pygame.draw.rect(screen, (37, 115, 193), sequence_boxes[square])

                if screen.get_at((x, y)) == BG_BLUE:
                    score_keeper[3] = None

            else:
                score_keeper[2] += 1
                if score_keeper[2] < 50:
                    screen.fill((231, 13, 1))

                display_msg(game_message, title, WHITE, 500, 200)
                display_msg("Press enter to continue", key_instr, WHITE, 500, 320)

        else:
            game_memory = []
            score_keeper = [0, 0, -1, 0, -1]
            display_msg("Sequence Memory", title, WHITE, 500, 100)
            display_msg("Memorise the increasing pattern!", text, WHITE, 500, 220)
            display_msg("Press enter to start", key_instr, WHITE, 500, 320)
            display_msg("Press escape to go back", key_instr, WHITE, 500, 355)

    elif page == 2:

        if game_start:

            if game_status == 0:

                score_keeper[1] += 1

                display_msg(str(3 - (score_keeper[1]//60)), back_text, WHITE, 500, 50)

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
                    pygame.draw.circle(screen, WHITE, (target_x, target_y), i * 14, 2 + i)

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
                display_msg(game_message, title, WHITE, 500, 200)
                display_msg("Press enter to continue", key_instr, WHITE, 500, 320)

        else:
            game_memory = 0
            score_keeper = [1, 0, 0]
            display_msg("Aim Trainer", title, WHITE, 500, 100)
            display_msg("Hit 30 targets as quickly as you can!", text, WHITE, 500, 220)
            display_msg("Press enter to start", key_instr, WHITE, 500, 320)
            display_msg("Press escape to go back", key_instr, WHITE, 500, 355)

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

                    display_msg(str(game_memory), medium_text, WHITE, 500, 150)
                    bar_length = math.floor(300 * (1 - (score_keeper[2] / time)))
                    pygame.draw.rect(screen, WHITE, pygame.Rect(350, 280, bar_length, 8))

                    if score_keeper[2] == time:
                        game_status = 1

            elif game_status == 1:
                display_msg("Type in the number", key_instr, WHITE, 500, 140)
                display_msg(score_keeper[3], medium_text, WHITE, 500, 150)

            else:
                display_msg(game_message, title, WHITE, 500, 200)
                display_msg("Press enter to continue", key_instr, WHITE, 500, 320)

        else:
            game_memory = 0
            score_keeper = [0, 1, -1, "", 0]
            display_msg("Number Memory", title, WHITE, 500, 100)
            display_msg("How many digits can you remember?", text, WHITE, 500, 220)
            display_msg("Press enter to start", key_instr, WHITE, 500, 320)
            display_msg("Press escape to go back", key_instr, WHITE, 500, 355)

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
                        display_msg("lives: " + str(game_memory), key_instr, WHITE, 500, 130)
                        display_msg(score_keeper[2], words_rep, WHITE, 500, 170)
                        buttons = []
                        for i in range(2):
                            buttons.append(pygame.Rect(350 + i * 200, 310, 100, 40))

                        for button in range(2):
                            if buttons[button].collidepoint((x, y)):
                                pygame.draw.rect(screen, (239, 195, 72), buttons[button])
                                score_keeper[3] = button
                            else:
                                pygame.draw.rect(screen, (255, 209, 84), buttons[button])

                        display_msg("SEEN", key_instr, BLACK, 400, 316)
                        display_msg("NEW", key_instr, BLACK, 601, 316)

                        if screen.get_at((x, y)) == BG_BLUE:
                            score_keeper[3] = None

                else:
                    game_message = str(score_keeper[5]) + " words"
                    game_status = 2

            else:
                display_msg(game_message, title, WHITE, 500, 200)
                display_msg("Press enter to continue", key_instr, WHITE, 500, 320)

        else:
            game_memory = 3
            score_keeper = [1, [], "", None, -1, 0]
            display_msg("Verbal Memory", title, WHITE, 500, 100)
            display_msg("Have you already seen this word or not?", text, WHITE, 500, 220)
            display_msg("Press enter to start", key_instr, WHITE, 500, 320)
            display_msg("Press escape to go back", key_instr, WHITE, 500, 355)

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
                                display_msg(str(draw + 1), box_num, WHITE, cords_xy[draw][0] + 40, cords_xy[draw][1] + 20)
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
                                    pygame.draw.rect(screen, WHITE, rects[draw], border_radius= 8)

                        if screen.get_at((x, y)) == BG_BLUE:
                            score_keeper[3] = None

                    if len(cords_list) == 0:
                        score_keeper[1] += 1
                        score_keeper[0] = 1

                else:
                    game_message = str(score_keeper[1]) + " numbers"
                    game_status = 2

            elif game_status == 1:
                display_msg(f"{game_memory} lives left", words_rep, WHITE, 500, 160)
                display_msg("Press enter to continue", key_instr, WHITE, 500, 320)

            else:
                display_msg(game_message, title, WHITE, 500, 200)
                display_msg("Press enter to continue", key_instr, WHITE, 500, 320)

        else:
            game_memory = 3
            score_keeper = [1, 4, 1, None]
            display_msg("Chimp Test", title, WHITE, 500, 100)
            display_msg("Remember the order of the squares", text, WHITE, 500, 220)
            display_msg("Press enter to start", key_instr, WHITE, 500, 320)
            display_msg("Press escape to go back", key_instr, WHITE, 500, 355)

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
                                pygame.draw.rect(screen, WHITE, g6_sp[i])
                            else:
                                pygame.draw.rect(screen, (37,115,193), g6_sp[i])

                        display_msg(f"Level {score_keeper[0]}", box_num, WHITE, 345, 10)
                        display_msg(f"Lives: {game_memory}", box_num, WHITE, 620, 10)

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
                        pygame.draw.rect(screen, WHITE, g6_sp[i])
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

                display_msg(f"Level {score_keeper[0]}", box_num, WHITE, 345, 10)
                display_msg(f"Lives: {game_memory}", box_num, WHITE, 620, 10)

                if screen.get_at((x, y)) == (43,135,209):
                    hover = None

                if len(temp_pos) == 0:
                    score_keeper[2] = 1
                    game_status = 0

                if score_keeper[7] == 3:
                    game_status = 0
                    game_memory -= 1

            else:
                display_msg(game_message, title, WHITE, 500, 200)
                display_msg("Press enter to continue", key_instr, WHITE, 500, 320)

        else:
            game_memory = 3
            score_keeper = [0, 1, 1, 3, 0, 1, [], 0]
            # level - continuous - new level - square output - timer - square positions - clicked
            display_msg("Visual Memory", title, WHITE, 500, 100)
            display_msg("Remember which squares were white", text, WHITE, 500, 220)
            display_msg("Press enter to start", key_instr, WHITE, 500, 320)
            display_msg("Press escape to go back", key_instr, WHITE, 500, 355)

    elif page == 7:

        if game_start:

            if game_status == 0:

                if score_keeper[0]:
                    display_msg("Typing", words_rep, (213, 231, 246), 500, 20)
                    display_msg("Type to Start", key_instr, (213, 231, 246), 500, 400)

                else:
                    score_keeper[1] += 1
                    print(score_keeper[2], score_keeper[1])
                    display_msg(str(round((FPS * score_keeper[2] * 86 * 60) / (488 * score_keeper[1]))), words_rep, (213, 231, 246), 500, 20)
                    display_msg(str(math.floor(score_keeper[1]/FPS)), key_instr, (213, 231, 246), 500, 400)
                    score_keeper[2] = 0

                line_state = [["", 45, 180], ["", 70, 208], ["", 85, 236], ["", 48, 264], ["", 85, 292]]

                pygame.draw.rect(screen, WHITE, pygame.Rect(0, 160, 1005, 175))
                display_msg(type_text[0], typing_game, (33, 33, 33), 0, 180, 45)
                display_msg(type_text[1], typing_game, (33, 33, 33), 500, 208, 70)
                display_msg(type_text[2], typing_game, (33, 33, 33), 500, 236, 85)
                display_msg(type_text[3], typing_game, (33, 33, 33), 500, 264, 48)
                display_msg(type_text[4], typing_game, (33, 33, 33), 500, 292, 85)

                if len(game_memory) > 0:
                    score_keeper[0] = 0

                    for i in range(5):
                        pygame.draw.rect(screen, WHITE, pygame.Rect(line_state[i][1], line_state[i][2], score_keeper[3][i], 30))

                    for i in range(len(game_memory)):

                        if i < 103:
                            index = i
                            edit = 0

                        elif i < 201:
                            index = i - 103
                            edit = 1

                        elif i < 290:
                            index = i - 201
                            edit = 2

                        elif i < 391:
                            index = i - 290
                            edit = 3

                        elif i < 487:
                            index = i - 391
                            edit = 4

                        else:
                            game_status = 2
                            game_message = str(round((FPS * score_keeper[2] * 86 * 60) / (488 * score_keeper[1])))

                        score_keeper[3][edit] = typing_game.render(line_state[edit][0], False, (231, 13, 1)).get_width()

                        if game_memory[i] == type_text[edit][index]:
                            score_keeper[2] += 1
                            display_msg(type_text[edit][index], typing_game, (94, 196, 111), 500, line_state[edit][2], line_state[edit][1] + score_keeper[3][edit])
                        else:
                            display_msg(type_text[edit][index], typing_game, (231, 13, 1), 500, line_state[edit][2], line_state[edit][1] + score_keeper[3][edit])

                        line_state[edit][0] += type_text[edit][index]



            else:
                display_msg(game_message + ' WPM', title, WHITE, 500, 200)
                display_msg("Press enter to continue", key_instr, WHITE, 500, 320)

        else:
            game_memory = ""
            score_keeper = [1, 0, 0, [0, 0, 0, 0, 0]]
            display_msg("Typing", title, WHITE, 500, 100)
            display_msg("How fast can you type?", text, WHITE, 500, 220)
            display_msg("Press enter to start", key_instr, WHITE, 500, 320)
            display_msg("Press escape to go back", key_instr, WHITE, 500, 355)

    pygame.display.update()
    clock.tick(FPS)

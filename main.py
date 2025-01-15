from sys import exit
import pygame


# Initialize Pygame

WIDTH, HEIGHT = 900, 700
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Graph parameters
grid_spacing = 20  # Spacing between grid lines
origin = (0, 700)  # Center of the screen

# Line equation parameters
m = 0.5  # Slope
b = 0   # y-intercept (in graph units)

# Convert graph units to screen pixels


def graph_to_screen(x, y):
    screen_x = origin[0] + x * grid_spacing
    screen_y = origin[1] - y * grid_spacing  # Invert y-axis
    return screen_x, screen_y

# Function to calculate line points


def calculate_line_points(m, b, width, spacing):
    # Graph x-range: Convert screen width to graph units
    x_min = -width // (2 * spacing)
    x_max = width // (2 * spacing)

    # Calculate y values for the line endpoints
    y1 = m * x_min + b
    y2 = m * x_max + b

    # Convert graph coordinates to screen coordinates
    p1 = graph_to_screen(x_min, y1)
    p2 = graph_to_screen(x_max, y2)
    return p1, p2


# def index_of(val, in_list):
#     try:
#         return in_list.index(val)
#     except ValueError:
#         return -1


# def keypad(string, keysdown):
#     key = index_of(True, keysdown)
#     print(pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
#           pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9)
#     if pygame.K_0 <= key <= pygame.K_9:
#         string += str(key - pygame.K_0)
#     return string
pygame.init()
screen = pygame.display.set_mode((900, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("CodePi Game")
back_button = pygame.image.load(
    './images/back_button.png').convert_alpha()
back_button_rect = back_button.get_rect(topleft=(50, 50))
back_button_selected = pygame.image.load(
    './images/back_button_selected.png').convert_alpha()
back_button_selected_rect = back_button_selected.get_rect(topleft=(50, 50))

alien_tutorial = pygame.image.load(
    './images/alien_tutorial.png').convert_alpha()
alien_tutorial_rect = alien_tutorial.get_rect(topleft=(100, 200))
text_box = pygame.image.load(
    './images/text_box.png').convert_alpha()
text_box_rect = text_box.get_rect(topleft=(30, 400))

font = pygame.font.Font('./fonts/Stickman-Regular.ttf', 32)

# --------------------------    TITLE SCREEN    --------------------------
title_screen = pygame.image.load(
    './images/title screen/title_screen.png').convert_alpha()
title_screen_rect = title_screen.get_rect(topleft=(0, 0))
title_screen_button = pygame.image.load(
    './images/title screen/button.png').convert_alpha()
title_screen_button_rect = title_screen_button.get_rect(center=(450, 550))


# --------------------------    CUTSCENES    --------------------------
cutscene1 = pygame.image.load(
    './images/cutscene/cutscene1.png').convert_alpha()
cutscene2 = pygame.image.load(
    './images/cutscene/cutscene2.png').convert_alpha()
cutscene3 = pygame.image.load(
    './images/cutscene/cutscene3.png').convert_alpha()
cutscene_rect = cutscene1.get_rect(topleft=(0, 0))
cutscenes = [cutscene1, cutscene2, cutscene3]


# --------------------------    PLANET    --------------------------
planet = pygame.image.load(
    './images/planet.png').convert_alpha()
planet_rect = planet.get_rect(topleft=(0, 0))


# --------------------------    ROCKET    --------------------------
rocket_broken = pygame.image.load(
    './images/rocket_broken.png').convert_alpha()
rocket_broken_rect = rocket_broken.get_rect(topleft=(600, 400))
rocket_broken_selected = pygame.image.load(
    './images/rocket_broken_selected.png').convert_alpha()
rocket_broken_selected_rect = rocket_broken_selected.get_rect(
    topleft=(600, 400))
rocket_broken_inside = pygame.image.load(
    './images/cutscene/cutscene1.png').convert_alpha()
rocket_broken_inside_rect = rocket_broken_inside.get_rect(topleft=(0, 0))

part1_rocket = font.render(
    "Part 1 done", True, 'black')
part1_rocket_rect = part1_rocket.get_rect(topleft=(400, 300))
part2_rocket = font.render(
    "Part 2 done", True, 'black')
part2_rocket_rect = part2_rocket.get_rect(topleft=(400, 300))
part3_rocket = font.render(
    "Part 3 done", True, 'black')
part3_rocket_rect = part3_rocket.get_rect(topleft=(400, 300))
rocket_fixed_bg = pygame.image.load(
    './images/rocket_fixed_bg.png').convert_alpha()
rocket_fixed_bg_rect = rocket_fixed_bg.get_rect(topleft=(0, 0))

# --------------------------    MOUNTAINS    --------------------------
mountains = pygame.image.load(
    './images/mountains.png').convert_alpha()
mountains_rect = mountains.get_rect(topleft=(100, 150))
mountains_selected = pygame.image.load(
    './images/mountains_selected.png').convert_alpha()
mountains_selected_rect = mountains_selected.get_rect(topleft=(100, 150))
mountains_dialogue1 = font.render(
    "It seems the path is blocked by a boulder.", True, 'black')
mountains_dialogue1_rect = mountains_dialogue1.get_rect(topleft=(100, 150))
mountains_dialogue2 = font.render(
    "What's this? There's a pulley system attached.", True, 'black')
mountains_dialogue2_rect = mountains_dialogue2.get_rect(topleft=(100, 150))
mountains_dialogue3 = font.render(
    "If the boulder is 15 kg, and the rocks are 5x kg, then what is x?", True, 'black')
mountains_dialogue3_rect = mountains_dialogue3.get_rect(topleft=(100, 150))
mountains_dialogue_iter1 = iter([mountains_dialogue1,
                                 mountains_dialogue2, mountains_dialogue3])

boulder_done1 = font.render(
    "It worked! There's the part!", True, 'black')
boulder_done1_rect = boulder_done1.get_rect(topleft=(100, 150))
boulder_done_iter = iter([boulder_done1])

boulder_progress = pygame.image.load(
    './images/boulder_progress.png').convert_alpha()
boulder_progress_rect = boulder_progress.get_rect(topleft=(0, 0))


# --------------------------    LAKE    --------------------------
lake = pygame.image.load(
    './images/lake.png').convert_alpha()
lake_rect = lake.get_rect(topleft=(0, 500))
lake_selected = pygame.image.load(
    './images/lake_selected.png').convert_alpha()
lake_selected_rect = lake_selected.get_rect(topleft=(0, 500))
lake_dialogue1 = font.render(
    "The lake has a bridge, but there's a keypad to lower it.", True, 'black')
lake_dialogue1_rect = lake_dialogue1.get_rect(topleft=(0, 500))
lake_dialogue2 = font.render(
    "To find the code, we need to solve 3x + 4 = 367", True, 'black')
lake_dialogue2_rect = lake_dialogue2.get_rect(topleft=(0, 500))
lake_dialogue_iter1 = iter([lake_dialogue1, lake_dialogue2])

keypad_string = ""
keypad_text = font.render(keypad_string, True, 'black')
keypad_text_rect = keypad_text.get_rect(topleft=(0, 500))
keypad_wrong = font.render("Wrong code", True, 'black')
keypad_wrong_rect = keypad_wrong.get_rect(topleft=(0, 500))
bridge_done_bg = pygame.image.load(
    './images/bridge_done_bg.png').convert_alpha()
bridge_done_bg_rect = bridge_done_bg.get_rect(topleft=(0, 0))

# --------------------------    TOWN    --------------------------
town = pygame.image.load(
    './images/town.png').convert_alpha()
town_rect = town.get_rect(topleft=(500, 250))
town_selected = pygame.image.load(
    './images/town_selected.png').convert_alpha()
town_selected_rect = town_selected.get_rect(topleft=(500, 250))
town_bg = pygame.image.load(
    './images/town_bg.png').convert_alpha()
town_bg_rect = town_bg.get_rect(topleft=(0, 0))
# aliens
town_alien1 = pygame.image.load(
    './images/alien_town1.png').convert_alpha()
town_alien1_rect = town_alien1.get_rect(topleft=(100, 400))
town_alien1_selected = pygame.image.load(
    './images/alien_town1_selected.png').convert_alpha()
town_alien1_selected_rect = town_alien1_selected.get_rect(topleft=(100, 400))
town_alien1_dialogue = pygame.image.load(
    './images/alien_town1_dialogue.png').convert_alpha()
town_alien1_dialogue_rect = town_alien1_dialogue.get_rect(topleft=(100, 200))
town_alien1_dialogue1 = font.render(
    "I can lead you to one of the parts, but it is blocked by a wall.", True, 'black')
town_alien1_dialogue1_rect = town_alien1_dialogue1.get_rect(topleft=(100, 200))
town_alien1_dialogue2 = font.render(
    "The wall has weak points that you can aim at with a linear equation of y = mx + b. (no gravity)", True, 'black')
town_alien1_dialogue2_rect = town_alien1_dialogue2.get_rect(topleft=(100, 200))
town_alien1_dialogue3 = font.render(
    "If the equation is correct, the wall will break.", True, 'black')
town_alien1_dialogue3_rect = town_alien1_dialogue3.get_rect(topleft=(100, 200))
town_alien1_dialogue_iter = iter([town_alien1_dialogue1,
                                 town_alien1_dialogue2, town_alien1_dialogue3])
dialogue = font.render("", True, 'black')
dialogue_rect = dialogue.get_rect(topleft=(100, 200))
town_alien2 = pygame.image.load(
    './images/alien_town2.png').convert_alpha()
town_alien2_rect = town_alien2.get_rect(topleft=(500, 500))
town_alien2_selected = pygame.image.load(
    './images/alien_town2_selected.png').convert_alpha()
town_alien2_selected_rect = town_alien2_selected.get_rect(topleft=(500, 500))

# --------------------------    PART 1    --------------------------
part1_bg = pygame.image.load(
    './images/part1/part1_bg.png').convert_alpha()
part1_bg_rect = part1_bg.get_rect(topleft=(0, 0))
alien1_wall_dialogue = font.render(
    "Change the coefficient of x to hit the weak points!", True, 'black')
alien1_wall_dialogue_rect = alien1_wall_dialogue.get_rect(topleft=(100, 200))
alien1_wall_dialogue_iter = iter([alien1_wall_dialogue])
coefficient_text = font.render(
    "y = m x + b", True, 'black')
coefficient_text_rect = coefficient_text.get_rect(topleft=(100, 200))

# --------------------------    GAME STATS/VARIABLES    --------------------------
game_status = 'home'
part1, part2, part3 = True, True, True
interact = 'tutorial'
cutscene = 0

while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_status == 'title':
                if title_screen_button_rect.collidepoint(mouse_pos):
                    game_status = 'cutscene'
            if game_status == 'cutscene':

                if cutscene >= 2:
                    game_status = 'home'
                else:
                    cutscene += 1
            if game_status == 'home':
                if interact == 'none':
                    if rocket_broken_rect.collidepoint(mouse_pos):
                        game_status = 'rocket_broken'
                    elif mountains_rect.collidepoint(mouse_pos):
                        game_status = 'mountains'
                        interact = 'boulder'
                    elif lake_rect.collidepoint(mouse_pos):
                        game_status = 'lake'
                        interact = 'bridge'
                    elif town_rect.collidepoint(mouse_pos):
                        game_status = 'town'
                else:
                    interact = 'none'

            if game_status == 'rocket_broken':
                if back_button_rect.collidepoint(mouse_pos):
                    game_status = 'home'
            if game_status == 'mountains':
                if back_button_rect.collidepoint(mouse_pos):
                    game_status = 'home'
            if game_status == 'lake':
                if back_button_rect.collidepoint(mouse_pos):
                    game_status = 'home'
                if interact == 'bridge':
                    if dialogue := next(lake_dialogue_iter1, None):
                        dialogue_rect = dialogue.get_rect(topleft=(0, 500))
                    else:
                        interact = 'none'
            if game_status == 'town':
                if back_button_rect.collidepoint(mouse_pos):
                    game_status = 'home'
                if town_alien1_rect.collidepoint(mouse_pos):
                    interact = 'alien1'
                if town_alien2_rect.collidepoint(mouse_pos):
                    interact = 'alien2'
                if interact == 'alien1':
                    if dialogue := next(town_alien1_dialogue_iter, None):
                        dialogue_rect = dialogue.get_rect(topleft=(100, 200))
                    else:
                        game_status = 'part1'
                        interact = 'alien1_wall'
            if game_status == 'mountains':
                if interact == 'boulder':
                    if dialogue := next(mountains_dialogue_iter1, None):
                        dialogue_rect = dialogue.get_rect(topleft=(100, 150))
                    else:
                        interact = 'boulder_progress'
                elif interact == 'boulder_progress':
                    interact = 'none'
                elif interact == 'boulder_done':
                    if dialogue := next(boulder_done_iter, None):
                        dialogue_rect = dialogue.get_rect(topleft=(100, 150))
                    else:
                        part2 = True
                        interact = 'part2_done'
            if game_status == 'part1':
                if interact == 'alien1_wall':
                    if dialogue := next(alien1_wall_dialogue_iter, None):
                        dialogue_rect = dialogue.get_rect(topleft=(100, 200))
                    else:
                        interact = 'none'
        if event.type == pygame.KEYDOWN:
            if game_status == 'lake':
                if event.key == pygame.K_BACKSPACE:
                    keypad_string = keypad_string[:-1]
                elif event.key == pygame.K_RETURN:

                    if keypad_string == '1234':
                        interact = 'bridge_done'
                        part3 = True
                    else:

                        interact = 'bridge_wrong'
                    keypad_string = ""
                if pygame.K_0 <= event.key <= pygame.K_9 and len(keypad_string) < 4:
                    keypad_string += str(event.key - pygame.K_0)

    if game_status == 'title':
        screen.fill('white')
        screen.blit(title_screen, title_screen_rect)
        screen.blit(title_screen_button, title_screen_button_rect)
    elif game_status == 'cutscene':
        screen.blit(cutscenes[cutscene], cutscene_rect)
    elif game_status == 'home':

        # keys = pygame.key.get_pressed()
        screen.fill('white')
        screen.blit(planet, planet_rect)
        screen.blit(rocket_broken, rocket_broken_rect)
        screen.blit(mountains, mountains_rect)
        screen.blit(lake, lake_rect)
        screen.blit(town, town_rect)
        if mountains_rect.collidepoint(mouse_pos) and interact == 'none':
            screen.blit(mountains_selected, mountains_selected_rect)
        if rocket_broken_rect.collidepoint(mouse_pos) and interact == 'none':
            screen.blit(rocket_broken_selected, rocket_broken_selected_rect)
        if lake_rect.collidepoint(mouse_pos) and interact == 'none':
            screen.blit(lake_selected, lake_selected_rect)
        if town_rect.collidepoint(mouse_pos) and interact == 'none':
            screen.blit(town_selected, town_selected_rect)
        if interact == 'tutorial':
            screen.blit(alien_tutorial, alien_tutorial_rect)
            screen.blit(text_box, text_box_rect)
    elif game_status == 'rocket_broken':
        screen.fill('white')
        screen.blit(rocket_broken_inside, rocket_broken_inside_rect)
        screen.blit(back_button, back_button_rect)
        if back_button_rect.collidepoint(mouse_pos):
            screen.blit(back_button_selected, back_button_selected_rect)
        if part1:
            screen.blit(part1_rocket, part1_rocket_rect)
        if part2:
            screen.blit(part2_rocket, part2_rocket_rect)
        if part3:
            screen.blit(part3_rocket, part3_rocket_rect)
        if part1 and part2 and part3:
            game_status = 'rocket_fixed'
    elif game_status == 'mountains':
        screen.fill('white')
        screen.blit(mountains, mountains_rect)
        # screen.blit(back_button, back_button_rect)
        # if back_button_rect.collidepoint(mouse_pos):
        #     screen.blit(back_button_selected, back_button_selected_rect)
        if interact == 'boulder':
            screen.blit(dialogue, dialogue_rect)
        elif interact == 'boulder_progress':
            screen.blit(boulder_progress, boulder_progress_rect)
        elif interact == 'boulder_done':
            screen.blit(dialogue, dialogue_rect)

    elif game_status == 'lake':
        screen.fill('white')
        screen.blit(lake, lake_rect)

        keypad_text = font.render(keypad_string, True, 'black')
        keypad_text_rect = keypad_text.get_rect(topleft=(0, 500))
        screen.blit(keypad_text, keypad_text_rect)

        if interact == 'bridge':
            screen.blit(dialogue, dialogue_rect)
        elif interact == 'bridge_wrong':
            screen.blit(keypad_wrong, keypad_wrong_rect)
        elif interact == 'bridge_done':
            screen.blit(bridge_done_bg, bridge_done_bg_rect)
            screen.blit(back_button, back_button_rect)
            if back_button_rect.collidepoint(mouse_pos):
                screen.blit(back_button_selected, back_button_selected_rect)

    elif game_status == 'town':
        screen.fill('white')

        if interact == 'none':
            screen.blit(town_bg, town_bg_rect)
            screen.blit(town_alien2, town_alien2_rect)
            screen.blit(town_alien1, town_alien1_rect)
        elif interact == 'alien1':
            screen.blit(town_bg, town_bg_rect)
            screen.blit(town_alien2, town_alien2_rect)
            screen.blit(town_alien1_dialogue, town_alien1_dialogue_rect)
            screen.blit(text_box, text_box_rect)
            screen.blit(dialogue, dialogue_rect)
        elif interact == 'alien2':
            screen.blit(town_bg, town_bg_rect)
            screen.blit(town_alien1, town_alien1_rect)
            screen.blit(text_box, text_box_rect)
        else:
            screen.blit(town_alien1, town_alien1_rect)
            screen.blit(town_alien2, town_alien2_rect)

        if town_alien1_rect.collidepoint(mouse_pos) and interact == 'none':
            screen.blit(town_alien1_selected, town_alien1_selected_rect)
        if town_alien2_rect.collidepoint(mouse_pos) and interact == 'none':
            screen.blit(town_alien2_selected, town_alien2_selected_rect)
        screen.blit(back_button, back_button_rect)
        if back_button_rect.collidepoint(mouse_pos):
            screen.blit(back_button_selected, back_button_selected_rect)
    elif game_status == 'part1':
        screen.fill('white')
        screen.blit(part1_bg, part1_bg_rect)
        if interact == 'alien1_wall':

            screen.blit(text_box, text_box_rect)
            screen.blit(dialogue, dialogue_rect)
        else:
            for x in range(0, WIDTH, grid_spacing):
                pygame.draw.line(screen, GRAY, (x, 0),
                                 (x, HEIGHT), 1)  # Vertical lines
            for y in range(0, HEIGHT, grid_spacing):
                pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y),
                                 1)  # Horizontal lines

            # Draw axes
            pygame.draw.line(
                screen, BLACK, (0, origin[1]), (WIDTH, origin[1]), 2)  # x-axis
            pygame.draw.line(
                screen, BLACK, (origin[0], 0), (origin[0], HEIGHT), 2)  # y-axis

            # Draw the y = mx + b line
            p1, p2 = calculate_line_points(m, b, WIDTH, grid_spacing)
            pygame.draw.line(screen, RED, p1, p2, 4)

            # Update the display
            pygame.display.flip()
            screen.blit(coefficient_text, coefficient_text_rect)

        if part1:
            interact = 'alien1_done'
    elif game_status == 'rocket_fixed':
        screen.fill('white')
        screen.blit(rocket_fixed_bg, rocket_fixed_bg_rect)

    pygame.display.update()
    clock.tick(60)

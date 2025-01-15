from sys import exit
import pygame


WIDTH, HEIGHT = 900, 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)


grid_spacing = 20
origin = (0, 700)


m = 3
b = 5


def graph_to_screen(x, y):
    screen_x = origin[0] + x * grid_spacing
    screen_y = origin[1] - y * grid_spacing
    return screen_x, screen_y


def calculate_line_points(m, b, width, spacing):

    x_min = -width // (2 * spacing)
    x_max = width // (2 * spacing)

    y1 = m * x_min + b
    y2 = m * x_max + b

    p1 = graph_to_screen(x_min, y1)
    p2 = graph_to_screen(x_max, y2)
    return p1, p2


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

text_box = pygame.image.load(
    './images/text_box.png').convert_alpha()
text_box_rect = text_box.get_rect(topleft=(30, 400))

font = pygame.font.Font('./fonts/SpaceGrotesk-VariableFont_wght.ttf', 20)

# --------------------------    TUTORIAL    --------------------------
alien_tutorial = pygame.image.load(
    './images/alien_tutorial.png').convert_alpha()
alien_tutorial_rect = alien_tutorial.get_rect(topleft=(100, 200))
alien_tutorial_dialogue = font.render(
    "Hey are your okay?", True, 'black')
alien_tutorial_dialogue2 = font.render(
    "It looks like your rocket is broken.", True, 'black')
alien_tutorial_dialogue3 = font.render(
    "I can help you fix it, but you need to find the parts first.", True, 'black')
alien_tutorial_dialogue4 = font.render(
    "You can find the parts around here, just click around the map.", True, 'black')
alien_tutorial_dialogue_iter = iter([alien_tutorial_dialogue,
                                    alien_tutorial_dialogue2,
                                    alien_tutorial_dialogue3,
                                    alien_tutorial_dialogue4])

# --------------------------    TITLE SCREEN    --------------------------
title_screen = pygame.image.load(
    './images/title screen/title_screen.png').convert_alpha()
title_screen_rect = title_screen.get_rect(topleft=(0, 0))
title_screen_button = pygame.image.load(
    './images/title screen/button.png').convert_alpha()
title_screen_button_rect = title_screen_button.get_rect(center=(450, 550))
title_screen_button_selected = pygame.image.load(
    './images/title screen/button_selected.png').convert_alpha()
title_screen_button_selected_rect = title_screen_button_selected.get_rect(
    center=(450, 550))


# --------------------------    CUTSCENES    --------------------------
cutscene1 = pygame.image.load(
    './images/cutscene/cutscene1.png').convert_alpha()
cutscene1_rect = cutscene1.get_rect(topleft=(0, 0))
cutscene_dialogue1 = font.render(
    "ALERT! ALERT!", True, 'black')
cutscene_dialogue1_rect = cutscene_dialogue1.get_rect(topleft=(100, 200))
cutscene_dialogue2 = font.render(
    "Critical failure detected in the propulsion system.", True, 'black')
cutscene_dialogue2_rect = cutscene_dialogue2.get_rect(topleft=(100, 200))
cutscene_dialogue3 = font.render(
    "Warning: Trajectory unstable. Rocket integrity compromised.", True, 'black')
cutscene_dialogue3_rect = cutscene_dialogue3.get_rect(topleft=(100, 200))
cutscene_dialogue4 = font.render(
    "Impact with nearby planet expected in 10... 9... 8...", True, 'black')
cutscene_dialogue4_rect = cutscene_dialogue4.get_rect(topleft=(100, 200))
cutscene_dialogue_iter1 = iter(
    [cutscene_dialogue1, cutscene_dialogue2, cutscene_dialogue3, cutscene_dialogue4])


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
    './images/rocket_broken_bg.png').convert_alpha()
rocket_broken_inside_rect = rocket_broken_inside.get_rect(topleft=(0, 0))

rocket_fixed_bg = pygame.image.load(
    './images/rocket_fixed_bg.png').convert_alpha()
rocket_fixed_bg_rect = rocket_fixed_bg.get_rect(topleft=(0, 0))
part1_item = pygame.image.load(
    './images/part.png').convert_alpha()
part1_item_rect = part1_item.get_rect(topleft=(100, 500))
part2_item = pygame.image.load(
    './images/part.png').convert_alpha()
part2_item_rect = part2_item.get_rect(topleft=(300, 500))
part3_item = pygame.image.load(
    './images/part.png').convert_alpha()
part3_item_rect = part3_item.get_rect(topleft=(500, 500))

rocket_fixed_dialogue = font.render(
    "You did it! With these parts, I fixed the rocket.", True, 'black')
rocket_fixed_dialogue2 = font.render(
    "Congrats on beating this game!", True, 'black')
rocket_fixed_dialogue_rect = rocket_fixed_dialogue.get_rect(topleft=(100, 200))
rocket_fixed_dialogue_iter = iter(
    [rocket_fixed_dialogue, rocket_fixed_dialogue2])

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
    "If the boulder is 300 kg, and there are 100 kg weights",  True, 'black')

mountains_dialogue3_rect = mountains_dialogue3.get_rect(topleft=(100, 150))
mountains_dialogue4 = font.render(
    "How many weights do we need to lift the boulder?", True, 'black')
mountains_dialogue4_rect = mountains_dialogue4.get_rect(topleft=(100, 150))
mountains_dialogue5 = font.render(
    "This can be modeled by the equation 300 = 100x", True, 'black')
mountains_dialogue5_rect = mountains_dialogue5.get_rect(topleft=(100, 150))
mountains_dialogue6 = font.render(
    "What is the value of x?", True, 'black')
mountains_dialogue6_rect = mountains_dialogue6.get_rect(topleft=(100, 150))
mountains_dialogue_iter1 = iter([mountains_dialogue1,
                                 mountains_dialogue2, mountains_dialogue3, mountains_dialogue4, mountains_dialogue5, mountains_dialogue6])

boulder_bg = pygame.image.load(
    './images/boulder_bg.png').convert_alpha()
boulder_bg_rect = boulder_bg.get_rect(topleft=(0, 0))
boulder_done1 = font.render(
    "It worked! There's the part!", True, 'black')
boulder_done1_rect = boulder_done1.get_rect(topleft=(100, 150))
boulder_done_iter = iter([boulder_done1])

boulder_progress = pygame.image.load(
    './images/boulder_progress.png').convert_alpha()
boulder_progress_rect = boulder_progress.get_rect(topleft=(0, 0))
boulder_done_bg = pygame.image.load(
    './images/boulder_done_bg.png').convert_alpha()
boulder_done_bg_rect = boulder_done_bg.get_rect(topleft=(0, 0))


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
    "To find the code, we need to solve 3x + 4 = 3673", True, 'black')
lake_dialogue2_rect = lake_dialogue2.get_rect(topleft=(0, 500))
lake_dialogue_iter1 = iter([lake_dialogue1, lake_dialogue2])

keypad_string = ""
keypad_text = font.render(keypad_string, True, 'black')
keypad_text_rect = keypad_text.get_rect(topleft=(100, 450))
keypad_wrong = font.render("Wrong code", True, 'black')
keypad_wrong_rect = keypad_wrong.get_rect(topleft=(100, 500))
bridge_done_bg = pygame.image.load(
    './images/bridge_done_bg.png').convert_alpha()
bridge_done_bg_rect = bridge_done_bg.get_rect(topleft=(0, 0))

lake_bg = pygame.image.load(
    './images/lake_bg.png').convert_alpha()
lake_bg_rect = lake_bg.get_rect(topleft=(0, 0))


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
    "The wall has a weak point that you can hit.", True, 'black')
town_alien1_dialogue2_rect = town_alien1_dialogue2.get_rect(topleft=(100, 200))
town_alien1_dialogue3 = font.render(
    "You can use y = mx + b to aim at the weak point.", True, 'black')
town_alien1_dialogue3_rect = town_alien1_dialogue3.get_rect(topleft=(100, 200))
town_alien1_dialogue4 = font.render(
    "If the equation is correct, the wall will break.", True, 'black')
town_alien1_dialogue4_rect = town_alien1_dialogue4.get_rect(topleft=(100, 200))
town_alien1_dialogue_iter = iter([town_alien1_dialogue1,
                                 town_alien1_dialogue2, town_alien1_dialogue3, town_alien1_dialogue4])
dialogue = font.render("", True, 'black')
dialogue_rect = dialogue.get_rect(topleft=(100, 450))


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
alien1_done = font.render(
    "You did it! The wall is broken!", True, 'black')
alien1_done_rect = alien1_done.get_rect(topleft=(100, 200))

alien1_done_iter = iter([alien1_done])

past_wall_bg = pygame.image.load(
    './images/past_wall_bg.png').convert_alpha()
past_wall_bg_rect = past_wall_bg.get_rect(topleft=(0, 0))

# --------------------------    GAME STATS/VARIABLES    --------------------------
game_status = 'title'
part1, part2, part3 = False, False, False
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
                if dialogue := next(cutscene_dialogue_iter1, None):
                    dialogue_rect = dialogue.get_rect(topleft=(100, 450))
                else:
                    game_status = 'home'
                    interact = 'tutorial'
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
                if interact == 'tutorial':
                    if dialogue := next(alien_tutorial_dialogue_iter, None):
                        dialogue_rect = dialogue.get_rect(topleft=(100, 450))
                    else:
                        interact = 'none'

            if game_status == 'rocket_broken':
                if back_button_rect.collidepoint(mouse_pos):
                    game_status = 'home'
                    interact = 'none'
            if game_status == 'mountains':
                if back_button_rect.collidepoint(mouse_pos):
                    game_status = 'home'
                    interact = 'none'
            if game_status == 'lake':
                if back_button_rect.collidepoint(mouse_pos):
                    game_status = 'home'
                    interact = 'none'
                if interact == 'bridge':
                    if dialogue := next(lake_dialogue_iter1, None):
                        dialogue_rect = dialogue.get_rect(topleft=(100, 450))
                    else:
                        interact = 'none'
            if game_status == 'town':
                if back_button_rect.collidepoint(mouse_pos):
                    game_status = 'home'
                    interact = 'none'
                if town_alien1_rect.collidepoint(mouse_pos):
                    interact = 'alien1'

                if interact == 'alien1':
                    if dialogue := next(town_alien1_dialogue_iter, None):
                        dialogue_rect = dialogue.get_rect(topleft=(100, 450))
                    else:
                        game_status = 'part1'
                        interact = 'alien1_wall'
            if game_status == 'mountains':
                if interact == 'boulder':
                    if dialogue := next(mountains_dialogue_iter1, None):
                        dialogue_rect = dialogue.get_rect(topleft=(100, 450))
                    else:
                        interact = 'boulder_progress'
                elif interact == 'boulder_progress':
                    interact = 'none'
                elif interact == 'boulder_done':
                    pass
                    # if dialogue := next(boulder_done_iter, None):
                    #     dialogue_rect = dialogue.get_rect(topleft=(100, 150))
                    # else:
                    #     part2 = True

            if game_status == 'part1':
                if interact == 'alien1_wall':
                    if dialogue := next(alien1_wall_dialogue_iter, None):
                        dialogue_rect = dialogue.get_rect(topleft=(100, 450))
                    else:
                        interact = 'none'
            if game_status == 'past_wall':
                if back_button_rect.collidepoint(mouse_pos):
                    game_status = 'home'
                    interact = 'none'
                # if interact == 'alien1_done':
                #     if dialogue := next(alien1_done_iter, None):
                #         dialogue_rect = dialogue.get_rect(topleft=(100, 200))
                #     else:
                #         interact = 'none'
                #         game_status = 'home'
            if game_status == 'rocket_fixed':
                if dialogue := next(rocket_fixed_dialogue_iter, None):
                    dialogue_rect = dialogue.get_rect(topleft=(100, 450))

        if event.type == pygame.KEYDOWN:
            if game_status == 'lake':
                if event.key == pygame.K_BACKSPACE:
                    keypad_string = keypad_string[:-1]
                elif event.key == pygame.K_RETURN:

                    if keypad_string == '1223':
                        interact = 'bridge_done'
                        part3 = True
                    else:

                        interact = 'bridge_wrong'
                    keypad_string = ""
                if pygame.K_0 <= event.key <= pygame.K_9 and len(keypad_string) < 4:
                    keypad_string += str(event.key - pygame.K_0)
            elif game_status == 'part1':
                if event.key == pygame.K_BACKSPACE:
                    keypad_string = keypad_string[:-1]
                elif event.key == pygame.K_RETURN:
                    m = float(keypad_string)
                    if keypad_string == '.2' or keypad_string == '0.2':
                        part1 = True
                        interact = 'none'
                        game_status = 'past_wall'
                    keypad_string = ""
                if pygame.K_0 <= event.key <= pygame.K_9:
                    keypad_string += str(event.key - pygame.K_0)
                elif event.key == pygame.K_PERIOD:
                    keypad_string += '.'
            elif interact == 'boulder_progress':
                if event.key == pygame.K_BACKSPACE:
                    keypad_string = keypad_string[:-1]
                elif event.key == pygame.K_RETURN:

                    if keypad_string == '3':
                        part2 = True
                        interact = 'boulder_done'

                    keypad_string = ""
                elif pygame.K_0 <= event.key <= pygame.K_9:
                    keypad_string += str(event.key - pygame.K_0)

    if game_status == 'title':
        screen.fill('white')
        screen.blit(title_screen, title_screen_rect)
        screen.blit(title_screen_button, title_screen_button_rect)
        if title_screen_button_rect.collidepoint(mouse_pos):
            screen.blit(title_screen_button_selected,
                        title_screen_button_selected_rect)
    elif game_status == 'cutscene':
        screen.blit(cutscene1, cutscene1_rect)
        screen.blit(text_box, text_box_rect)
        screen.blit(dialogue, dialogue_rect)
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
            screen.blit(dialogue, dialogue_rect)
    elif game_status == 'rocket_broken':
        screen.fill('white')
        screen.blit(rocket_broken_inside, rocket_broken_inside_rect)
        screen.blit(back_button, back_button_rect)
        if back_button_rect.collidepoint(mouse_pos):
            screen.blit(back_button_selected, back_button_selected_rect)
        if part1:
            screen.blit(part1_item, part1_item_rect)
        if part2:
            screen.blit(part2_item, part2_item_rect)
        if part3:
            screen.blit(part3_item, part3_item_rect)
        if part1 and part2 and part3:
            game_status = 'rocket_fixed'
            dialogue = next(rocket_fixed_dialogue_iter, None)
            dialogue_rect = dialogue.get_rect(topleft=(100, 450))
    elif game_status == 'mountains':
        screen.fill('white')

        if interact == 'boulder':
            screen.blit(boulder_bg, boulder_bg_rect)
            screen.blit(text_box, text_box_rect)
            screen.blit(dialogue, dialogue_rect)

        elif interact == 'boulder_progress':
            screen.blit(boulder_progress, boulder_progress_rect)
            screen.blit(text_box, text_box_rect)
            keypad_text = font.render(
                'What is the value of x? ' + keypad_string, True, 'black')
            keypad_text_rect = keypad_text.get_rect(topleft=(100, 450))
            screen.blit(keypad_text, keypad_text_rect)
        elif interact == 'boulder_done':
            screen.blit(boulder_done_bg, boulder_done_bg_rect)
            screen.blit(back_button, back_button_rect)
            if back_button_rect.collidepoint(mouse_pos):
                screen.blit(back_button_selected, back_button_selected_rect)

    elif game_status == 'lake':
        screen.fill('white')
        screen.blit(lake_bg, lake_bg_rect)
        screen.blit(text_box, text_box_rect)

        if interact == 'bridge':

            screen.blit(dialogue, dialogue_rect)
        else:
            keypad_text = font.render(
                'What is the code to lower the bridge (3x + 4 = 3673)? ' + keypad_string, True, 'black')
            keypad_text_rect = keypad_text.get_rect(topleft=(100, 450))
            screen.blit(keypad_text, keypad_text_rect)
        if interact == 'bridge_wrong':
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
            screen.blit(town_alien1, town_alien1_rect)
        elif interact == 'alien1':
            screen.blit(town_bg, town_bg_rect)
            screen.blit(town_alien1_dialogue, town_alien1_dialogue_rect)
            screen.blit(text_box, text_box_rect)
            screen.blit(dialogue, dialogue_rect)
        elif interact == 'alien2':
            screen.blit(town_bg, town_bg_rect)
            screen.blit(town_alien1, town_alien1_rect)
            screen.blit(text_box, text_box_rect)
        else:
            screen.blit(town_alien1, town_alien1_rect)

        if town_alien1_rect.collidepoint(mouse_pos) and interact == 'none':
            screen.blit(town_alien1_selected, town_alien1_selected_rect)

        screen.blit(back_button, back_button_rect)
        if back_button_rect.collidepoint(mouse_pos):
            screen.blit(back_button_selected, back_button_selected_rect)
    elif game_status == 'part1':
        screen.fill('white')
        screen.blit(part1_bg, part1_bg_rect)
        if interact == 'alien1_wall':

            screen.blit(text_box, text_box_rect)
            screen.blit(dialogue, dialogue_rect)
        elif interact == 'alien1_done':
            screen.blit(text_box, text_box_rect)
            screen.blit(dialogue, dialogue_rect)
        else:
            for x in range(0, WIDTH, grid_spacing):
                pygame.draw.line(screen, GRAY, (x, 0),
                                 (x, HEIGHT), 1)
            for y in range(0, HEIGHT, grid_spacing):
                pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y),
                                 1)

            pygame.draw.line(
                screen, BLACK, (0, origin[1]), (WIDTH, origin[1]), 2)
            pygame.draw.line(
                screen, BLACK, (origin[0], 0), (origin[0], HEIGHT), 2)

            p1, p2 = calculate_line_points(m, b, 1600, grid_spacing)
            pygame.draw.line(screen, RED, p1, p2, 4)
            coefficient_text = font.render(
                f"equation: y = {m}x + {b}", True, 'black')
            coefficient_text_rect = coefficient_text.get_rect(
                topleft=(100, 100))
            screen.blit(text_box, text_box.get_rect(topleft=(50, 50)))
            screen.blit(coefficient_text, coefficient_text_rect)
            keypad_text = font.render("m: " + keypad_string, True, 'black')

            keypad_text_rect = keypad_text.get_rect(topleft=(100, 150))

            screen.blit(keypad_text, keypad_text_rect)

    elif game_status == 'past_wall':
        screen.fill('white')
        screen.blit(past_wall_bg, past_wall_bg_rect)
        screen.blit(back_button, back_button_rect)
        if back_button_rect.collidepoint(mouse_pos):
            screen.blit(back_button_selected, back_button_selected_rect)
    elif game_status == 'rocket_fixed':
        screen.fill('white')
        screen.blit(rocket_fixed_bg, rocket_fixed_bg_rect)
        screen.blit(part1_item, part1_item_rect)
        screen.blit(part2_item, part2_item_rect)
        screen.blit(part3_item, part3_item_rect)
        screen.blit(alien_tutorial, alien_tutorial_rect)

        screen.blit(text_box, text_box_rect)
        screen.blit(dialogue, dialogue_rect)

    pygame.display.update()
    clock.tick(60)

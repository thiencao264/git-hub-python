# 1. Draw tube
# 2. Draw bird
# 3. record scores
# 4. Stop Screen

# Draw tubes inverse

import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
TUBE_VELOCITY = 3
TUBE_WIDTH = 50
tube1_x = 0
tube2_x = 200
tube3_x = 400
TUBE_GAP = 150
BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
bird_drop_velocity = 0
GRAVITY = 0.5
score = 0
font = pygame.font.SysFont('sans', 40)
# Create random hights
tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)

tube1_pass = False
tube2_pass = False
tube3_pass = False


while running:
    clock.tick(60)
    screen.fill(GREEN)

    # draw tubes
    tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
    tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
    tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))


    #draw tubes inverse
    tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH,  HEIGHT - TUBE_GAP))
    tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - TUBE_GAP))
    tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - TUBE_GAP))

    # Move tubes to left sid.
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY

    # Draw bird
    bird_rect = pygame.draw.rect(screen, RED, (BIRD_X, bird_y, BIRD_WIDTH,  BIRD_HEIGHT))

    # Bird fall
    bird_y = bird_y + bird_drop_velocity
    bird_drop_velocity += GRAVITY




    # If tube_x <50 then (disappear on screen) then assign tub_x = 550
    # Generate new tube
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100, 400)
        tube1_pass = False

    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100, 400)
        tube2_pass = False

    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100, 400)
        tube3_pass = False
        

    score_txt = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_txt, (5, 5))
    if (tube1_x + TUBE_WIDTH <= BIRD_X) and tube1_pass == False:
        score += 1
        tube1_pass = True

    if (tube2_x + TUBE_WIDTH <= BIRD_X) and tube2_pass == False:
        score += 1
        tube2_pass = True

    if (tube3_x + TUBE_WIDTH <= BIRD_X) and tube3_pass == False:
        score += 1
        tube3_pass = True
    #update score



    #Check collision
    # if bird_rect.colliderect(tube1_rect):
    #     TUBE_VELOCITY = 0
    # if bird_rect.colliderect(tube2_rect):
    #     TUBE_VELOCITY = 0
    # if bird_rect.colliderect(tube3_rect):
    #     TUBE_VELOCITY = 0

    # if bird_rect.colliderect(tube1_rect_inv):
    #     TUBE_VELOCITY = 0
    # if bird_rect.colliderect(tube2_rect_inv):
    #     TUBE_VELOCITY = 0
    # if bird_rect.colliderect(tube3_rect_inv):
    #     TUBE_VELOCITY = 0

    for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv]:
        if bird_rect.colliderect(tube):
            TUBE_VELOCITY = 0
            bird_drop_velocity = 0

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_drop_velocity = 0
                bird_drop_velocity -= 10




    pygame.display.flip()

pygame.quit()
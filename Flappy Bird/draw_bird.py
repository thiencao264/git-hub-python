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

# Create random hights
tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)

while running:
    clock.tick(60)
    screen.fill(GREEN)

    # draw tubes
    pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
    pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
    pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))


    #draw tubes inverse
    pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH,  HEIGHT - TUBE_GAP))
    pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - TUBE_GAP))
    pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - TUBE_GAP))

    # Move tubes to left sid.
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY

    # Draw bird
    pygame.draw.rect(screen, RED, (BIRD_X, bird_y, BIRD_WIDTH,  BIRD_HEIGHT))

    # Bird fall
    bird_y = bird_y + bird_drop_velocity
    bird_drop_velocity += GRAVITY




    # If tube_x <50 then (disappear on screen) then assign tub_x = 550
    # Generate new tube
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100, 400)
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100, 400)
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100, 400)
        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_drop_velocity = 0
                bird_drop_velocity -= 10




    pygame.display.flip()

pygame.quit()
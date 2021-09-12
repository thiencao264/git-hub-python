# 1. Draw tube
# 2. Draw bird
# 3. record scores
# 4. Stop Screen

# Draw 03 tube and move it to left

# Create a new tube with x = 550 if the tube move to x = -50

# => Three tubes will move to left continuously.

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
TUBE_VELOCITY = 3
TUBE_WIDTH = 50
tube1_x = 0
tube2_x = 200
tube3_x = 400
tube1_height = 300
tube2_height = 300
tube3_height = 300

while running:
    clock.tick(60)
    screen.fill(GREEN)

    # Create 03 tubes
    pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
    pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
    pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))

    # Move tubes to left sid.
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY

    # If tube_x <50 then (disappear on screen) then assign tub_x = 550
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
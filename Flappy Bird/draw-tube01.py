# 1. Draw tube
# 2. Draw bird
# 3. record scores
# 4. Stop Screen


# Draw one tube and move it to left
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
tube1_x = 300

tube1_height = 300

while running:
    clock.tick(60)
    screen.fill(GREEN)

    pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))

    tube1_x = tube1_x - TUBE_VELOCITY
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
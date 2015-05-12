import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


grid = []
for row in range (10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

pygame.init()
size = [400, 400]
screen = pygame.display.set_mode(size)
tileWidth = 20
tileHeight = 20
tileMargin = 5
color = WHITE




 
pygame.display.set_caption("Rush Hour")


"""class Visualization:
    def __init__(self, width, height)"""

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True    

    
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20])


pygame.quit()
            




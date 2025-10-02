import pygame
import sys
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Rectangles Game")


WHITE = (255, 255, 255)
col1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
col2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


rect1 = pygame.Rect(100, 100, 60, 60)
rect2 = pygame.Rect(400, 300, 80, 80)

COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_EVENT, 3000)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == COLOR_EVENT:
            col1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            col2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    pygame.draw.rect(screen, col1, rect1)
    pygame.draw.rect(screen, col2, rect2)

    pygame.display.flip()

pygame.quit()
sys.exit()

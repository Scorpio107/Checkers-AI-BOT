import pygame

width, height = 800, 800
rows, cols = 8, 8
square_side = width // cols

# rgb
brown = (101, 67, 33)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
grey = (128,128,128)

crown = pygame.transform.scale(pygame.image.load('Images/kingcrown.png'), (45, 25))

import pygame
import colorsys

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
hue = 0

WIDTH = 2000
HEIGHT = 2000

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
columns = WIDTH // x_separator

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Number 1')
font = pygame.font.SysFont('Arial', 18, bold=True)

# Define the number '1' pattern (5x5)
number_1 = [
    '11111',
    '  11 ',
    '  11 ',
    '  11 ',
    '11111'
]

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    screen.blit(text, (x_start, y_start))

run = True
x_start, y_start = 0, 0

while run:
    screen.fill(black)
    
    for i in range(len(number_1)):
        for j in range(len(number_1[i])):
            if number_1[i][j] == '1':
                text_display('1', x_start, y_start)
            x_start += x_separator
        y_start += y_separator
        x_start = 0
    
    pygame.display.update()

    hue += 0.005

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
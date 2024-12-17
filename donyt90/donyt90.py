import pygame
import random
import math

# Set dimensions for the display window
window_width = 500
window_height = 500

# Set colors
window_color = (0, 0, 0)  # Black
character_color = (255, 0, 255)  # Pink

# Initialize pygame
pygame.init()

# Create display window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("3D rotation of numbers(0-9)")

# Set rotation speeds
x_axis_rotate_speed = random.uniform(0.005, 0.025)
y_axis_rotate_speed = random.uniform(0.005, 0.025)
z_axis_rotate_speed = random.uniform(0.005, 0.025)

#Draw the characters 0-9 in their 2D view
characters = {
    '0': [
        '     11111     ',
        '   111111111   ',
        '  11111111111  ',
        ' 1111111111111 ',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        ' 1111111111111 ',
        '  11111111111  ',
        '   111111111   ',
        '     11111     '
    ],
    '1': [
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111'
    ],
    '2': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111'
    ],
    '3': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111'
    ],
    '4': [
        '          11111',
        '        1111111',
        '       11111111',
        '      111111111',
        '     1111111111',
        '    11111 11111',
        '   11111  11111',
        '  11111   11111',
        ' 11111    11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111'
    ],
    '5': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111'

    ],
    '6': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111'
    ],
    '7': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '         11111 ',
        '        11111  ',
        '       11111   ',
        '       11111   ',
        '      11111    ',
        '      11111    ',
        '     11111     ',
        '     11111     ',
        '    11111      ',
        '    11111      ',
        '   11111       ',
        '   11111       ',
        '  11111        ',
        '  11111        ',
        ' 11111         ',
        ' 11111         ',
        '11111          ',
        '11111          ',
    ],
    '8': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',

    ],
    '9': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
    ]
}
running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# Initial rotation angles
x_start_angle = 0
y_start_angle = 0
z_start_angle = 0

# Pause state for a character
pause_states = {char: False for char in characters.keys()}

character = input("Enter the numerical character you want: ")
print('Press enter to pause. Choose a new number.')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                character = input("\nEnter the numerical character you want: ")
                print('Press enter to pause. Choose a new number')

            elif event.key == pygame.K_RETURN:  # Press enter key to pause
                pause_states[character] = not pause_states[character]

    if not pause_states[character]:
        # Reset the screen
        window.fill(window_color)

        for i, line in enumerate(characters[character]):
            for j, char in enumerate(line):
                if char == '1':
                    # Set character depth with 5 characters
                    for depth in range(5):
                        x = j - len(line) / 2
                        y = i - len(characters[character]) / 2
                        z = depth - 2  # Adjust the depth

                        # Rotate around the x-axis
                        y_rotation_angle = y * math.cos(x_start_angle) - z * math.sin(x_start_angle)
                        z_rotation_angle = y * math.sin(x_start_angle) + z * math.cos(x_start_angle)

                        # Rotate around the y-axis
                        x_rotation_angle = x * math.cos(y_start_angle) + z_rotation_angle * math.sin(y_start_angle)
                        z_rotation_angle = -x * math.sin(y_start_angle) + z_rotation_angle * math.cos(y_start_angle)

                        # Rotate around the z-axis
                        x_rotation_angle_final = x_rotation_angle * math.cos(z_start_angle) - y_rotation_angle * math.sin(z_start_angle)
                        y_rotation_angle_final = x_rotation_angle * math.sin(z_start_angle) + y_rotation_angle * math.cos(z_start_angle)

                        # Convert the 3D coordinates to 2D screen coordinates
                        scale = 10
                        x_screen = int(x_rotation_angle_final * scale + window_width / 2)
                        y_screen = int(y_rotation_angle_final * scale + window_height / 2)

                        # Set font size
                        text_render = font.render('1', True, character_color)
                        window.blit(text_render, (x_screen, y_screen))

        # Change the rotation angles
        x_start_angle += x_axis_rotate_speed
        y_start_angle += y_axis_rotate_speed
        z_start_angle += z_axis_rotate_speed

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the program
pygame.quit()
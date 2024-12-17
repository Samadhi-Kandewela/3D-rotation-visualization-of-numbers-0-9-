import pygame
import random
import math

def draw_character(character, x_start_angle, y_start_angle, z_start_angle):
    # Iterate through each line of the character
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

                    # Draw the point
                    pygame.draw.line(window, character_color, (x_screen, y_screen), (x_screen, y_screen))

# Initialize pygame
pygame.init()

# Set dimensions for display window
window_width = 500
window_height = 500

# Create the display window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("3D rotation of numbers(0-9)")

# Set colors
window_color = (0, 0, 0)  # Set to black
character_color = (255, 255, 255)  # Set to white 

# Set rotation speeds
x_axis_rotate_speed = random.uniform(0.005, 0.025)
y_axis_rotate_speed = random.uniform(0.005, 0.025)
z_axis_rotate_speed = random.uniform(0.005, 0.025)

character = input("Enter the numerical character you want: ")
print('Press enter to pause. Choose a new number.')

# Initial rotation angles
x_start_angle = 0
y_start_angle = 0
z_start_angle = 0

# Pause state for a character
pause_states = {char: False for char in characters.keys()}

# Main game loop
running = True
clock = pygame.time.Clock()

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

        # Draw the character with 3D rotation
        draw_character(character, x_start_angle, y_start_angle, z_start_angle)

        # Change the rotation angles
        x_start_angle += x_axis_rotate_speed
        y_start_angle += y_axis_rotate_speed
        z_start_angle += z_axis_rotate_speed

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the program
pygame.quit()


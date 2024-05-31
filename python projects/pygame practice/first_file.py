import pygame

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the player as a Rect object
player = pygame.Rect(0, 0, 50, 50)

# Main game loop
running = True
while running:
    # Fill the screen with black to clear it
    screen.fill((0, 0, 0))

    # Draw the player rectangle
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Get the state of all keyboard keys
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-5, 0)
    if key[pygame.K_d]:
        player.move_ip(5, 0)
    if key[pygame.K_w]:
        player.move_ip(0, -5)
    if key[pygame.K_s]:
        player.move_ip(0, 5)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()


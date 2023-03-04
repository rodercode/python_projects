# Import and initialize the pygame library
import pygame
pygame.init

# Set up the drawing window
window_size = [500, 500]
window = pygame.display.set_mode(window_size)

# Game Loop
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set background color to the scene
    window.fill((255, 255, 255))

    # Draw a solid green circle in the center
    pygame.draw.circle(window, (100, 200, 50), (250, 250), 50)

    # update content on the scene for each frame
    pygame.display.flip()

# exit the game
pygame.quit()

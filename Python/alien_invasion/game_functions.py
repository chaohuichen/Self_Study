import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                #ship.rect.centerx += 1
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.big_color)
    ship.blitme()

    #Make the most recently drawn screen visible.
    pygame.display.flip()

import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('Images/ship.png')
        self.rect = self.image.get_rect()
        self.small_image = pygame.transform.scale(self.image, (261, 138))

        # Start each new ship at the left center of the screen.
        self.rect.left = 0
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        # This allows the image to touch the bottom of the screen
        if self.moving_down and self.rect.bottom < (self.screen_rect.bottom + 180):
            self.y += self.settings.ship_speed

        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.small_image, self.rect)

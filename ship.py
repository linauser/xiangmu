import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/1.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:  # 新增：检查飞船是否在屏幕顶部
            self.y -= self.settings.ship_speed  # 更新 y 位置
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:  # 新增：检查飞船是否在屏幕底部
            self.y += self.settings.ship_speed  # 更新 y 位置
            
        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y  # 更新 y 坐标

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

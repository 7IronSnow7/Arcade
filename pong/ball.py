import constants
import random
import math
import arcade

class Ball:
    def __init__(self):
        # Ball sprite
        radius = constants.BALL_SIZE // 2
        self.sprite = arcade.SpriteCircle(
            radius,
            arcade.color.RED
        )
        
        self.speed_multiplier = 1.0
        self.base_speed = constants.BALL_SPEED

        self.reset()
    
    def reset(self):
        # Reset ball position to center
        self.sprite.center_x = constants.WINDOW_WIDTH / 2
        self.sprite.center_y = constants.WINDOW_HEIGHT / 2
        
        # Random angle between -45 and 45 degrees
        angle = random.randint(-45, 45)
        angle_rad = math.radians(angle)
        
        # Set velocity based on angle
        self.change_x = constants.BALL_SPEED * math.cos(angle_rad)
        self.change_y = constants.BALL_SPEED * math.sin(angle_rad)
        
        self.speed_multiplier = 1.0
    
    def check_paddle_collision(self, paddle):
        # Check if ball overlaps with paddle
        if (self.sprite.right > paddle.sprite.left and 
            self.sprite.left < paddle.sprite.right and
            self.sprite.top > paddle.sprite.bottom and 
            self.sprite.bottom < paddle.sprite.top):
            
            # Increase speed
            self.speed_multiplier += 0.1
            
            # Reverse x direction and apply speed multiplier
            self.change_x = -self.change_x * self.speed_multiplier
            
            # Return True to indicate collision occurred
            return True
        return False
    def update(self):
        # Update ball position
        self.sprite.center_x += self.change_x
        self.sprite.center_y += self.change_y

        # Bounce off top and bottom
        if self.sprite.top > constants.WINDOW_HEIGHT or self.sprite.bottom < 0:
            self.change_y = -self.change_y

    def draw(self):
        self.sprite.draw()
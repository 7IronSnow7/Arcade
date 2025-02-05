import arcade
import constants

class Paddle:
    def __init__(self, x, y, is_player=True):
        # Create paddle sprite
        self.sprite = arcade.SpriteSolidColor(
            constants.PADDLE_WIDTH,
            constants.PADDLE_HEIGHT,
            constants.PADDLE_COLOR
        )
        
        # Set initial position
        self.sprite.center_x = x
        self.sprite.center_y = y
        
        # Movement
        self.change_y = 0
        
       # Paddle control type (player/AI)
        self.is_player = is_player
        
        # Reference to ball (for AI)
        self.ball = None
        
    def set_ball(self, ball):
        self.ball = ball

    def update(self):
        if not self.is_player and self.ball:
            # AI movement
            target_y = self.ball.sprite.center_y
            move_speed = 4 # Adjust this value for smoothness
            
            if abs(self.sprite.center_y - target_y) > move_speed:
                if self.sprite.center_y < target_y:
                    self.change_y = move_speed
                else:
                    self.change_y = -move_speed
            else:
                self.change_y = 0
        
        # Update paddle position
        self.sprite.center_y += self.change_y
        
        # Keep paddle on screen
        if self.sprite.top > constants.WINDOW_HEIGHT:
            self.sprite.top = constants.WINDOW_HEIGHT
        elif self.sprite.bottom < 0:
            self.sprite.bottom = 0

    def move_up(self):
        self.change_y = constants.PADDLE_SPEED

    def move_down(self):
        self.change_y = -constants.PADDLE_SPEED

    def stop(self):
        self.change_y = 0

    def draw(self):
        self.sprite.draw()
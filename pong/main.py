import arcade
import constants
from ball import Ball
from paddle import Paddle

# class PongGame(arcade.Window):
#     def __init__(self):
#         super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Pong")
#         # Game state
#         self.game_state = "MENU"
        
#         # Create Text objects for the menu
#         self.title_text = arcade.Text(
#             "PONG",
#             WINDOW_WIDTH / 2,
#             WINDOW_HEIGHT * 0.7,
#             arcade.color.AMARANTH_PINK,
#             50,
#             anchor_x="center"
#         )
        
#         self.instruction_text = arcade.Text(
#             "Use UP/DOWN or W/S to move paddle",
#             WINDOW_WIDTH / 2,
#             WINDOW_HEIGHT * 0.5,
#             arcade.color.BURNT_UMBER,
#             20,
#             anchor_x="center"
#         )
        
#         self.start_text = arcade.Text(
#             "Press SPACE to start",
#             WINDOW_WIDTH / 2,
#             WINDOW_HEIGHT * 0.4,
#             arcade.color.CORAL,
#             20,
#             anchor_x="center"
#         )
        
#         # Create Text objects for scores
#         self.player_score_text = arcade.Text(
#             "0",
#             WINDOW_WIDTH / 4,
#             WINDOW_HEIGHT - 50,
#             arcade.color.DARK_GOLDENROD,
#             30
#         )
        
#         self.opponent_score_text = arcade.Text(
#             "0",
#             3 * WINDOW_WIDTH / 4,
#             WINDOW_HEIGHT - 50,
#             arcade.color.AMARANTH_PINK,
#             30
#         )
        
#         # Set up game objects
#         self.player_paddle = None
#         self.opponent_paddle = None
#         self.ball = None
        
#         # Create the sprite list
#         self.sprite_list = None
        
#         # Set background color
#         arcade.set_background_color(arcade.color.BLACK)
#         self.setup()
        
#         self.player_score = 0
#         self.opponent_score = 0
#         # Track ball speed
#         self.current_ball_speed = BALL_SPEED
        
#     def setup(self):
#         # Create sprite list
#         self.sprite_list = arcade.SpriteList()
        
#         # Create game objects
#         self.player_paddle = arcade.SpriteSolidColor(10, 100, arcade.color.WHITE)
#         self.player_paddle.center_x = 50
#         self.player_paddle.center_y = WINDOW_HEIGHT // 2
        
#         # Create AI opponent
#         self.opponent_paddle = arcade.SpriteSolidColor(10, 100, arcade.color.RADICAL_RED)
#         self.opponent_paddle.center_x = WINDOW_WIDTH - 50
#         self.opponent_paddle.center_y = WINDOW_HEIGHT // 2
        
#         # Add ball
#         self.ball = arcade.SpriteCircle(BALL_SIZE, arcade.color.WHITE)
#         self.ball.center_x = WINDOW_WIDTH // 2
#         self.ball.center_y = WINDOW_HEIGHT // 2
#         self.ball.change_x = BALL_SPEED
#         self.ball.change_y = BALL_SPEED
        
#         # Add sprites to the list
#         self.sprite_list.append(self.player_paddle)
#         self.sprite_list.append(self.opponent_paddle)
#         self.sprite_list.append(self.ball)
            
#     def on_draw(self):
#        # Clear screen and draw objects
#         self.clear()
#         self.sprite_list.draw()
        
#         # Draw scores (update text and draw)
#         self.player_score_text.text = f"{self.player_score}"
#         self.opponent_score_text.text = f"{self.opponent_score}"
#         self.player_score_text.color = arcade.color.AIR_FORCE_BLUE
#         self.opponent_score_text.color = arcade.color.ARMY_GREEN
#         self.player_score_text.draw()
#         self.opponent_score_text.draw()
        
#         # Draw Menu state if in menu state
#         if self.game_state == "MENU":
#             # Update colors for menu items
#             self.title_text.color = arcade.color.YELLOW_ROSE
#             self.instruction_text.color = arcade.color.PURPLE_HEART
#             self.start_text.color = arcade.color.WHITE
            
#             # Draw menu items
#             self.title_text.draw()
#             self.instruction_text.draw()
#             self.start_text.draw()
        
#     def on_update(self, delta_time):
#         if self.game_state == "PLAYING":
            
#             # Update sprite position
#             self.sprite_list.update()
            
#             # Keep player paddle in bounds
#             if self.player_paddle.top > WINDOW_HEIGHT:
#                 self.player_paddle.top = WINDOW_HEIGHT
#             if self.player_paddle.bottom < 0:
#                 self.player_paddle.bottom = 0
                    
#             # Ball bouncing off top and bottom
#             if self.ball.top > WINDOW_HEIGHT or self.ball.bottom < 0:
#                 self.ball.change_y *= -1
                    
#             # Check for ball collision with paddles
#             if arcade.check_for_collision(self.ball, self.player_paddle) or \
#             arcade.check_for_collision(self.ball, self.opponent_paddle):
#                 # Reverse ball direction
#                 self.ball.change_x *= -1
#                 # Increase ball speed
#                 self.current_ball_speed *= 1.1
#                 self.ball.change_x = self.current_ball_speed if self.ball.change_x > 0 else -self.current_ball_speed
#                 self.ball.change_y = self.current_ball_speed if self.ball.change_y > 0 else -self.current_ball_speed
                    
#             # AI movement
#             if self.opponent_paddle.center_y < self.ball.center_y:
#                 self.opponent_paddle.center_y += PADDLE_SPEED
#             elif self.opponent_paddle.center_y > self.ball.center_y:
#                 self.opponent_paddle.center_y -= PADDLE_SPEED
                    
#             # Keep AI paddle in bounds
#             if self.opponent_paddle.top > WINDOW_HEIGHT:
#                 self.opponent_paddle.top = WINDOW_HEIGHT
#             if self.opponent_paddle.bottom < 0:
#                 self.opponent_paddle.bottom = 0
                        
#             # Scoring and reset ball
#             if self.ball.right > WINDOW_WIDTH: # Player scores
#                 self.player_score += 1
#                 self.reset_ball()
#             elif self.ball.left < 0:
#                 self.opponent_score += 1
#                 self.reset_ball()
                    
                
#     def on_key_press(self, key, modifiers):
#         print("Any key when pressed")
#         # Handle key presses
#         if key == arcade.key.SPACE and self.game_state == "MENU":
#             # Change game state to playing
#             self.game_state = "PLAYING"
#             # Reset ball to start the game
#             self.reset_ball()
#         if self.game_state == "PLAYING":
#             if key == arcade.key.UP:
#                 self.player_paddle.change_y = PADDLE_SPEED
#             elif key == arcade.key.DOWN:
#                 self.player_paddle.change_y = -PADDLE_SPEED
            
#     def on_key_release(self, key, modifiers):
#         # Stop paddle when key is released
#         if key in (arcade.key.UP, arcade.key.S, arcade.key.DOWN, arcade.key.W):
#             self.player_paddle.change_y = 0
            
#     def reset_ball(self):
#         self.ball.center_x = WINDOW_WIDTH // 2
#         self.ball.center_y = WINDOW_HEIGHT // 2
        
#         # Reset speed to initial value
#         self.current_ball_speed = BALL_SPEED
        
#         # Randomize direction
#         direction = random.choice([-1, 1])
        
#         # Randomize angle
#         angle = random.uniform(-45, 45)
        
#         # Convert angle to radians and calculate x/y components
#         angle_rad = math.radians(angle)
#         self.ball.change_x = direction * self.current_ball_speed * math.cos(angle_rad)
#         self.ball.change_y = self.current_ball_speed * math.sin(angle_rad)
            
# def main():
#     game = PongGame()
#     game.setup()
#     arcade.run()
    
# if __name__ == "__main__":
#     main()
    
    # Adding in more features to get it working on personal portfoilio
    # More features to add.
    
#_______________________________________________________________________________
# ABOVE THIS LINE THE PONG GAME CAN RUN WITHOUT ANY IMPORTS FROM THE CLASSES
# P.S just change the constant variables in the constants directory
    
class PongGame(arcade.Window):
    def __init__(self):
        super().__init__(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT, "Pong")
        
        # Game objects
        self.ball = None
        self.player_paddle = None
        self.opponent_paddle = None
        
        # Game state
        self.game_state = "START"  # START, PLAYING, GAME_OVER
        
        # Scores
        self.player_score = 0
        self.opponent_score = 0
        
        arcade.set_background_color(constants.BACKGROUND_COLOR)

    def setup(self):
        # Create game objects
        self.ball = Ball()
        self.player_paddle = Paddle(x=30, y=constants.WINDOW_HEIGHT/2, is_player=True)
        self.opponent_paddle = Paddle(x=constants.WINDOW_WIDTH-30, 
                                    y=constants.WINDOW_HEIGHT/2, 
                                    is_player=False)
        
        self.opponent_paddle.set_ball(self.ball)
        
        # Reset scores
        self.player_score = 0
        self.opponent_score = 0
        
        # Set initial game state
        self.game_state = "START"
    
    def on_draw(self):
        self.clear()
        
        # Create a sprite list and add our sprites
        sprite_list = arcade.SpriteList()
        sprite_list.append(self.ball.sprite)
        sprite_list.append(self.player_paddle.sprite)
        sprite_list.append(self.opponent_paddle.sprite)
        
        # Draw all sprites at once
        sprite_list.draw()
        
        # Draw scores
        arcade.draw_text(f"{self.player_score}", 
                        constants.WINDOW_WIDTH/4, 
                        constants.WINDOW_HEIGHT - 50,
                        arcade.color.YELLOW, 
                        24)
        arcade.draw_text(f"{self.opponent_score}", 
                        3*constants.WINDOW_WIDTH/4, 
                        constants.WINDOW_HEIGHT - 50,
                        arcade.color.GREEN, 
                        24)
        
        # Draw game state messages
        if self.game_state == "START":
            arcade.draw_text("Press SPACE to start", 
                            constants.WINDOW_WIDTH/2,
                            constants.WINDOW_HEIGHT/2,
                            arcade.color.BABY_BLUE,
                            24,
                            anchor_x="center")
        elif self.game_state == "GAME_OVER":
            arcade.draw_text("Game Over - Press SPACE to restart",
                            constants.WINDOW_WIDTH/2,
                            constants.WINDOW_HEIGHT/2,
                            arcade.color.ORANGE,
                            24,
                            anchor_x="center")
            

    def on_update(self, delta_time):
       if self.game_state == "PLAYING":
        # Update game objects
        self.ball.update()
        self.player_paddle.update()
        self.opponent_paddle.update()
        
        # Simple AI for opponent paddle
        if self.opponent_paddle.sprite.center_y < self.ball.sprite.center_y:
            self.opponent_paddle.move_up()
        elif self.opponent_paddle.sprite.center_y > self.ball.sprite.center_y:
            self.opponent_paddle.move_down()
        
        # Check for scoring
        if self.ball.sprite.right > constants.WINDOW_WIDTH:
            self.player_score += 1
            self.ball.reset()
        elif self.ball.sprite.left < 0:
            self.opponent_score += 1
            self.ball.reset()
        
        # Check for collisions with paddles
        if arcade.check_for_collision(self.ball.sprite, self.player_paddle.sprite):
            self.ball.sprite.left = self.player_paddle.sprite.right
            self.ball.speed_multiplier += 0.02  # Increase speed by 2%
            self.ball.change_x = abs(self.ball.change_x) * self.ball.speed_multiplier

        elif arcade.check_for_collision(self.ball.sprite, self.opponent_paddle.sprite):
            self.ball.sprite.right = self.opponent_paddle.sprite.left
            self.ball.speed_multiplier += 0.02  # Increase speed by 2%
            self.ball.change_x = -abs(self.ball.change_x) * self.ball.speed_multiplier

        # Check for game over
        if self.player_score >= constants.WINNING_SCORE or self.opponent_score >= constants.WINNING_SCORE:
            self.game_state = "GAME_OVER"
            
            
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.SPACE:
            if self.game_state == "START":
                self.game_state = "PLAYING"
            elif self.game_state == "GAME_OVER":
                self.setup()
                self.game_state = "PLAYING"
        
        if self.game_state == "PLAYING":
            if key == arcade.key.UP:
                self.player_paddle.move_up()
            elif key == arcade.key.DOWN:
                self.player_paddle.move_down()
                
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player_paddle.stop()

def main():
    window = PongGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
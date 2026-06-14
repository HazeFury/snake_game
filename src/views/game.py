import arcade
from core.food import Food
from core.snake import Snake
from core.grid import Grid
from views.game_over import GameOverView
from utils.handle_input import handle_input


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self, level: str):
        """
        Set up the application.
        """

        super().__init__()
        self.is_running: True = True
        self.is_game_over = False
        self.speed = 1

        self.grid: Grid = Grid(level)
        self.snake: Snake = Snake()
        self.food: Food = Food()

        self.window.set_size(self.grid.window_width, self.grid.window_height)
        self.window.center_window()
        self.background_color = arcade.color.WHITE

        self.grid.create_grid()
        self.grid.put_snake_on_grid(self.snake)
        self.food.generate_new_food(self.snake, self.grid)

        arcade.schedule(self.game_loop, self.speed)

    def game_loop(self, delta_time):
        """
        Move the snake and refresh the grid, then draw it. Also check if snake
        collision has collision with walls or himself.
        """
        self.snake.check_snake_collision()
        self.snake.move()

        if not self.snake.check_border_collision(
            self.grid.rows, self.grid.columns
                ) or not self.snake.check_snake_collision():
            self.is_running = False
            self.is_game_over = True
            return arcade.unschedule(self.game_loop)

        self.grid.reset_grid()
        self.grid.put_snake_on_grid(self.snake)
        self.food.generate_new_food(self.snake, self.grid)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        self.clear()

        # Draw the grid
        if self.is_running is True and self.is_game_over is False:
            self.grid.draw_grid()
        else:
            self.window.show_view(GameOverView(
                score=len(self.snake.body) - 4
                ))

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        handle_input(key, self.snake)

        if key == arcade.key.ESCAPE:
            self.is_running = not self.is_running
            if self.is_running is True:
                arcade.schedule(self.game_loop, self.speed)
            else:
                arcade.unschedule(self.game_loop)

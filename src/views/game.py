import arcade
from core.snake import Snake
from core.grid import Grid


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self, level: str):
        """
        Set up the application.
        """

        super().__init__()
        self.grid: Grid = Grid(level)
        self.snake: Snake = Snake()

        self.window.set_size(self.grid.window_width, self.grid.window_height)
        self.window.center_window()
        self.background_color = arcade.color.WHITE

        self.grid.create_grid()
        self.grid.put_snake_on_grid(self.snake)

        arcade.schedule(self.some_action, 1)
        # Unschedule
        # arcade.unschedule(self.some_action)

    def some_action(self, delta_time):
        self.snake.move()
        self.grid.reset_grid()
        self.grid.put_snake_on_grid(self.snake)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        self.clear()

        # Draw the grid
        self.grid.draw_grid()

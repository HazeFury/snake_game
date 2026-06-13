import arcade
from core.snake import Snake
from core.grid import Grid
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
        self.grid: Grid = Grid(level)
        self.snake: Snake = Snake()

        self.window.set_size(self.grid.window_width, self.grid.window_height)
        self.window.center_window()
        self.background_color = arcade.color.WHITE

        self.grid.create_grid()
        self.grid.put_snake_on_grid(self.snake)

        arcade.schedule(self.some_action, 1)

    def some_action(self, delta_time):
        self.snake.move()
        self.grid.reset_grid()
        self.grid.put_snake_on_grid(self.snake)
        print(self.is_running)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        self.clear()

        # Draw the grid
        if self.is_running is True:
            self.grid.draw_grid()
        # else:

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        handle_input(key, self.snake)

        if key == arcade.key.ESCAPE:
            self.is_running = not self.is_running
            if self.is_running is True:
                arcade.schedule(self.some_action, 1)
            else:
                arcade.unschedule(self.some_action)

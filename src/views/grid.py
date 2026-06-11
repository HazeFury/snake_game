import arcade
from utils.config_loader import GAME_CONFIG
from core.snake import Snake


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self, level: str):
        """
        Set up the application.
        """

        super().__init__()

        self.level = level
        self.snake = Snake()
        # Define the margin between each cell and the border
        self.margin = 1
        self.rows = GAME_CONFIG["levels"][self.level]["rows"]
        self.columns = GAME_CONFIG["levels"][self.level]["col"]
        self.cell_size = GAME_CONFIG["levels"][self.level]["cell_size"]

        self.window_width = \
            (self.cell_size + self.margin) * self.columns + self.margin
        self.window_height = \
            (self.cell_size + self.margin) * self.rows + self.margin

        self.window.set_size(self.window_width, self.window_height)
        self.window.center_window()

        self.grid = []
        for row in range(self.rows):
            # Add an empty array that will hold each cell in this row
            self.grid.append([])
            for column in range(self.columns):
                self.grid[row].append(0)  # Append a cell

        for i, snake_cell in enumerate(self.snake.body):
            x = snake_cell.get("x", 0)
            y = snake_cell.get("y", 0)

            if i == 0:
                self.grid[y][x] = 2
            else:
                self.grid[y][x] = 1

        self.background_color = arcade.color.WHITE

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        self.clear()

        # Draw the grid
        for row in range(self.rows):
            for column in range(self.columns):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                elif self.grid[row][column] == 2:
                    color = arcade.color.RED
                else:
                    color = arcade.color.BLACK

                x = (self.margin + self.cell_size) * column + self.margin + \
                    self.cell_size // 2
                y = (self.margin + self.cell_size) * row + self.margin + \
                    self.cell_size // 2

                # Draw the box
                arcade.draw_rect_filled(arcade.rect.XYWH(
                    x,
                    y,
                    self.cell_size,
                    self.cell_size
                    ), color
                    )

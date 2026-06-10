import arcade
import math
from utils.config_loader import GAME_CONFIG

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 1

# Set how many rows and columns we will have
ROW_COUNT = 8
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = ((1200 - MARGIN) / COLUMN_COUNT) - MARGIN
HEIGHT = ((800 - MARGIN) / ROW_COUNT) - MARGIN


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

        self.window_width = GAME_CONFIG["window"]["width"]
        self.window_height = GAME_CONFIG["window"]["height"]

        # Define the margin between each cell and the border
        self.margin = 1

        # Determine grid rows and columns based on the difficulty level
        self.rows = GAME_CONFIG["levels"][self.level]["rows"]
        # Aspect ratio of the window is 1.5 (1200/800)
        self.columns = self.rows

        self.cell_width = math.floor((self.window_width - self.margin) / self.columns) - self.margin
        self.cell_height = math.floor((self.window_height - self.margin) / self.rows) - self.margin

        self.cell_size = min(self.cell_width, self.cell_height)

        # --- MATH FIX START: Dimension and Centering ---
        # A unit box is `(cell_size + inner_margin)`. For C units, we have `C*unit`.
        # This covers the grid lines. We then need one final outer margin, and one initial outer margin.
        # Total drawn dimension = `init_outer_margin + C*(cell_size + inner_margin) + final_outer_margin`.
        # Total Container dimension to wrap the drawn grid perfectly should be:
        self.grid_width_px = 2 * self.margin + self.columns * (self.cell_size + self.margin)
        self.grid_height_px = 2 * self.margin + self.rows * (self.cell_size + self.margin)

        # Standard centering logic, now using correct robust dimensions.
        # offset = (window_dimension - grid_dimension) // 2
        self.x_offset = (self.window_width - self.grid_width_px) // 2
        self.y_offset = (self.window_height - self.grid_height_px) // 2

        # Drawing start point for cells
        # We start drawing from theContainer's origin, plus an initial margin.
        self.cell_drawing_start_x = self.x_offset + self.margin
        self.cell_drawing_start_y = self.y_offset + self.margin

        # Create a 2 dimensional array. A two-dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(self.rows):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(self.columns):
                self.grid[row].append(0)  # Append a cell

        self.background_color = arcade.color.WHITE

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        arcade.draw_rect_outline(
            arcade.rect.XYWH(
                self.x_offset, # Container origin
                self.y_offset,
                self.grid_width_px,
                self.grid_height_px
            ),
            color=arcade.color.RED,
            border_width=2
        )

        # Draw the grid
        for row in range(self.rows):
            for column in range(self.columns):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.BLACK

                # Standard XYWH origin is at (draw_origin_x + unit_w * col, draw_origin_y + unit_h * row)
                # We start drawing from theContainer's origin, plus an initial margin.
                x = (self.margin + self.cell_width) * column + self.margin + self.cell_width // 2
                y = (self.margin + self.cell_height) * row + self.margin + self.cell_height // 2

                # Draw the box
                arcade.draw_rect_filled(arcade.rect.XYWH(
                    x,
                    y,
                    self.cell_width,
                    self.cell_height
                    ), color
                    )

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (self.cell_width + self.margin))
        row = int(y // (self.cell_height + self.margin))

        print(f"({x}, {y}). Grid coordinates: ({row}, {column})")
        print(800 // self.cell_width)
        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < self.rows and column < self.columns:
            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

import arcade
from core.snake import Snake


def handle_input(key, snake: Snake, is_running: bool):
    """Called whenever a key is pressed. """

    if key == arcade.key.UP:
        snake.direction = "N"
    elif key == arcade.key.DOWN:
        snake.direction = "S"
    elif key == arcade.key.LEFT:
        snake.direction = "W"
    elif key == arcade.key.RIGHT:
        snake.direction = "E"
    # elif key == arcade.key.ESCAPE:
    #     is_running = not is_running

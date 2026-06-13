import arcade
from core.snake import Snake


def handle_input(key, snake: Snake):
    """Called whenever a key is pressed. """

    if key == arcade.key.UP and snake.direction != "S":
        snake.direction = "N"
    elif key == arcade.key.DOWN and snake.direction != "N":
        snake.direction = "S"
    elif key == arcade.key.LEFT and snake.direction != "E":
        snake.direction = "W"
    elif key == arcade.key.RIGHT and snake.direction != "W":
        snake.direction = "E"

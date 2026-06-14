import random
from core.grid import Grid
from core.snake import Snake


class Food:
    def __init__(self):
        self.current_food_coord: tuple[int, int] | None = None

    def generate_new_food(self, snake: Snake, grid: Grid) -> tuple[int, int]:
        toto = 0
        while 1:
            toto = 0
            y = random.randint(0, grid.rows - 1)
            x = random.randint(0, grid.columns - 1)
            for node in snake.body:
                if node["y"] == y and node["x"] == x:
                    toto = 1
                    continue
            if toto == 0:
                break
        grid.grid[y][x] = 3
        self.current_food_coord = (y, x)

class Snake:
    """Represent the snake and all his capabilities."""
    def __init__(self) -> None:
        self.body: list[dict[str, int]] = [
            {"x": 7, "y": 3},
            {"x": 7, "y": 4},
            {"x": 7, "y": 5},
            {"x": 7, "y": 6}
            ]
        self.last_direction: str = "N"

    def move(self) -> None:
        snake_head = self.body[0]
        if self.last_direction = "N":
            new_head = snake_head
            self.body.insert(0, snake_head["y"])
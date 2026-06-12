class Snake:
    """Represent the snake and all his capabilities."""
    def __init__(self) -> None:
        self.body: list[dict[str, int]] = [
            {"x": 7, "y": 3},
            {"x": 7, "y": 2},
            {"x": 7, "y": 1},
            {"x": 6, "y": 1}
            ]
        self.direction: str = "N"

    def move(self) -> None:
        x = self.body[0].get("x")
        y = self.body[0].get("y")
        new_head = {"x": x, "y": y}
        if self.direction == "N":
            new_head.update({"y": new_head.get("y") + 1})
        elif self.direction == "S":
            new_head.update({"y": new_head.get("y") - 1})
        elif self.direction == "W":
            new_head.update({"x": new_head.get("x") - 1})
        elif self.direction == "E":
            new_head.update({"x": new_head.get("x") + 1})

        self.body.insert(0, new_head)
        self.body.pop()

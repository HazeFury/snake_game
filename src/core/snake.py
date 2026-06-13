from itertools import groupby


class Snake:
    """Represent the snake and all his capabilities."""
    def __init__(self) -> None:
        self.body: list[dict[str, int]] = [
            {"x": 0, "y": 6},
            {"x": 0, "y": 5},
            {"x": 0, "y": 4},
            {"x": 0, "y": 3},
            {"x": 0, "y": 2},
            {"x": 0, "y": 1},
            {"x": 0, "y": 0}
            ]
        self.direction: str = "N"

    def check_border_collision(self, max_rows: int, max_cols: int) -> bool:
        """Check if the snake is currently out the map."""
        for node in self.body:
            if node["y"] < 0 or node["y"] >= max_rows:
                return False
            elif node["x"] < 0 or node["x"] >= max_cols:
                return False

        return True

    def check_snake_collision(self) -> bool:
        """Check if the snake is currently walking on himself."""
        coord_list: list[tuple[int, int]] = [
            (el["y"], el["x"]) for el in self.body
            ]
        coord_list.sort()
        grouped = groupby(coord_list)
        duplicates = [key for key, group in grouped if len(list(group)) > 1]
        if len(duplicates) > 0:
            return False
        else:
            return True

    def move(self) -> None:
        """Move the snake according to the current direction."""
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

"""Demonstrates general setup.

If Arcade and Python are properly installed, you can run this example with:
python -m arcade.examples.gui.0_basic_setup

Content:
- create a view manually creating UIManager and adding widgets
- create a second view extending UIView and adding widgets

"""

import arcade
from utils.config_loader import GAME_CONFIG
from views.menu import MenuView


def main():
    """Main function"""
    # Create a window class. This is what actually shows up on screen
    window_width = GAME_CONFIG["window"]["width"]
    window_height = GAME_CONFIG["window"]["height"]

    window = arcade.Window(
        title="Snake Game",
        width=window_width,
        height=window_height
        )
    window.show_view(MenuView())
    window.center_window()

    arcade.run()


if __name__ == "__main__":
    main()

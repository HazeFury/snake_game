"""Demonstrates general setup.

If Arcade and Python are properly installed, you can run this example with:
python -m arcade.examples.gui.0_basic_setup

Content:
- create a view manually creating UIManager and adding widgets
- create a second view extending UIView and adding widgets

"""

import arcade
from views.menu import MenuView


def main():
    """Main function"""
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(title="Snake Game", width=1200, height=800)
    window.set_location(x=800, y=1200)

    # Show the view on screen
    window.show_view(MenuView())

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()

import arcade
from arcade.gui import UIManager, UITextureButton, UIAnchorLayout, UIBoxLayout, UILabel
from views.grid import GameView

from utils.config_loader import GAME_CONFIG

# Preload textures, because they are mostly used multiple times,so they are not
# loaded multiple times
TEX_RED_BUTTON_NORMAL = arcade.load_texture(
    ":resources:gui_basic_assets/button/red_normal.png"
)
TEX_RED_BUTTON_HOVER = arcade.load_texture(
    ":resources:gui_basic_assets/button/red_hover.png"
)
TEX_RED_BUTTON_PRESS = arcade.load_texture(
    ":resources:gui_basic_assets/button/red_press.png"
)


class LevelView(arcade.View):
    """Uses the arcade.View and shows how to integrate UIManager."""

    def __init__(self):
        super().__init__()

        levels = GAME_CONFIG["levels"]

        # Create a UIManager
        self.ui = UIManager()

        # Create anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout())

        button_box = UIBoxLayout(space_between=100)

        button_box.add(
            UILabel(
                text="Choose the difficulty",
                font_size=30,
                text_color=arcade.color.WHITE,
            )
        )
        for level in levels.keys():
            current = button_box.add(
                UITextureButton(
                    text=level,
                    texture=TEX_RED_BUTTON_NORMAL,
                    texture_hovered=TEX_RED_BUTTON_HOVER,
                    texture_pressed=TEX_RED_BUTTON_PRESS,
                )
            )

            @current.event("on_click")
            def on_click(event, captured_level=level):
                self.window.show_view(GameView(level=captured_level))

        return_button = button_box.add(
            UITextureButton(
                text="Go back to menu",
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            )
        )

        from views.menu import MenuView

        @return_button.event("on_click")
        def on_click_exit(event):
            self.window.show_view(MenuView())

        anchor.add(button_box)

    def on_show_view(self) -> None:
        self.ui.enable()

    def on_hide_view(self) -> None:
        self.ui.disable()

    def on_draw(self):
        # Clear the screen
        self.clear(color=arcade.uicolor.GREEN_EMERALD)

        # Add draw commands that should be below the UI
        # ...

        self.ui.draw()

        # Add draw commands that should be on top of the UI (uncommon)
        # ...

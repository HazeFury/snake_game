import arcade
from utils.config_loader import GAME_CONFIG
from arcade.gui import (
    UIManager,
    UITextureButton,
    UIAnchorLayout,
    UIBoxLayout,
    UILabel
)

TEX_RED_BUTTON_NORMAL = arcade.load_texture(
    ":resources:gui_basic_assets/button/red_normal.png"
)
TEX_RED_BUTTON_HOVER = arcade.load_texture(
    ":resources:gui_basic_assets/button/red_hover.png"
)
TEX_RED_BUTTON_PRESS = arcade.load_texture(
    ":resources:gui_basic_assets/button/red_press.png"
)


class GameOverView(arcade.View):
    """Uses the arcade.View and shows how to integrate UIManager."""

    def __init__(self, score):
        super().__init__()

        window_width = GAME_CONFIG["window"]["width"]
        window_height = GAME_CONFIG["window"]["height"]

        self.window.set_size(window_width, window_height)
        self.window.center_window()

        self.ui = UIManager()

        anchor = self.ui.add(UIAnchorLayout())

        button_box = UIBoxLayout(space_between=80)

        button_box.add(
            UILabel(
                text="GAME OVER",
                font_size=50,
                text_color=arcade.color.WHITE,
            )
        )

        button_box.add(
            UILabel(
                text=f"Score : {score}",
                font_size=30,
                text_color=arcade.color.BLUE,
            )
        )

        play_again_button = button_box.add(
            UITextureButton(
                text="Play again",
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            )
        )

        from views.level_selection import LevelView

        @play_again_button.event("on_click")
        def on_click_play(event):
            self.window.show_view(LevelView())

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
        self.clear(color=arcade.uicolor.BLACK)
        self.ui.draw()

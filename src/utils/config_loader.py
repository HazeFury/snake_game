import json
from pathlib import Path
import sys


def get_application_root() -> Path:
    """
    Determine the root directory of the application.
    If the script is bundled by PyInstaller, it returns the directory
    containing the executable, allowing users to modify the external JSON.
    """
    if getattr(sys, "frozen", False):
        # Running as a compiled executable
        return Path(sys.executable).parent
    else:
        # Running in a standard development environment
        # Moves up from 'src/utils/config_loader.py' to the project root
        return Path(__file__).resolve().parent.parent.parent


# Define the absolute path to the configuration file
CONFIG_FILE_PATH = get_application_root() / "config.json"


def load_game_configuration() -> dict:
    """
    Read the config.json file from the disk and parse it.
    Returns a fallback dictionary if the file is missing or corrupted.
    """
    # Hardcoded fallback values to guarantee the game starts no matter what
    default_config = {
        "window": {"width": 1200, "height": 800},
        "levels": {
            "Easy": {"rows": 10},
            "Intermediate": {"rows": 20},
            "Hardcore": {"rows": 30},
        },
    }

    if not CONFIG_FILE_PATH.exists():
        print(
            f"Warning: Configuration file not found at {CONFIG_FILE_PATH}."
            " Using defaults."
        )
        return default_config

    try:
        with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as error:
        print(f"Error while reading configuration file: {error}")
        print("Falling back to default internal configuration.")
        return default_config


# Global configuration variable acting as a singleton in RAM
# Thanks to Python's module caching system, this setup runs exactly once
# upon the very first import.
GAME_CONFIG = load_game_configuration()

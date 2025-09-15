import pyfiglet
from rich.console import Console
from rich.text import Text
from rich.color import Color
from rich.color import blend_rgb

console = Console()

def gradient_text(text: str, start_color: str, end_color: str) -> Text:
    """
    Render text with a smooth gradient from start_color to end_color.
    """
    rich_text = Text()
    start = Color.parse(start_color).triplet
    end = Color.parse(end_color).triplet
    steps = max(len(text), 1)

    for i, char in enumerate(text):
        # Blend colors smoothly across the length of the string
        blend = blend_rgb(start, end, i / steps)
        hex_color = f"#{blend[0]:02x}{blend[1]:02x}{blend[2]:02x}"
        rich_text.append(char, style=f"bold {hex_color}")
    
    return rich_text

def show_banner(message: str):
    ascii_art = pyfiglet.figlet_format(message, font="bloody")
    for line in ascii_art.splitlines():
        console.print(gradient_text(line, "#FFD700", "#00FFFF"), justify="center")  # Gold → Cyan
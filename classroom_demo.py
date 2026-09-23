from __future__ import annotations

import os
import sys
import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk
import pygame


# Change these values to select another bundled resource or duration.
IMAGE_NAME = "classroom_slide.png"
AUDIO_NAME = "classroom_audio.wav"
DURATION_SECONDS = 10


def resource_path(filename: str) -> Path:
    """Return a resource path that works from source or a PyInstaller bundle."""
    bundle_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return bundle_dir / "assets" / filename


def close_program(window: tk.Tk) -> None:
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    finally:
        window.destroy()


def main() -> None:
    image_path = resource_path(IMAGE_NAME)
    audio_path = resource_path(AUDIO_NAME)

    if not image_path.is_file():
        raise FileNotFoundError(f"Missing image resource: {image_path}")
    if not audio_path.is_file():
        raise FileNotFoundError(f"Missing audio resource: {audio_path}")

    window = tk.Tk()
    window.title("Classroom demonstration")
    window.configure(background="black")
    window.attributes("-fullscreen", True)
    window.bind("<Escape>", lambda _event: close_program(window))
    window.bind("<Button-1>", lambda _event: close_program(window))

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    image = Image.open(image_path).convert("RGB")
    image.thumbnail((screen_width, screen_height), Image.Resampling.LANCZOS)
    displayed_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(window, image=displayed_image, background="black")
    image_label.pack(expand=True)

    # Starting playback after the window is mapped keeps the two starts close together.
    def start_media() -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(os.fspath(audio_path))
        pygame.mixer.music.play()

    window.after(50, start_media)
    window.after(DURATION_SECONDS * 1000, lambda: close_program(window))
    window.mainloop()


if __name__ == "__main__":
    main()
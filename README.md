# Classroom fullscreen demo

This is a harmless classroom demonstration: it shows one local image, starts one local audio file, and closes automatically after the configured duration.

## Files

- `classroom_demo.py`: complete source code
- `assets/classroom_slide.png`: bundled sample image
- `assets/classroom_audio.wav`: bundled sample audio
- `requirements.txt`: Python packages used for running and packaging
- `build_windows.bat`: Windows build helper

Edit `IMAGE_NAME`, `AUDIO_NAME`, or `DURATION_SECONDS` at the top of `classroom_demo.py` when choosing different files. Put replacement media in `assets/` and keep the names in sync. WAV and MP3 audio are supported by pygame; the sample uses WAV so it needs no codec-specific setup.

## Build on Windows

Install Python on the build computer only, open Command Prompt in this folder, and run:

```bat
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py -m PyInstaller --onefile --windowed --name ClassroomDemo --add-data "assets;assets" classroom_demo.py
```

The standalone file is `dist\ClassroomDemo.exe`. Python is not needed on the target computer. The program uses the PyInstaller bundle directory, so it also works when launched by double-clicking from another current directory.

Press `Esc` or click the image to close it early. The configured automatic close is 10 seconds by default.
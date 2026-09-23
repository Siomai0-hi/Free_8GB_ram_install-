 # Classroom fullscreen demo

The demo displays `assets/Aimr.jpg`, plays
`assets/universfield-male-horror-scream-08-352438.wav`, and closes after 10
seconds. Press `Esc` or click the image to close it early.

## Run from source

```text
py -m pip install -r requirements.txt
py classroom_demo.py
```

## Build on Windows

```text
py -m PyInstaller --onefile --windowed --name ClassroomDemo --add-data "assets;assets" classroom_demo.py
```

 The standalone file is created at `dist\ClassroomDemo.exe`.
Run `dist\ClassroomDemo.exe` on the target Windows computer.

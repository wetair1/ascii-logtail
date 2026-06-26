# Architecture

ascii-logtail is a tiny curses log viewer built with the Python standard library.

## Runtime flow

1. The app receives a log path from the command line.
2. `tail()` reads the last part of the file as bytes.
3. Bytes are decoded with replacement so broken log lines do not crash the app.
4. The curses UI redraws the visible window and handles scrolling.
5. Pressing `q` exits the app.

## Main parts

- `tail()` loads recent lines from the target log file.
- `draw()` owns the curses loop, scroll offset and refresh timing.
- Keyboard input controls scrolling and exit.

## Design rules

- Keep dependencies at zero.
- Keep file errors visible in the UI.
- Do not load huge logs fully into memory.
- Keep scrolling logic simple and predictable.
- Prefer readable polling over background file watchers.

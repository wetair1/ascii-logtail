# ascii-logtail

Tiny curses log tail viewer with ASCII terminal controls.

## Features

- Reads the end of a log file
- Auto-refreshes
- Scroll through recent lines
- Works with any text log path
- Pure Python stdlib

## Usage

```bash
python3 main.py
python3 main.py /var/log/syslog
python3 main.py ./app.log
```

## Controls

- `j` / Down: scroll down
- `k` / Up: scroll up
- `q`: quit

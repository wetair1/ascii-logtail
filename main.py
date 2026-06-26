#!/usr/bin/env python3
import curses, sys, os, time


def tail(path, n=200):
    try:
        with open(path, 'rb') as f:
            f.seek(0, os.SEEK_END); end = f.tell(); size = min(end, 8192)
            f.seek(-size, os.SEEK_END)
            return f.read().decode(errors='replace').splitlines()[-n:]
    except Exception as e:
        return [f'error: {e}']


def draw(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    path = sys.argv[1] if len(sys.argv) > 1 else '/var/log/syslog'
    top = 0
    while True:
        lines = tail(path)
        h, w = stdscr.getmaxyx()
        max_top = max(0, len(lines)-h+3)
        top = min(top, max_top)
        stdscr.erase()
        stdscr.addstr(0, 2, f'ASCII LOGTAIL: {path}  q quit  j/k scroll')
        view = lines[top:top+h-2]
        for i, line in enumerate(view, 2):
            stdscr.addstr(i, 0, line[:w-1])
        ch = stdscr.getch()
        if ch in (ord('q'), ord('Q')): break
        if ch in (ord('j'), curses.KEY_DOWN): top = min(max_top, top+1)
        if ch in (ord('k'), curses.KEY_UP): top = max(0, top-1)
        time.sleep(0.3)


if __name__ == '__main__':
    curses.wrapper(draw)

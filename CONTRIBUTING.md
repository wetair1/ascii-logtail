# Contributing

Thanks for improving ascii-logtail.

## Local setup

```bash
git clone https://github.com/wetair1/ascii-logtail.git
cd ascii-logtail
python3 main.py ./app.log
```

No external dependencies are required.

## Code style

- Keep the project pure Python stdlib.
- Prefer small readable functions.
- Keep the TUI usable on small terminals.
- Avoid blocking work inside the render loop.
- Keep log file errors visible but non-fatal.

## Checks

```bash
python3 -m py_compile main.py
```

## Commit style

Use short imperative messages, for example:

- `Add follow mode`
- `Fix scroll bounds`
- `Document controls`

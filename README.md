# Small Project: Notes CLI

A tiny Python command-line project to manage local notes.

## Features
- Add a note
- List all notes
- Delete a note by ID

## Run
```bash
python3 notes_app.py --help
```

## Usage
```bash
# Add a note
python3 notes_app.py add "Buy groceries"

# List notes
python3 notes_app.py list

# Delete note with id 1
python3 notes_app.py delete 1
```

Notes are stored in `notes.json` in the project root.

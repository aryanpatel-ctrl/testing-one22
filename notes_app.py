#!/usr/bin/env python3
"""A tiny notes CLI that stores data in a local JSON file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DATA_FILE = Path("notes.json")


def load_notes() -> list[dict[str, Any]]:
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
        if not isinstance(data, list):
            return []
        return data


def save_notes(notes: list[dict[str, Any]]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)


def next_id(notes: list[dict[str, Any]]) -> int:
    if not notes:
        return 1
    return max(int(note["id"]) for note in notes) + 1


def cmd_add(args: argparse.Namespace) -> None:
    notes = load_notes()
    note = {"id": next_id(notes), "text": args.text}
    notes.append(note)
    save_notes(notes)
    print(f"Added note #{note['id']}")


def cmd_list(_: argparse.Namespace) -> None:
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    for note in notes:
        print(f"{note['id']}: {note['text']}")


def cmd_delete(args: argparse.Namespace) -> None:
    notes = load_notes()
    filtered = [note for note in notes if int(note["id"]) != args.note_id]
    if len(filtered) == len(notes):
        print(f"Note #{args.note_id} not found.")
        return

    save_notes(filtered)
    print(f"Deleted note #{args.note_id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple notes manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("text", help="Text for the note")
    add_parser.set_defaults(func=cmd_add)

    list_parser = subparsers.add_parser("list", help="List all notes")
    list_parser.set_defaults(func=cmd_list)

    delete_parser = subparsers.add_parser("delete", help="Delete a note by ID")
    delete_parser.add_argument("note_id", type=int, help="Numeric note ID")
    delete_parser.set_defaults(func=cmd_delete)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

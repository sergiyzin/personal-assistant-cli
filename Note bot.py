from difflib import get_close_matches
import re


class Note:
    def __init__(self, text):
        self.text = text
        self.tags = self.extract_tags()

    def extract_tags(self):
        return re.findall(r"#\w+", self.text.lower())

    def edit(self, new_text):
        self.text = new_text
        self.tags = self.extract_tags()

    def matches_text(self, keyword):
        return keyword.lower() in self.text.lower()

    def matches_tag(self, tag):
        tag = tag.lower()
        if not tag.startswith("#"):
            tag = f"#{tag}"
        return tag in self.tags

    def __str__(self):
        return self.text


class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, text):
        self.notes.append(Note(text))
        return "Note added."

    def edit_note(self, index, new_text):
        if 0 <= index < len(self.notes):
            self.notes[index].edit(new_text)
            return "Note updated."
        return "Invalid note number."

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
            return "Note deleted."
        return "Invalid note number."

    def show_all_notes(self):
        if not self.notes:
            return "No notes available."
        return "\n".join(f"{i + 1}. {note}" for i, note in enumerate(self.notes))

    def search_notes(self, keyword):
        results = [
            f"{i + 1}. {note}"
            for i, note in enumerate(self.notes)
            if note.matches_text(keyword)
        ]
        if not results:
            return "No matching notes found."
        return "\n".join(results)

    def search_by_tag(self, tag):
        results = [
            f"{i + 1}. {note}"
            for i, note in enumerate(self.notes)
            if note.matches_tag(tag)
        ]
        if not results:
            return "No notes found with this tag."
        return "\n".join(results)


def suggest_command(command, commands):
    matches = get_close_matches(command, commands, n=1, cutoff=0.6)
    if matches:
        return f"Unknown command. Maybe you meant '{matches[0]}'?"
    return "Unknown command."


def parse_input(user_input):
    parts = user_input.strip().split(" ", 1)
    command = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""
    return command, args


def main():
    notes_manager = NotesManager()

    commands = [
        "add-note",
        "edit-note",
        "delete-note",
        "show-notes",
        "search-notes",
        "search-tag",
        "help",
        "close",
        "exit"
    ]

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter command: ").strip()

        if not user_input:
            print("Please enter a command.")
            continue

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "help":
            print(
                "Available commands:\n"
                "add-note <text>\n"
                "edit-note <number>; <new text>\n"
                "delete-note <number>\n"
                "show-notes\n"
                "search-notes <keyword>\n"
                "search-tag <tag>\n"
                "close / exit"
            )

        elif command == "add-note":
            if not args:
                print("Usage: add-note <text>")
            else:
                print(notes_manager.add_note(args.strip()))

        elif command == "edit-note":
            try:
                index_str, new_text = args.split(";", 1)
                index = int(index_str.strip()) - 1
                print(notes_manager.edit_note(index, new_text.strip()))
            except ValueError:
                print("Usage: edit-note <number>; <new text>")

        elif command == "delete-note":
            try:
                index = int(args.strip()) - 1
                print(notes_manager.delete_note(index))
            except ValueError:
                print("Usage: delete-note <number>")

        elif command == "show-notes":
            print(notes_manager.show_all_notes())

        elif command == "search-notes":
            if not args:
                print("Usage: search-notes <keyword>")
            else:
                print(notes_manager.search_notes(args.strip()))

        elif command == "search-tag":
            if not args:
                print("Usage: search-tag <tag>")
            else:
                print(notes_manager.search_by_tag(args.strip()))

        else:
            print(suggest_command(command, commands))


if __name__ == "__main__":
    main()
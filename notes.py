from validation import normalize_tag


# Цей описує одну нотатку
class Note:
    def __init__(self, note_id: int, text: str, tags=None):
        self.note_id = note_id

        self.text = text.strip()

        self.tags = []

        # якщо теги передані то додати їх
        if tags:
            for tag in tags:
                self.add_tag(tag)

    def add_tag(self, tag: str):
        tag = normalize_tag(tag)
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        tag = normalize_tag(tag)
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            raise ValueError("Tag not found.")

    def edit_text(self, new_text: str):
        new_text = new_text.strip()
        if not new_text:
            raise ValueError("Note text cannot be empty.")
        self.text = new_text

    # Чекінг чи підходить нотатка до пошукового запиту
    def matches(self, query: str) -> bool:
        query = query.lower()

        # Шукаємо у тексті нотатки
        if query in self.text.lower():
            return True

        # Шукаємо серед тегів
        for tag in self.tags:
            if query in tag.lower():
                return True

        return False

    # Чекінг чи має нотатка тег
    def has_tag(self, tag: str) -> bool:
        return normalize_tag(tag) in self.tags

    # Робе нотатки у словник для файлу
    def to_dict(self):
        return {
            "note_id": self.note_id,
            "text": self.text,
            "tags": self.tags,
        }

    # Робе нотатки зі словника при завантаженні
    @classmethod
    def from_dict(cls, data):
        return cls(
            note_id=data.get("note_id", 0),
            text=data.get("text", ""),
            tags=data.get("tags", []),
        )

    def __str__(self):
        tags_text = ", ".join(self.tags) if self.tags else "No tags"
        return f"ID: {self.note_id} | Text: {self.text} | Tags: {tags_text}"


# Це керує всіма нотатками
class NotesManager:
    def __init__(self):
        self.notes = []

        self.next_id = 1

    def add_note(self, text: str, tags=None):
        text = text.strip()
        if not text:
            raise ValueError("Note text cannot be empty.")

        note = Note(self.next_id, text, tags)
        self.notes.append(note)
        self.next_id += 1
        return note

    def get_note_by_id(self, note_id: int):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def delete_note(self, note_id: int):
        note = self.get_note_by_id(note_id)
        if not note:
            raise ValueError("Note not found.")
        self.notes.remove(note)

    def search_notes(self, query: str):
        return [note for note in self.notes if note.matches(query)]

    def search_by_tag(self, tag: str):
        tag = normalize_tag(tag)
        return [note for note in self.notes if note.has_tag(tag)]
    
    def edit_note(self, note_id: int, new_text: str):
        note = self.get_note_by_id(note_id)
        if not note:
            raise ValueError("Note not found.")
        note.edit_text(new_text)

    def sort_by_tags(self):
        return sorted(self.notes, key=lambda note: ",".join(note.tags))

    def all_notes(self):
        return self.notes

    def to_dict(self):
        return {
            "next_id": self.next_id,
            "notes": [note.to_dict() for note in self.notes],
        }

    # Тут робимо Notes Manager зі словника при отриманні з файлу
    @classmethod
    def from_dict(cls, data):
        manager = cls()
        manager.next_id = data.get("next_id", 1)
        manager.notes = [Note.from_dict(item) for item in data.get("notes", [])]
        return manager
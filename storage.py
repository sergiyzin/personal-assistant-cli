import json
from pathlib import Path

from contacts import AddressBook
from notes import NotesManager

# Це є папка для збереження даних у директорії юзера
DATA_DIR = Path.home() / ".personal_assistant"

# Це є Файл де будуть зберігатися контакти та нотатки
DATA_FILE = DATA_DIR / "assistant_data.json"

# Робе папки для збереження якщо немає
def ensure_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

# Зберегає контактів і нотаток у JSON файл
def save_data(address_book: AddressBook, notes_manager: NotesManager):
    ensure_storage()

    # Робить об'єкти у словники щоб зберегти
    data = {
        "contacts": address_book.to_dict(),
        "notes": notes_manager.to_dict(),
    }

    # Записує дані у файл
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_data():
    ensure_storage()

    # файл не існує - то повертає порожні об'єкти
    if not DATA_FILE.exists():
        return AddressBook(), NotesManager()

    try:
        # Читає JSON з файлу
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Рекавер AddressBook і NotesManager зі словників
        address_book = AddressBook.from_dict(data.get("contacts", {}))
        notes_manager = NotesManager.from_dict(data.get("notes", {}))

        return address_book, notes_manager

    # файл пошкоджений або сталася помилка — виводимо warning і повертаємо порожні дані
    except json.JSONDecodeError:
        print(f"Warning: corrupted JSON file: {DATA_FILE}")
        return AddressBook(), NotesManager()

    except OSError as error:
        print(f"Warning: cannot read file: {error}")
        return AddressBook(), NotesManager()

    except ValueError as error:
        print(f"Warning: invalid data format: {error}")
        return AddressBook(), NotesManager()
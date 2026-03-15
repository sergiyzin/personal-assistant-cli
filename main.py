import difflib

from storage import load_data, save_data

# Список всіх CLI команд
COMMANDS = [
    "help",
    "add-contact",
    "show-contacts",
    "find-contact",
    "delete-contact",
    "edit-contact-name",
    "add-phone",
    "edit-phone",
    "remove-phone",
    "set-email",
    "set-address",
    "set-birthday",
    "birthdays",
    "add-note",
    "show-notes",
    "find-note",
    "edit-note",
    "delete-note",
    "add-tag",
    "remove-tag",
    "find-tag",
    "sort-notes-tags",
    "exit",
]

# Показ довідки по командах
def print_help():
    print("\nAvailable commands:")
    print("  help")
    print("  add-contact")
    print("  show-contacts")
    print("  find-contact")
    print("  delete-contact")
    print("  edit-contact-name")
    print("  add-phone")
    print("  edit-phone")
    print("  remove-phone")
    print("  set-email")
    print("  set-address")
    print("  set-birthday")
    print("  birthdays")
    print("  add-note")
    print("  show-notes")
    print("  find-note")
    print("  edit-note")
    print("  delete-note")
    print("  add-tag")
    print("  remove-tag")
    print("  find-tag")
    print("  sort-notes-tags")
    print("  exit\n")

# Hint, якщо команда введена неправильно
def suggest_command(user_command: str):
    matches = difflib.get_close_matches(user_command, COMMANDS, n=1, cutoff=0.5)
    return matches[0] if matches else None

# Функція для показу необов'язкових даних
def input_optional(prompt):
    value = input(prompt).strip()
    return value

# Main функція програми
def main():
    # Load контакти та нотатки з файлів
    address_book, notes_manager = load_data()

    print("Welcome to Personal Assistant!")
    print("Type 'help' to see all commands.\n")

    # CLI цикл
    while True:
        command = input("Enter command: ").strip()

    def handle_help():
        print_help()

    def handle_add_contact():
        name = input("Name: ").strip()
        address = input_optional("Address (optional): ")
        phone = input_optional("Phone (optional): ")
        email = input_optional("Email (optional): ")
        birthday = input_optional("Birthday YYYY-MM-DD (optional): ")

        address_book.add_contact(
            name=name,
            address=address,
            phone=phone if phone else None,
            email=email,
            birthday=birthday,
        )
        save_data(address_book, notes_manager)
        print("Contact added.")

    def handle_show_contacts():
        contacts = address_book.all_contacts()
        if not contacts:
            print("No contacts.")
        else:
            for contact in contacts:
                print(contact)

    def handle_find_contact():
        query = input("Enter search text: ").strip()
        results = address_book.search_contacts(query)
        if not results:
            print("Nothing found.")
        else:
            for contact in results:
                print(contact)

    def handle_delete_contact():
        name = input("Enter contact name: ").strip()
        address_book.delete_contact(name)
        save_data(address_book, notes_manager)
        print("Contact deleted.")

    def handle_edit_contact_name():
        old_name = input("Old name: ").strip()
        new_name = input("New name: ").strip()
        address_book.edit_contact_name(old_name, new_name)
        save_data(address_book, notes_manager)
        print("Contact name updated.")

    def handle_add_phone():
        name = input("Contact name: ").strip()
        phone = input("New phone: ").strip()
        contact = address_book.get_contact(name)
        if not contact:
            print("Contact not found.")
        else:
            contact.add_phone(phone)
            save_data(address_book, notes_manager)
            print("Phone added.")

    def handle_edit_phone():
        name = input("Contact name: ").strip()
        old_phone = input("Old phone: ").strip()
        new_phone = input("New phone: ").strip()
        contact = address_book.get_contact(name)
        if not contact:
            print("Contact not found.")
        else:
            contact.edit_phone(old_phone, new_phone)
            save_data(address_book, notes_manager)
            print("Phone updated.")

    def handle_remove_phone():
        name = input("Contact name: ").strip()
        phone = input("Phone to remove: ").strip()
        contact = address_book.get_contact(name)
        if not contact:
            print("Contact not found.")
        else:
            contact.remove_phone(phone)
            save_data(address_book, notes_manager)
            print("Phone removed.")

    def handle_set_email():
        name = input("Contact name: ").strip()
        email = input("New email: ").strip()
        contact = address_book.get_contact(name)
        if not contact:
            print("Contact not found.")
        else:
            contact.set_email(email)
            save_data(address_book, notes_manager)
            print("Email updated.")

    def handle_set_address():
        name = input("Contact name: ").strip()
        address = input("New address: ").strip()
        contact = address_book.get_contact(name)
        if not contact:
            print("Contact not found.")
        else:
            contact.set_address(address)
            save_data(address_book, notes_manager)
            print("Address updated.")

    def handle_set_birthday():
        name = input("Contact name: ").strip()
        birthday = input("Birthday YYYY-MM-DD: ").strip()
        contact = address_book.get_contact(name)
        if not contact:
            print("Contact not found.")
        else:
            contact.set_birthday(birthday)
            save_data(address_book, notes_manager)
            print("Birthday updated.")

    def handle_birthdays():
        days = int(input("Show birthdays within how many days?: ").strip())
        results = address_book.upcoming_birthdays(days)
        if not results:
            print("No upcoming birthdays.")
        else:
            for contact, days_left in results:
                print(f"{contact.name} - in {days_left} day(s), date: {contact.birthday}")

    def handle_add_note():
        text = input("Note text: ").strip()
        raw_tags = input_optional("Tags separated by commas (optional): ")
        tags = [tag.strip() for tag in raw_tags.split(",") if tag.strip()] if raw_tags else []
        note = notes_manager.add_note(text, tags)
        save_data(address_book, notes_manager)
        print(f"Note added with ID {note.note_id}.")

    def handle_show_notes():
        notes = notes_manager.all_notes()
        if not notes:
            print("No notes.")
        else:
            for note in notes:
                print(note)

    def handle_find_note():
        query = input("Enter search text: ").strip()
        results = notes_manager.search_notes(query)
        if not results:
            print("Nothing found.")
        else:
            for note in results:
                print(note)

    def handle_edit_note():
        note_id = int(input("Note ID: ").strip())
        new_text = input("New text: ").strip()
        notes_manager.edit_note(note_id, new_text)
        save_data(address_book, notes_manager)
        print("Note updated.")

    def handle_delete_note():
        note_id = int(input("Note ID: ").strip())
        notes_manager.delete_note(note_id)
        save_data(address_book, notes_manager)
        print("Note deleted.")

    def handle_add_tag():
        note_id = int(input("Note ID: ").strip())
        tag = input("Tag: ").strip()
        note = notes_manager.get_note_by_id(note_id)
        if not note:
            print("Note not found.")
        else:
            note.add_tag(tag)
            save_data(address_book, notes_manager)
            print("Tag added.")

    def handle_remove_tag():
        note_id = int(input("Note ID: ").strip())
        tag = input("Tag to remove: ").strip()
        note = notes_manager.get_note_by_id(note_id)
        if not note:
            print("Note not found.")
        else:
            note.remove_tag(tag)
            save_data(address_book, notes_manager)
            print("Tag removed.")

    def handle_find_tag():
        tag = input("Tag: ").strip()
        results = notes_manager.search_by_tag(tag)
        if not results:
            print("Nothing found.")
        else:
            for note in results:
                print(note)

    def handle_sort_notes_tags():
        notes = notes_manager.sort_by_tags()
        if not notes:
            print("No notes.")
        else:
            for note in notes:
                print(note)

    commands = {
        "help": handle_help,
        "add-contact": handle_add_contact,
        "show-contacts": handle_show_contacts,
        "find-contact": handle_find_contact,
        "delete-contact": handle_delete_contact,
        "edit-contact-name": handle_edit_contact_name,
        "add-phone": handle_add_phone,
        "edit-phone": handle_edit_phone,
        "remove-phone": handle_remove_phone,
        "set-email": handle_set_email,
        "set-address": handle_set_address,
        "set-birthday": handle_set_birthday,
        "birthdays": handle_birthdays,
        "add-note": handle_add_note,
        "show-notes": handle_show_notes,
        "find-note": handle_find_note,
        "edit-note": handle_edit_note,
        "delete-note": handle_delete_note,
        "add-tag": handle_add_tag,
        "remove-tag": handle_remove_tag,
        "find-tag": handle_find_tag,
        "sort-notes-tags": handle_sort_notes_tags,
    }

    # CLI цикл
    while True:
        command = input("Enter command: ").strip()

        try:
            if command == "exit":
                save_data(address_book, notes_manager)
                print("Goodbye!")
                break

            handler = commands.get(command)

            if handler:
                handler()
            else:
                suggestion = suggest_command(command)
                if suggestion:
                    print(f"Unknown command. Maybe you meant: {suggestion}")
                else:
                    print("Unknown command. Type 'help'.")

        except ValueError as error:
            print(f"Error: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")
# Вхід у програму
if __name__ == "__main__":
    main()
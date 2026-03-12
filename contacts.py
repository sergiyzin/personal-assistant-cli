# Імпорт модулів для дат
from datetime import datetime, date

# Імпорт функції перевірки даних з validation.py
from validation import (
    validate_name,
    validate_phone,
    validate_email,
    validate_birthday,
    validate_address,
)


# Опис контакту у адрес. книзі
class Contact:
    def __init__(self, name, address="", phones=None, email="", birthday=""):
        self.name = validate_name(name)
        self.address = address.strip() if address else ""
        self.phones = phones if phones else []
        self.email = email.strip() if email else ""
        self.birthday = birthday.strip() if birthday else ""

    # Додає телефон
    def add_phone(self, phone: str):
        phone = validate_phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)

    # Видаляє тел.
    def remove_phone(self, phone: str):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone not found.")

    # Редагує тел.
    def edit_phone(self, old_phone: str, new_phone: str):
        # Перевка чи існує старий номер
        if old_phone not in self.phones:
            raise ValueError("Old phone not found.")

        new_phone = validate_phone(new_phone)

        # Заміна номера
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def set_email(self, email: str):
        self.email = validate_email(email)

    def set_birthday(self, birthday: str):
        self.birthday = validate_birthday(birthday)

    def set_address(self, address: str):
        self.address = validate_address(address)

    def matches(self, query: str) -> bool:
        query = query.lower()

        # Пошук по імені ..
        if query in self.name.lower():
            return True

        if self.address and query in self.address.lower():
            return True

        if self.email and query in self.email.lower():
            return True

        for phone in self.phones:
            if query in phone.lower():
                return True

        if self.birthday and query in self.birthday.lower():
            return True

        return False

    # Вичислити скільки залишиль до наступного ДН
    def days_to_birthday(self):
        if not self.birthday:
            return None

        today = date.today()
        bday = datetime.strptime(self.birthday, "%Y-%m-%d").date()

        try:
            next_birthday = date(today.year, bday.month, bday.day)
        except ValueError:
            # Feb 29 і поточний рік невисокосний
            next_birthday = date(today.year, 3, 1)

        if next_birthday < today:
            try:
                next_birthday = date(today.year + 1, bday.month, bday.day)
            except ValueError:
                next_birthday = date(today.year + 1, 3, 1)

        return (next_birthday - today).days

    #  Щоб зберегти у файл Контакт робимо у словник
    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "phones": self.phones,
            "email": self.email,
            "birthday": self.birthday,
        }

    # Креатування контакту зі словника щоб завантажити з файлу
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", ""),
            address=data.get("address", ""),
            phones=data.get("phones", []),
            email=data.get("email", ""),
            birthday=data.get("birthday", ""),
        )

    # Правильний вигляд контакту
    def __str__(self):
        phones_text = ", ".join(self.phones) if self.phones else "No phones"
        email_text = self.email if self.email else "No email"
        birthday_text = self.birthday if self.birthday else "No birthday"
        address_text = self.address if self.address else "No address"

        return (
            f"Name: {self.name} | "
            f"Phones: {phones_text} | "
            f"Email: {email_text} | "
            f"Birthday: {birthday_text} | "
            f"Address: {address_text}"
        )


# Відповідає за управління всією книгою контактів
class AddressBook:
    def __init__(self):
        # Словник контактів
        self.contacts = {}

    def add_contact(self, name, address="", phone=None, email="", birthday=""):
        name = validate_name(name)

        # Перевірка чи є такий ж контакт
        if name in self.contacts:
            raise ValueError("Contact already exists.")

        contact = Contact(name=name)

        if address:
            contact.set_address(address)

        if phone:
            contact.add_phone(phone)

        if email:
            contact.set_email(email)

        if birthday:
            contact.set_birthday(birthday)

        self.contacts[name] = contact

    def get_contact(self, name: str):
        return self.contacts.get(name)

    def delete_contact(self, name: str):
        if name in self.contacts:
            del self.contacts[name]
        else:
            raise ValueError("Contact not found.")

    def search_contacts(self, query: str):
        result = []

        for contact in self.contacts.values():
            if contact.matches(query):
                result.append(contact)

        return result

    def edit_contact_name(self, old_name: str, new_name: str):
        if old_name not in self.contacts:
            raise ValueError("Contact not found.")

        new_name = validate_name(new_name)

        if new_name in self.contacts and new_name != old_name:
            raise ValueError("New contact name already exists.")

        contact = self.contacts[old_name]
        contact.name = new_name

        self.contacts[new_name] = contact

        if new_name != old_name:
            del self.contacts[old_name]

    # Получити список найближчих ДН
    def upcoming_birthdays(self, days: int):
        result = []

        for contact in self.contacts.values():
            days_left = contact.days_to_birthday()

            if days_left is not None and days_left <= days:
                result.append((contact, days_left))

        # Сортуфання списоку за кількістю днів до ДН
        result.sort(key=lambda item: item[1])

        return result

    def all_contacts(self):
        return list(self.contacts.values())

    def to_dict(self):
        return {name: contact.to_dict() for name, contact in self.contacts.items()}

    # Робить AddressBook з словника
    @classmethod
    def from_dict(cls, data):
        book = cls()

        for name, contact_data in data.items():
            book.contacts[name] = Contact.from_dict(contact_data)

        return book
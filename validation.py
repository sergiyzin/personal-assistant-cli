import re
from datetime import datetime


# Чекінг імені
def validate_name(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    return name


# Чекінг номера телефона
def validate_phone(phone: str) -> str:
    phone = phone.strip()
    cleaned = re.sub(r"[^\d+]", "", phone)

    # Правильні формати:
    # +380XXXXXXXXX, 380XXXXXXXXX, 10-15 цифр
    if re.fullmatch(r"\+?\d{10,15}", cleaned):
        return cleaned

    raise ValueError("Invalid phone number format.")


# Чекінг email
def validate_email(email: str) -> str:
    email = email.strip()
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if re.fullmatch(pattern, email):
        return email
    raise ValueError("Invalid email format.")


# Чекінг ДН у форматі YYYY-MM-DD
def validate_birthday(date_str: str) -> str:
    date_str = date_str.strip()
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("Birthday must be in YYYY-MM-DD format.")


# Чекінг адреси
def validate_address(address: str) -> str:
    address = address.strip()
    if not address:
        raise ValueError("Address cannot be empty.")
    return address


# Це є за для нотаток
def normalize_tag(tag: str) -> str:
    tag = tag.strip().lower()
    if not tag:
        raise ValueError("Tag cannot be empty.")
    return tag
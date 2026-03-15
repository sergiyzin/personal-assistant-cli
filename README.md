# Personal Assistant CLI
Командний фінальний проєкт команди **Team 4** для курсу
**Python Programming: Foundations and Best Practices**.

**Personal Assistant CLI** — це консольний застосунок для роботи з контактами та нотатками.  
Програма дозволяє зберігати контакти, телефони, email, адреси, дати народження, а також створювати нотатки з тегами та шукати їх.  
Дані зберігаються локально у JSON-файлі, тому не втрачаються після перезапуску програми.

---

# Функціонал
Програма дозволяє робити наступне:

### Контакти
- додавання контакту
- редагування імені контакту
- додавання телефону
- редагування телефону
- видалення телефону
- збереження email
- збереження адреси
- додавання дати народження
- пошук контактів
- видалення контактів
- перегляд усіх контактів
- перегляд найближчих днів народження

### Нотатки
- створення нотатки
- редагування нотатки
- видалення нотатки
- пошук нотаток
- додавання тегів
- видалення тегів
- пошук нотаток за тегами
- сортування нотаток за тегами

### Робота з даними
- автоматичне збереження даних
- автоматичне завантаження при запуску
- обробка помилок читання JSON
- валідація телефону, email, дати народження та тегів

---

## Технології
Проєкт реалізований з використанням:

- Python 3
- Object-Oriented Programming
- JSON для збереження даних
- CLI (Command Line Interface)
- Git та GitHub для командної розробки

---
## Вимоги
Проєкт використовує лише стандартну бібліотеку Python.  
Зовнішні залежності не потрібні.

---
## Встановлення
### 1. Клонувати репозиторій
git clone https://github.com/sergiyzin/personal-assistant-cli.git
cd personal-assistant-cli

---

# Створення та запуску віртуального середовища
## Windows
python -m venv .venv
.venv\Scripts\activate

## macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

## Запуск програма
python3 main.py

## Основні команди
help
add-contact
show-contacts
find-contact
delete-contact
edit-contact-name
add-phone
edit-phone
remove-phone
set-email
set-address
set-birthday
birthdays
add-note
show-notes
find-note
edit-note
delete-note
add-tag
remove-tag
find-tag
sort-notes-tags
exit

## Збереження даних
Програма зберігає всі дані локально у JSON-файлі.
Контакти та нотатки автоматично завантажуються при запуску та зберігаються після змін.

# Структура проєкту з описом 
personal-assistant-cli
│
├── main.py # основний CLI та обробка команд
├── contacts.py # моделі контактів (Contact, AddressBook)
├── notes.py # модель нотаток та менеджер нотаток
├── storage.py # збереження і завантаження JSON
├── validation.py # перевірка телефонів, email та інших даних
├── requirements.txt інформація про залежності проєкту
└── README.md

# Команда
Проєкт виконаний командою Team 4
у межах курсу Python Programming: Foundations and Best Practices.

Team Lead: Sergiy Zinkivsky
Scrum Master: Solomiia Zubar
Developer: Dmytro Surov
Developer: Denys Musich
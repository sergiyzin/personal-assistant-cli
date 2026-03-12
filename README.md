# personal-assistant-cli
CLI Personal Assistant – Python course team project




2.Notes Module
Overview

The Notes module is part of the console assistant project.
It allows users to create, manage, edit, and search personal notes directly from the command line.
Each note contains text and may include hashtags that can be used for searching and organizing notes.
The module supports the following functionality:

Creating notes
Editing notes
Deleting notes
Viewing all notes
Searching notes by text
Searching notes by hashtags
Intelligent command suggestion for mistyped commands

Note Model
The Note class represents a single note.

Each note contains:
note text
extracted hashtags (tags)
Hashtags are automatically extracted from the note text using a regular expression.

Example:
Buy milk and bread #shopping #home

Extracted tags:
#shopping
#home

Notes Manager
The NotesManager class manages all notes and provides the following methods:

Add note
Creates a new note and stores it in the notes list.
add-note <text>

Example:
add-note Buy milk and bread #shopping

Edit note
Updates an existing note using its number.
edit-note <number>; <new text>

Example:
edit-note 1; Buy milk, bread and apples #shopping

Delete note
Removes a note by its number.
delete-note <number>

Example:
delete-note 2

Show all notes
Displays all stored notes with numbering.
show-notes

Example output:
1. Buy milk and bread #shopping
2. Prepare weekly report #work

Search notes by keyword
Finds notes that contain a specific word.
search-notes <keyword>

Example:
search-notes milk
Search notes by hashtag

Finds notes containing a specific hashtag.
search-tag <tag>

Example:
search-tag #work
The hashtag may also be entered without the # symbol.

Example:
search-tag work

Intelligent Command Suggestion
If a user enters an unknown command, the assistant attempts to suggest the closest valid command using the difflib library.

Example:
add-not Buy milk

Output:
Unknown command. Maybe you meant 'add-note'?

Technologies Used
Python 3

re – hashtag extraction using regular expressions
difflib – intelligent command suggestions

Example Session
add-note Buy milk and bread #home
Note added.

add-note Prepare weekly report #work
Note added.

show-notes
1. Buy milk and bread #home
2. Prepare weekly report #work

search-tag #home
1. Buy milk and bread #home

edit-note 1; Buy milk, bread and apples #home
Note updated.

delete-note 2
Note deleted.
Summary

The Notes module provides a simple and efficient way to manage notes within the console assistant.
It supports searching, editing, and organizing notes using hashtags while maintaining a clean and minimal command-line interface.

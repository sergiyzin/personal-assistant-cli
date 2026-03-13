from setuptools import setup

setup(
    name="personal-assistant-cli",
    version="0.1",
    description="CLI Personal Assistant for contacts and notes",
    py_modules=[
        "main",
        "contacts",
        "notes",
        "storage",
        "validation",
    ],
    entry_points={
        "console_scripts": [
            "personal-assistant=main:main",
        ]
    },
)
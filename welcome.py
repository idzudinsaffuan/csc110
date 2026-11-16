"""CSC110/111: Welcome File

Welcome! This is a sample Python file that you should be able to run after you
have completed the steps in the CSC110/111 Software Installation Guide.

To run this file in VS Code, open this file and click the play button in the
top-right corner of the editor. If VS Code asks you to select a Python
interpreter, choose Python 3.13.14.

You can also run this file from the VS Code terminal:

Windows:
    python welcome.py

macOS:
    python3 welcome.py
"""

MY_NAME = 'Idzudin'


def greet(name: str) -> str:
    """Return a welcome message for the given person.

    >>> greet('Strawberry')
    'Hello, Strawberry! Welcome to CSC110/111. Hope you have a great time this term. :)'
    """
    return (f'Hello, {name}! Welcome to CSC110/111. ' +
            'Hope you have a great time this term. :)')


if __name__ == '__main__':
    print(greet(MY_NAME))

# AirBnB Clone

## Description

The AirBnB Clone project is a web application project that recreates some of the core functionality of the AirBnB platform.

The project is developed step by step, starting with a command interpreter and data models, followed by web static pages and database storage.

## The Command Interpreter

The command interpreter is a console application that allows users to interact with the application's objects.

It will allow users to:

- Create new objects
- Display objects
- Update objects
- Destroy objects
- Display the number of objects

### How to start it

Run:

    ./console.py

### How to use it

Once the console is running, commands can be entered at the prompt:

    (hbnb)

For example:

    (hbnb) create BaseModel
    (hbnb) show BaseModel <id>
    (hbnb) all
    (hbnb) update BaseModel <id> name "My first model"
    (hbnb) destroy BaseModel <id>
    (hbnb) quit

### Examples

    $ ./console.py
    (hbnb) help
    (hbnb) create BaseModel
    (hbnb) all
    (hbnb) quit

## Project Structure

- `models/` — contains the classes used in the project.
- `tests/` — contains unit tests for the project.
- `console.py` — the entry point for the command interpreter.
- `models/base_model.py` — defines the base class for project models.

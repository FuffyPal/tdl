# To-Do List Application Plan

This document contains the architecture, file tree, and development phases for the TOML-based To-Do List application to be developed with Python.

## File Tree

The following structure will be used to make your project modular and manageable:

```text
to-do-list/
├── src/
│   ├── __init__.py
│   ├── main.py          # Main entry point of the application (where commands are received)
│   ├── todo.py          # ToDo business logic (Add, Remove, Update tasks)
│   └── storage.py       # TOML file read/write operations
├── data/
│   └── todos.toml       # Database file where tasks will be saved
├── requirements.txt     # Dependencies (e.g., tomli-w or toml)
└── README.md            # Project description and user manual
```

## Phases

### Phase 1: Basic Setup and Data Layer (Storage)
- Creating the required folder structure (`src/`, `data/`) for the project.
- Selecting appropriate libraries for TOML read/write operations with Python (Standard library `tomllib` is available for reading in Python 3.11, an external module will be needed for writing).
- Creating functions within the `storage.py` module to smoothly read the `todos.toml` file and write new content to the file.

### Phase 2: Task Business Logic (To-Do Logic)
- Writing main task management functions in the `todo.py` file:
  - **Add**: Adding a new task to the list.
  - **Remove**: Deleting a task by its title or unique ID (sequence number-based).
  - **Update**: Updating a task as "Tick" (✔) or "Cross" (✖) (Assigning Completed or Not Completed status).

### Phase 3: User Interface (CLI Integration)
- A detailed Command Line Interface will be added into `main.py` using `argparse`.
- The application will support the following arguments and their shortcuts:
  - `-h` or `--help`: Shows the help menu and command usages.
  - `-a` or `--add`: Adds a new To-Do item. (e.g., `python src/main.py -a "Buy bread"`)
  - `-r` or `--remove`: Deletes a specified task by its ID or name. (e.g., `python src/main.py -r 1`)
  - `-u` or `--update`: Updates the completion status of a task.
    - If it takes a `+` parameter, it marks the task with a tick (✔) (completed). (e.g., `python src/main.py -u 1 +`)
    - If it takes a `-` parameter, it marks the task with a cross (✖) (not completed). (e.g., `python src/main.py -u 1 -`)
  - `-l` or `--list`: Lists all current tasks along with their status emojis (✔, ✖). (e.g., `python src/main.py -l`)
- Values entered by the user from the console will be parsed and passed to the relevant methods in the `todo.py` logic module.

### Phase 4: Testing and Validation
- Testing each functionality (verifying the correctness of the TOML table after adding data, etc.).
- Printing appropriate warnings for situations such as user data errors and file not found (Error Handling).

## User Review Required
This is the plan in broad strokes. I have specifically designed an application that will run via the **CLI** (Command Line Interface). If the plan is suitable for you, you can give your approval; if there are other features or details you want to modify or add, please let me know.

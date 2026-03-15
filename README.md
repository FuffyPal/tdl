# To-Do List CLI

A simple, efficient, and modular Command Line Interface (CLI) To-Do List application written in Python. It uses a TOML file for local data storage, ensuring that your tasks are kept in a readable and easily manageable format without requiring a complex database setup.

## Features

- **Add Tasks:** Quickly add new tasks to your to-do list from the command line.
- **Remove Tasks:** Delete tasks using their unique numerical ID.
- **Update Status:** Easily mark your tasks as completed (✔) or not completed (✖).
- **List Tasks:** View all your pending and completed tasks along with their current completion status.
- **Persistent Storage:** All tasks are securely saved in a TOML file (`data/tasks.toml`), meaning your data persists across sessions.

## Project Structure

```text
to-do-list/
├── main.py              # Main entry point of the CLI application
├── src/
│   ├── todo.py          # Core business logic for task management
│   └── storage.py       # Handles reading from and writing to the TOML file
├── data/
│   └── tasks.toml       # The local database file where tasks are saved
├── requirements.txt     # Python dependencies
├── task.md              # Project task and progress tracking
└── implementation_plan.md # Details the architecture and development phases
```

## Requirements

- **Python 3.11+** is recommended (since it relies on `tomllib` which is built-in for Python 3.11+).
- **tomli-w**: Used for writing data back to the TOML file.

## Installation

1. **Clone or Download the Repository:**
   Navigate to the project directory in your terminal.

2. **Set up a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install Dependencies:**
   Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The application is run from the command line using `main.py`. Here are the available commands:

### Help
To view all available commands and their usage explanations:
```bash
python main.py -h
# or
python main.py --help
```

### Add a Task
Add a new task to your list using the `-a` or `--add` argument:
```bash
python main.py -a "Buy groceries"
python main.py --add "Read a book"
```

### List Tasks
View all your current tasks, showing their ID and completion status using the `-l` or `--list` argument:
```bash
python main.py -l
```

### Update a Task
Update the status of a specific task using its ID. 
- Use the `+` operator to mark a task as completed (✔)
- Use the `-` operator to mark it as not completed (✖)
```bash
# Mark task #1 as completed
python main.py -u 1 +

# Mark task #1 as not completed
python main.py -u 1 -
```

### Remove a Task
Delete a task completely from your list using its ID with the `-r` or `--remove` argument:
```bash
python main.py -r 1
```

## Development and Architecture

This project was developed following a modular 4-phase plan:
1. **Basic Setup and Data Layer:** Configuring the project structure, dependency management, and TOML read/write operations (`storage.py`).
2. **Task Logic:** Implementing the core CRUD functions in `todo.py`.
3. **User Interface:** Building the robust CLI interface with the standard `argparse` library in `main.py`.
4. **Testing and Validation:** Ensuring strict error handling, handling edge cases (like non-existent tasks), and accurate data persistence.

For detailed information regarding the initial plan and feature roadmap, refer to the `implementation_plan.md` and `task.md` files.

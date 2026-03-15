# To-Do List Project Tasks

- [x] Phase 1: Basic Setup and Data Layer (Storage)
  - [x] Create project directory structure
  - [x] Determine required libraries (toml, etc.) and create `requirements.txt`
  - [x] Write `storage.py` module to communicate (read/write) with the TOML file
- [x] Phase 2: Task Logic (To-Do Logic)
  - [x] Create `todo.py` and construct the basic data structure (Task)
  - [x] Integrate `add` function (adding a task)
  - [x] Integrate `remove` function (deleting a task)
  - [x] Integrate `update` function (updating ✔ / ✖ status)
- [x] Phase 3: User Interface (CLI Integration)
  - [x] Define command line arguments in `main.py` using `argparse`:
    - [x] `-h, --help` (Help menu)
    - [x] `-a, --add` (Add a new task)
    - [x] `-r, --remove` (Delete a task)
    - [x] `-u, --update` (Update tick/cross status by taking `+` or `-`)
    - [x] `-l, --list` (List tasks)
  - [x] Write list display function and support it with emojis (✔, ✖)
  - [x] Connect arguments to background `todo.py` functions
- [x] Phase 4: Testing and Validation
  - [x] Test basic scenarios
  - [x] Check error handling mechanisms (trying to delete a non-existent task, etc.)

- [ ] Phase 5: Graphical User Interface (GTK4+ & libadwaita)
  - [ ] Set up PyGObject and libadwaita dependencies
  - [ ] Design the main cross-platform application window with a HeaderBar
  - [ ] Create UI components (Task list, Add button, status toggles)
  - [ ] Connect UI signals directly to the `todo.py` logic
  - [ ] Prepare the application for cross-platform distribution

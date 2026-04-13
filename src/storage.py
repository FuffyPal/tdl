import tomlkit

file_path = "data/tasks.toml"

def load():
    try :
        with open(file_path, "r", encoding="utf-8") as f:
            tasks = tomlkit.load(f)
    except FileNotFoundError:
        tasks = tomlkit.document()
        tasks.add("tasks", tomlkit.table())
        with open(file_path, "x", encoding="utf-8") as f:
            tomlkit.dump(tasks, f)
    return tasks

def save(key, data):
    data['tasks'][key] = ""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(tomlkit.dumps(data))
    print(key + " " + "added to the list")

def update(key, new_value, data):
    data['tasks'][key] = new_value
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(tomlkit.dumps(data))
    print(key + " " + "updated to the list")

def remove(key, data):
    """
    Deletes the specified key from the TOML file.
    """
    try:
        target = data['tasks']

        if key in target:
            target.pop(key)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(tomlkit.dumps(data))
            print(f"'{key}' successfully deleted.")
        else:
            print(f"Warning: '{key}' not found, no deletion performed.")

    except Exception as e:
        print(f"An error occurred: {e}")
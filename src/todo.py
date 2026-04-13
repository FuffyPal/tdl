
def add():
    key = input("Enter the task: ")
    return key

def remove():
    key = input("Enter the task to remove: ")
    return key

def update():
    key = input("Enter the task to update: ")
    new_value = input("Enter the new value: ")
    cleaned_value = "".join([char for char in new_value if not char.isdigit()]).lower()
    return key, cleaned_value
def list(data):
    tasks = data.get("tasks", {})
    
    completed = []      
    incomplete = []      
    pending = []       

    for task_name, status in tasks.items():
        if status == "true":
            completed.append(f"✅ {task_name}")
        elif status == "false":
            incomplete.append(f"❌ {task_name}")
        else:
            pending.append(f"🔘 {task_name}")

    print("📋 TASK STATUS REPORT")
    print("-" * 30)
    
    print(f"\n🟢 COMPLETED ({len(completed)}):")
    print("\n".join(completed) if completed else "No records.")

    print(f"\n🔴 INCOMPLETE ({len(incomplete)}):")
    print("\n".join(incomplete) if incomplete else "No records.")

    print(f"\n⚪ PENDING ({len(pending)}):")
    print("\n".join(pending) if pending else "No records.")
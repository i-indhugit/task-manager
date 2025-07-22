import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(desc):
    tasks = load_tasks()
    tasks.append({"desc": desc, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {desc}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {status} {task['desc']}")

def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("✅ Task marked as complete.")
    else:
        print("❌ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['desc']}")
    else:
        print("❌ Invalid task number.")

if __name__ == "__main__":
    print("🔹 Task Manager CLI 🔹")
    print("1. Add Task\n2. List Tasks\n3. Complete Task\n4. Delete Task")
    choice = input("Enter choice: ")

    if choice == "1":
        desc = input("Task description: ")
        add_task(desc)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        num = int(input("Enter task number to mark complete: "))
        complete_task(num)
    elif choice == "4":
        num = int(input("Enter task number to delete: "))
        delete_task(num)
    else:
        print("❌ Invalid choice.")

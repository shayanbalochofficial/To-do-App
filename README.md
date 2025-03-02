
# ✨ Ultimate To-Do List Manager (CLI) ✨

A simple yet effective command-line To-Do List Manager built with Python and Click. Managed using the UV package manager, this app helps you keep track of your tasks with ease, using emojis for a touch of fun!

---

## 🌟 Features
- **Add Tasks**: Quickly add new tasks to your list.
- **List Tasks**: View all tasks with a ✅ or ❌ status indicator.
- **Complete Tasks**: Mark tasks as done by number.
- **Delete Tasks**: Remove tasks when they’re no longer needed.
- **Persistent Storage**: Tasks are saved to a JSON file for future use.

---

## 🚀 Getting Started

### 1️⃣ Install UV
First, install the UV package manager (skip if already installed):

#### Linux/macOS:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
#### Windows:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verify installation:
```bash
uv --version
```

### 2️⃣ Create and Initialize the Project
```bash
uv init todo-cli
cd todo-cli
```

### 3️⃣ Install Click (Dependency)
Add the required package:
```bash
uv add click
```

### 4️⃣ Activate UV Virtual Environment
#### Windows:
```bash
.venv\Scripts\activate
```
#### Linux/macOS:
```bash
source .venv/bin/activate
```

### 5️⃣ Save the Code
Copy the provided Python code into a file named `todo.py` in the `todo-cli` directory.

---

## 🎯 Usage

Run commands with `uv run python todo.py <command>`. Here’s how to use it:

### ➕ Add a New Task
```bash
uv run python todo.py add "Buy groceries"
```
- Adds a task with the given description.

### 📜 List All Tasks
```bash
uv run python todo.py list
```
- Displays all tasks with their status (✅ for done, ❌ for pending).

### ✅ Mark a Task as Completed
```bash
uv run python todo.py complete 1
```
- Marks the task at the specified number as completed.

### 🗑️ Remove a Task
```bash
uv run python todo.py delete 1
```
- Deletes the task at the specified number.

---

## 🎨 Example Output
```bash
$ uv run python todo.py add "Buy groceries"
Task 'Buy groceries' added successfully.

$ uv run python todo.py list
1. ❌ Buy groceries
2. ✅ Call friend

$ uv run python todo.py complete 1
Task #1 marked as completed.

$ uv run python todo.py delete 2
Task 'Call friend' deleted successfully.
```

---

## 💡 Tips
- Use task numbers carefully when completing or deleting to avoid errors.
- Check the `todo.json` file in your directory to see saved tasks.

---

## 📦 Requirements
- **Python 3.7+**: Ensure you have a modern Python version installed.
- **UV Package Manager**: For managing dependencies and virtual environments.
- **Dependencies**:
  - `click`: For the CLI framework (`uv add click`).

---

## 👨‍💻 Contributors
- **Shayan Baloch**: Creator and developer of this To-Do List Manager.

---

## 📜 License
This project is open-source and available under the MIT License. Feel free to fork, modify, and share it!

---

## 🙏 Acknowledgments
- Inspired by basic CLI task management tools.
- Thanks to the Click community for a robust CLI framework.

---

## 🎉 That’s It!
Your To-Do CLI is ready to help you manage your tasks efficiently. Start adding tasks and stay organized! 🚀

*Built with ❤️ by Shayan Baloch.*

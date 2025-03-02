import click  # to create a cli
import json  # to save and load tasks from a file
import os

TODO_FILE = "todo.json"

def load_tasks():
    """Load tasks from the JSON file, return empty list if file doesn’t exist or is invalid."""
    if not os.path.exists(TODO_FILE):
        return []  # Return empty list if file doesn’t exist
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []  # Return empty list if file is corrupted or unreadable

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task '{task}' added successfully.")

@click.command()
def list():
    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        click.echo(f"{i}. {status} {task['task']}")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):  # Fixed bounds check
        tasks[task_number - 1]['done'] = True
        save_tasks(tasks)
        click.echo(f"Task #{task_number} marked as completed.")
    else:
        click.echo("Invalid task number.")

@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):  # Fixed bounds check
        removed = tasks.pop(task_number - 1)  # Renamed 'remove' to 'removed' for clarity
        save_tasks(tasks)
        click.echo(f"Task '{removed['task']}' deleted successfully.")
    else:
        click.echo("Invalid task number.")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
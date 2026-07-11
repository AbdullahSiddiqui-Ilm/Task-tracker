# Task: CLI TODO App

## 📖 Description

**Task** is a command-line interface (CLI) application made to manage tasks efffortlessly.
it allows you to **add, update, delete, list, and track tasks** from your terminal.

---

## ✨ Features

- **Add a Task** → Create tasks. Each task gets a unique ID
- **Update a Task** → Modify the description of a task.
- **Update status of a task** → Update a task's status to `in progress` or `done`.
- **Delete a Task** → Remove tasks by their ID.
- **List Tasks** → Display all tasks or filter them by:
  `todo`, `in-progress`, `done`, or `all`

## 🗂 Project Structure

- **task.py** → Core CLI implementation
  - `main()` → Entry point, parses CLI arguments and runs commands.
  - `add_task(task_description, status="todo")` → Adds a new task.
  - `update_task(id, new_task)` → Updates description or status.
  - `list_tasks()` → Lists all tasks
  - `list_tasks_todo()` → Lists tasks which are todo
  - `list_tasks_inprogress()` → Lists tasks which are in progress
  - `list_tasks_done()` → Lists tasks which are done
  - `list_tasks_not_done()` → Lists tasks which are not done
  - `delete_task(id)` → Deletes a task.

- **pyproject.toml** → Project metadata, dependencies, and packaging config.

## ⚡ Installation

You can install Task directly from GitHub:

```bash
pip install git+https://github.com/AbdullahSiddiqui-Ilm/task.git
```

## 🚀 Usage

```bash
$ task add [-h] description

$ task update-task [-h] [-d description] id

$ task update-status [-h] [-d description] id

$ task list-tasks

$ task list-inprogress

$ task list-done

$ task list-todo

$ task list-not-done

$ task delete-tasks [-h] id
```

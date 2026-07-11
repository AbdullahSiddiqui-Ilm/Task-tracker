# Taskly: CLI TODO App

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
  - `add_task(database, description)` → Adds a new task.
  - `update_task(database, id, description?, status?)` → Updates description or status.
  - `mark_in_progress_task(database, id)` → Marks a task as _in-progress_.
  - `mark_done_task(database, id)` → Marks a task as _done_.
  - `delete_task(database, id)` → Deletes a task.
  - `list_task(database, status?, date?)` → Lists tasks with optional filters.

- **test_taskly.py** → Unit tests for all features using `pytest`.

- **pyproject.toml** → Project metadata, dependencies, and packaging config.

## ⚡ Installation

You can install Task directly from GitHub:

```bash
pip install git+https://github.com/AbdullahSiddiqui-Ilm/task.git
```

## 🚀 Usage

```bash
$ task add [-h] description

$ task update-task [-h] [-d description] [-s {done,in-progress,todo}] id

$ task update-status

$ task mark-done [-h] id

$ task mark-in-progress [-h] id

$ taskly delete [-h] id
```

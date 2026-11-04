# Task Manager v0.1

## Goal

Create a simple CLI task manager.

## Task structure

Each task contains:
- id
- title
- status

## Storage

All tasks are stored in one list.

## Statuses

- todo
- done

## Functions

### add_task()
Creates a new task and adds it to the list.

### list_tasks()
Displays all existing tasks.

### complete_task()
Finds a task by id and changes its status to done.

### delete_task()
Finds a task by id and removes it.

## Menu

1 - Add task
2 - List tasks
3 - Complete task
4 - Delete task
0 - Exit
import tkinter as tk

def add_task(todo_list, current_id, task_entry):
    if len(task_entry.get()) > 0:
        if len(current_id.get()) == 0:
            todo_list.insert(todo_list.index("end"), task_entry.get())

            with open("tasks.txt", "a") as file:
                file.write(f"{todo_list.get('end')}\n")

            clear_entries(current_id, task_entry)
        else:
            todo_list.delete(current_id.get())
            todo_list.insert(current_id.get(), task_entry.get())

            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                lines[int(current_id.get())] = f"{todo_list.get(int(current_id.get()))}\n"
            with open("tasks.txt", "w") as file:
                file.writelines(lines)

            clear_entries(current_id, task_entry)

def delete_task(todo_list, current_id, task_entry):
    if len(current_id.get()) > 0:
        todo_list.delete(current_id.get())

        with open("tasks.txt", "r") as file:
            lines = file.readlines()
        lines[int(current_id.get())] = ""
        with open("tasks.txt", "w") as file:
            file.writelines(lines)

        clear_entries(current_id, task_entry)

def mark_complete(todo_list, finished_list, current_id, task_entry):
    if len(current_id.get()) > 0:
        finished_list.insert("end", task_entry.get())
        todo_list.delete(current_id.get())
        with open("finished-tasks.txt", "a") as file:
            file.write(f"{finished_list.get('end')}")

        with open("tasks.txt", "r") as file:
            lines = file.readlines()
        lines[int(current_id.get())] = ""
        with open("tasks.txt", "w") as file:
            file.writelines(lines)

        clear_entries(current_id, task_entry)

def select_task(event, todo_list, current_id, task_entry):
    if event.widget.curselection():
        task_entry.delete(0, tk.END)
        current_id.set(f"{todo_list.index(event.widget.curselection())}")
        task_entry.insert(0, f"{todo_list.get(event.widget.curselection())}")

def deselect_task(event, current_id, task_entry):
    clear_entries(current_id, task_entry)

def select_finished_task(event, todo_list, current_id, task_entry):
    if event.widget.curselection():
        task_entry.delete(0, tk.END)
        current_id.set(f"{todo_list.index(event.widget.curselection())}")
        task_entry.insert(0, f"{todo_list.get(event.widget.curselection())}")

def deselect_finished_task(event, current_id, task_entry):
    clear_entries(current_id, task_entry)

def delete_finished_task(todo_list, current_id, task_entry):
    if len(current_id.get()) > 0:
        todo_list.delete(current_id.get())

        with open("finished-tasks.txt", "r") as file:
            lines = file.readlines()
        lines[int(current_id.get())] = ""
        with open("finished-tasks.txt", "w") as file:
            file.writelines(lines)

        clear_entries(current_id, task_entry)

def mark_uncompleted(todo_list, finished_list, current_id, task_entry):
    if len(current_id.get()) > 0:
        todo_list.insert("end", task_entry.get())
        finished_list.delete(current_id.get())
        with open("tasks.txt", "a") as file:
            file.write(f"{task_entry.get()}")

        with open("finished-tasks.txt", "r") as file:
            lines = file.readlines()
        lines[int(current_id.get())] = ""
        with open("finished-tasks.txt", "w") as file:
            file.writelines(lines)

        clear_entries(current_id, task_entry)


def clear_entries(current_id, task_entry):
    current_id.set("")
    task_entry.delete(0, tk.END)
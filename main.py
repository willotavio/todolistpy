import tkinter as tk
from tkinter import ttk

def add_task():
    if len(task_entry.get()) > 0:
        if len(id_entry.get()) == 0:
            todo_list.insert(todo_list.index("end"), task_entry.get())

            with open("tasks.txt", "a") as file:
                file.write(f"{todo_list.get('end')}\n")

            clear_entries()
        else:
            todo_list.delete(id_entry.get())
            todo_list.insert(id_entry.get(), task_entry.get())

            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                lines[int(id_entry.get())] = f"{todo_list.get(int(id_entry.get()))}\n"
            with open("tasks.txt", "w") as file:
                file.writelines(lines)

            clear_entries()

def delete_task():
    if len(current_id.get()) > 0:
        todo_list.delete(id_entry.get())

        with open("tasks.txt", "r") as file:
            lines = file.readlines()
        lines[int(current_id.get())] = ""
        with open("tasks.txt", "w") as file:
            file.writelines(lines)

        clear_entries()

def select_task(event):
    task_entry.delete(0, tk.END)
    if event.widget.curselection():
        current_id.set(f"{todo_list.index(event.widget.curselection())}")
        task_entry.insert(0, f"{todo_list.get(event.widget.curselection())}")

def deselect_task(event):
    clear_entries()

def mark_complete():
    if len(current_id.get()) > 0:
        finished_list.insert("end", todo_list.get(current_id.get()))
        todo_list.delete(current_id.get())
        with open("finished-tasks.txt", "a") as file:
            file.write(f"{finished_list.get('end')}\n")

        with open("tasks.txt", "r") as file:
            lines = file.readlines()
        lines[int(current_id.get())] = ""
        with open("tasks.txt", "w") as file:
            file.writelines(lines)

        clear_entries()
def clear_entries():
    current_id.set("")
    task_entry.delete(0, tk.END)

window = tk.Tk()
window.title("To-Do")
window.geometry("420x520")

notebook = ttk.Notebook(window)

todo_list_tab = ttk.Frame(notebook)
notebook.add(todo_list_tab, text="To-Do List")

finished_list_tab = ttk.Frame(notebook)
notebook.add(finished_list_tab, text="Finished List")

notebook.pack()

todo_list_title = tk.Label(todo_list_tab, text="To-Do List")
todo_list_title.pack()
todo_list = tk.Listbox(todo_list_tab, width=50)

try:
    with open("tasks.txt", "r") as file:
        for line in file.readlines():
            todo_list.insert("end", line)
except FileNotFoundError:
    pass

todo_list.pack(pady=10)

todo_list.bind("<<ListboxSelect>>", select_task)
todo_list.bind("<Double-1>", deselect_task)

current_id = tk.StringVar()

id_entry = tk.Entry(todo_list_tab, textvariable=current_id, state=tk.DISABLED)
id_entry.pack(pady=10)

task_entry = tk.Entry(todo_list_tab)
task_entry.pack(pady=10)

submit = tk.Button(todo_list_tab, text="Submit", command=add_task)
submit.pack(pady=10)

delete = tk.Button(todo_list_tab, text="Delete", command=delete_task)
delete.pack(pady=5)

complete = tk.Button(todo_list_tab, text="Complete", command=mark_complete)
complete.pack(pady=5)

finished_list_title = tk.Label(finished_list_tab, text="Finished List")
finished_list_title.pack()
finished_list = tk.Listbox(finished_list_tab, width=50)

try:
    with open("finished-tasks.txt", "r") as file:
        for line in file.readlines():
            finished_list.insert("end", line)
except FileNotFoundError:
    pass
finished_list.pack(pady=10)

window.mainloop()

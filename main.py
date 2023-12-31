import tkinter as tk
from tkinter import ttk
import functions as func

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

todo_list.bind("<<ListboxSelect>>", lambda event: func.select_task(event, todo_list, current_id, task_entry))
todo_list.bind("<Double-1>", lambda event: func.deselect_task(event, current_id, task_entry))

current_id = tk.StringVar()

id_entry = tk.Entry(todo_list_tab, textvariable=current_id, state=tk.DISABLED)
id_entry.pack(pady=10)

task_entry = tk.Text(todo_list_tab, height=3)
task_entry.pack(pady=10)

submit = tk.Button(todo_list_tab, text="Submit", command=lambda: func.add_task(todo_list, current_id, task_entry))
submit.pack(pady=10)

delete = tk.Button(todo_list_tab, text="Delete", command=lambda: func.delete_task(todo_list, current_id, task_entry))
delete.pack(pady=5)

complete = tk.Button(todo_list_tab, text="Complete", command=lambda: func.mark_complete(todo_list, finished_list, current_id, task_entry))
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

finished_list.bind("<<ListboxSelect>>", lambda event: func.select_finished_task(event, finished_list, current_finished_id, finished_task_entry))
finished_list.bind("<Double-1>", lambda event: func.deselect_finished_task(event, current_finished_id, finished_task_entry))

current_finished_id = tk.StringVar()

finished_id_entry = tk.Entry(finished_list_tab, textvariable=current_finished_id, state=tk.DISABLED)
finished_id_entry.pack(pady=10)

finished_task_entry = tk.Text(finished_list_tab, height=3)
finished_task_entry.pack(pady=10)

mark_uncomplete = tk.Button(finished_list_tab, text="Mark uncompleted", command=lambda: func.mark_uncompleted(todo_list, finished_list, current_finished_id, finished_task_entry))
mark_uncomplete.pack(pady=10)

delete_finished = tk.Button(finished_list_tab, text="Delete", command=lambda: func.delete_finished_task(finished_list, current_finished_id, finished_task_entry))
delete_finished.pack(pady=10)

window.mainloop()

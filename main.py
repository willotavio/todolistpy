import tkinter as tk

def add_task():
    if len(task_entry.get()) > 0:
        if len(id_entry.get()) == 0:
            todo_list.insert(todo_list.index("end"), task_entry.get())
            task_entry.delete(0, tk.END)
        else:
            todo_list.delete(id_entry.get())
            todo_list.insert(id_entry.get(), task_entry.get())
            current_id.set("")
            task_entry.delete(0, tk.END)

def delete_task():
    if len(current_id.get()) > 0:
        todo_list.delete(id_entry.get())
        current_id.set("")

def select_task(event):
    task_entry.delete(0, tk.END)
    if event.widget.curselection():
        current_id.set(f"{todo_list.index(event.widget.curselection())}")
        task_entry.insert(0, f"{todo_list.get(event.widget.curselection())}")

def deselect_task(event):
    current_id.set("")
    task_entry.delete(0, tk.END)

def mark_complete():
    if len(current_id.get()) > 0:
        finished_list.insert("end", todo_list.get(current_id.get()))
        todo_list.delete(current_id.get())

window = tk.Tk()
window.title("To-Do")
window.geometry("420x720")

todo_list_title = tk.Label(window, text="To-Do List")
todo_list_title.pack()
todo_list = tk.Listbox(window)
todo_list.pack(pady=10)

todo_list.bind("<<ListboxSelect>>", select_task)
todo_list.bind("<Double-1>", deselect_task)

finished_list_title = tk.Label(window, text="Finished List")
finished_list_title.pack()
finished_list = tk.Listbox(window)
finished_list.pack(pady=10)

current_id = tk.StringVar()

id_entry = tk.Entry(window, textvariable=current_id, state=tk.DISABLED)
id_entry.pack(pady=10)

task_entry = tk.Entry(window)
task_entry.pack(pady=10)

submit = tk.Button(window, text="Submit", command=add_task)
submit.pack(pady=10)

delete = tk.Button(window, text="Delete", command=delete_task)
delete.pack(pady=5)

complete = tk.Button(window, text="Complete", command=mark_complete)
complete.pack(pady=5)

window.mainloop()

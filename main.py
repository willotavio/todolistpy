import tkinter as tk

def add_task():
    if len(task_entry.get()) > 0:
        if len(id_entry.get()) == 0:
            todo_list.insert(0, task_entry.get())
            task_entry.delete(0, tk.END)
        else:
            todo_list.delete(id_entry.get())
            todo_list.insert(id_entry.get(), task_entry.get())
            id_entry.delete(0, tk.END)
            task_entry.delete(0, tk.END)

def delete_task():
    if todo_list.curselection():
        todo_list.delete(todo_list.curselection())

def update_task():
    id_entry.delete(0, tk.END)
    task_entry.delete(0, tk.END)
    if todo_list.curselection():
        id_entry.insert(0, todo_list.curselection())
        task_entry.insert(0, todo_list.get(todo_list.curselection()))

window = tk.Tk()
window.title("To-Do")
window.geometry("420x420")

todo_list = tk.Listbox(window)
todo_list.pack(pady=10)

id_entry = tk.Entry(window)
id_entry.pack(pady=10)
task_entry = tk.Entry(window)
task_entry.pack(pady=10)

submit = tk.Button(window, text="Submit", command=add_task)
submit.pack(pady=10)

delete = tk.Button(window, text="Delete", command=delete_task)
delete.pack(pady=5)

update = tk.Button(window, text="Update", command=update_task)
update.pack(pady=5)

window.mainloop()


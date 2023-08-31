import tkinter as tk

def add_task():
    if len(task_entry.get()) > 0:
        todo_list.insert(0, task_entry.get())
        task_entry.delete(0, tk.END)

def delete_task():
    if todo_list.curselection():
        todo_list.delete(todo_list.curselection())

window = tk.Tk()
window.title("To-Do")
window.geometry("420x420")

todo_list = tk.Listbox(window)
todo_list.pack(pady=10)

task_entry = tk.Entry(window)
task_entry.pack(pady=10)

submit = tk.Button(window, text="Submit", command=add_task)
submit.pack(pady=10)

delete = tk.Button(window, text="Delete", command=delete_task)
delete.pack(pady=5)

window.mainloop()


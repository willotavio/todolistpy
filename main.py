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
    if todo_list.curselection():
        todo_list.delete(todo_list.curselection())
        if len(id_entry.get()):
            current_id.set("")

def update_task(event):
    if event.widget.curselection():
        current_id.set(event.widget.curselection())

window = tk.Tk()
window.title("To-Do")
window.geometry("420x420")

todo_list = tk.Listbox(window)
todo_list.pack(pady=10)

todo_list.bind("<<ListboxSelect>>", update_task)

current_id = tk.StringVar()

id_entry = tk.Entry(window, textvariable=current_id, state=tk.DISABLED)
id_entry.pack(pady=10)

clear = tk.Button(window, text="Clear", command=lambda: current_id.set(""))
clear.pack(pady=5)

task_entry = tk.Entry(window)
task_entry.pack(pady=10)

submit = tk.Button(window, text="Submit", command=add_task)
submit.pack(pady=10)

delete = tk.Button(window, text="Delete", command=delete_task)
delete.pack(pady=5)

window.mainloop()


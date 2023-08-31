import tkinter as tk

def add_task():
    if len(task_entry.get()) > 0:
        todo_list.insert(0, task_entry.get())
        task_entry.delete(0, tk.END)

window = tk.Tk()
window.title("To-Do")

todo_list = tk.Listbox(window)
todo_list.pack()

task_entry = tk.Entry(window)
task_entry.pack()

submit = tk.Button(window, text="Submit", command=add_task)
submit.pack()

window.mainloop()


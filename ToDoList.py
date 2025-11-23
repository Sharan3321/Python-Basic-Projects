import tkinter as tk

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, task_description):
        task = {'name': task_name, 'description': task_description}
        self.tasks.append(task)
        self.update_display()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.update_display()

    def update_display(self):
        task_display.delete(1.0, tk.END)
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                task_display.insert(tk.END, f"Task {index}: {task['name']}\n")
                task_display.insert(tk.END, f"Description: {task['description']}\n\n")
        else:
            task_display.insert(tk.END, "You have no tasks.")

def add_task():
    task_name = task_name_entry.get()
    task_description = task_description_entry.get("1.0", tk.END).strip()
    if task_name and task_description:
        task_manager.add_task(task_name, task_description)
        task_name_entry.delete(0, tk.END)
        task_description_entry.delete("1.0", tk.END)

def remove_task():
    index = int(task_index_entry.get()) - 1
    task_manager.remove_task(index)

task_manager = ToDoListManager()

root = tk.Tk()
root.title("My To-Do List")


bg_color = "#F0F0F0"
root.configure(bg=bg_color)


header_frame = tk.Frame(root, bg="#1E8449", height=30)
header_frame.pack(fill=tk.X)

tk.Label(header_frame, text="To-Do List", fg="white", bg="#1E8449", font=("Arial", 14, "bold")).pack()

tk.Label(root, text="Task Name:", bg=bg_color).pack()
task_name_entry = tk.Entry(root, width=30)
task_name_entry.pack()

tk.Label(root, text="Task Description:", bg=bg_color).pack()
task_description_entry = tk.Text(root, height=4, width=30)
task_description_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#1E8449", fg="white", relief=tk.FLAT)
add_button.pack()

tk.Label(root, text="Task Index to Remove:", bg=bg_color).pack()
task_index_entry = tk.Entry(root, width=5)
task_index_entry.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#1E8449", fg="white", relief=tk.FLAT)
remove_button.pack()

task_display = tk.Text(root, height=10, width=40)
task_display.pack()

root.mainloop()

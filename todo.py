import tkinter as tk
from tkinter import ttk
import json
import os

def load():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for idx, task in enumerate(tasks):
        row = tk.Frame(frame2)
        row.pack(anchor="w", pady=5)

        task_text = task["name"]
        task_tag = task["tag"]

        if not(task["done"]):
            taskRow = tk.Label(row, text=f"{task_tag}, {task_text}")
            taskRow.pack(side="left")
            markDoneBtn = ttk.Button(row, text="Mark Done")
            markDoneBtn.config(command=lambda l=taskRow, b=markDoneBtn, i=idx: markDone(i, l, b))
            markDoneBtn.pack(side="left")

def vmwf():
    vmw.pack_forget()
    completedHead.pack_forget()
    frame3.pack_forget()
    for widget in frame2.winfo_children():
        widget.destroy()

    vctb.pack_configure(padx=10, pady=10)
    head.pack_configure(pady=20)
    frame1.pack_configure(anchor="nw", padx=10, pady=10)
    taskList.pack_configure(side="top", pady=30)
    frame2.pack_configure(padx=10, pady=10)

    if os.path.exists("tasks.json") and os.path.getsize("tasks.json") > 0:
        load()
    
    

def vctbf():
    head.pack_forget()
    frame1.pack_forget()
    taskList.pack_forget()
    frame2.pack_forget()
    vctb.pack_forget()

    vmw.pack_configure(pady=10)
    completedHead.pack_configure(pady=30)
    frame3.pack_configure(padx=10, pady=10)

    for widget in frame3.winfo_children():
        widget.destroy()
    if os.path.exists("tasks.json") and os.path.getsize("tasks.json") > 0:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        for task in tasks:
            task_text = task["name"]
            task_tag = task["tag"]
            if task["done"]:
                taskRow1 = tk.Label(frame3, text=f"{task_tag}, {task_text}")
                taskRow1.pack()
            
def markDone(index, label, button):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    
    tasks[index]["done"] = True

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    label.config(fg="gray")
    button.pack_forget()

def add():
    taskDesc = addBox.get()
    taskTag = selected_option.get()
    task = {
        "tag": taskTag,
        "name": taskDesc,
        "done": False
    }
    if os.path.exists("tasks.json") and os.path.getsize("tasks.json") > 0:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        tasks.append(task)
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    else:
        with open("tasks.json", "w") as file:
            json.dump([task], file, indent=4)

    addBox.delete(0, tk.END)

    for widget in frame2.winfo_children():
        widget.destroy()
    load()
 
root = tk.Tk()
root.geometry("400x600")
root.title("To-do List")

vmw = ttk.Button(root, text="View Main Window", command=vmwf)
completedHead = tk.Label(root, text="Completed Tasks", font=("Arial", 30))

vctb = ttk.Button(root, text="View Completed Tasks", command=vctbf)
vctb.pack(padx=10, pady=10)

head = tk.Label(root, font=("Arial", 30), text="To-do List")
head.pack(pady=20)

frame1 = tk.Frame(root)
frame1.pack(anchor="nw", padx=10, pady=10)

options = ["Select Tags", "School", "Important", "Misc."]
selected_option = tk.StringVar(root)
selected_option.set(options[0])
dropdown = ttk.OptionMenu(frame1, selected_option, *options)
dropdown.pack(side="left")

addBox = ttk.Entry(frame1, font="Arial")
addBox.pack(pady=20, side="left", padx=10)

addBtn = ttk.Button(frame1, text="Add", command=add)
addBtn.pack(side = "left", padx=20)

taskList = tk.Label(root, font=("Arial", 20), text="List of Tasks")
taskList.pack(side="top", pady=30)


frame2 = tk.Frame(root)
frame2.pack_configure(padx=10, pady=10)

if os.path.exists("tasks.json") and os.path.getsize("tasks.json") > 0:
    load()

frame3 = tk.Frame(root)

root.mainloop()

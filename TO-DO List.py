from tkinter import *
import tkinter.messagebox


def add_task():
    task = entry_task.get()
    if task:
        listbox_task.insert(END, task)
        entry_task.delete(0, END)


def delete_task():
    try:
        selected_task_index = listbox_task.curselection()[0]
        listbox_task.delete(selected_task_index)
    except IndexError:
        tkinter.messagebox.showwarning("Warning", "Please select a task to delete.")


def mark_completed():
    try:
        selected_task_index = listbox_task.curselection()[0]
        listbox_task.itemconfig(selected_task_index, {'bg': 'green'})
    except IndexError:
        tkinter.messagebox.showwarning("Warning", "Please select a task to mark as completed.")


window = Tk()
window.title("Python To-Do List APP")


frame_task = Frame(window)
frame_task.pack()


listbox_task = Listbox(frame_task, bg="white", fg="black", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)


entry_task = Entry(window, width=50)
entry_task.pack(pady=3)


add_button = Button(window, text="Add task", width=50, command=add_task)
add_button.pack(pady=3)

delete_button = Button(window, text="Delete selected task", width=50, command=delete_task)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as completed", width=50, command=mark_completed)
mark_button.pack(pady=3)


window.mainloop()

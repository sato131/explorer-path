import tkinter as tk
from tkinter import Pack, filedialog, Text
import os
import pathlib

root = tk.Tk()
root.title("explorer path")
apps = []

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialfile="/",
                                          filetypes=(("exexutables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)

def deleteApp():
    apps.clear()
    for widget in frame.winfo_children():
        widget.destroy()

canvas = tk.Canvas(width=700, height=700, bg="#99FFFF")
canvas.pack()

frame = tk.Frame(root, bg="#EEEEEE")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openFileButton = tk.Button(root, text="Open File", padx=5, pady=5, fg="white", bg="#263D42", command=addApp)
openFileButton.pack()

runFileButton = tk.Button(root, text="Run File", padx=5, pady=5, fg="white", bg="#263D42", command=runApp)
runFileButton.pack()

deleteFileButton = tk.Button(root, text="Delete File", padx=5, pady=5, fg="white", bg="#263D42", command=deleteApp)
deleteFileButton.pack()

root.mainloop()

import tkinter as tk

def get_answer():
    answer = entry.get()
    entry.delete(0, tk.END)
    label.config(text=f"You chose {answer}.")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=get_answer)
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()

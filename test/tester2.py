import tkinter as tk

def change_color():
    entry.tag_add('red', '1.1')
    entry.tag_add('red', '1.4')

root = tk.Tk()

entry = tk.Text(root, height=1, width=20)
entry.tag_configure('red', foreground='red')
entry.bind('<Return>', lambda e: "break")  # prevent newlines
entry.insert('1.0', '123456789')

entry.pack()
tk.Button(root, text='Change color', command=change_color).pack()
root.mainloop()
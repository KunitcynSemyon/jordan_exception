# from tkinter import *

# master = Tk()
# master.geometry("500x500")

# def create_matrix(rows, columns):
#     textMatrix = []
#     for r in range(rows):
#         textRow = []
#         for c in range(columns):
#             variable = StringVar()
#             entry = Entry(master, textvariable=variable, width=2)
#             entry.grid(row=r, column=c)
#             textRow.append(variable)
#         textMatrix.append(textRow)
#     return textMatrix

# n = IntVar()
# m = IntVar()

# n_label = Label(master, text = 'n:')
# m_label = Label(master, text = 'm:')
# n_label.pack()
# m_label.pack()

# row_entry = Entry(master)
# column_entry = Entry(master)
# row_entry.pack()
# column_entry.pack()

# #text_matrix = create_matrix(row_entry.get(), column_entry.get())

# master.mainloop()

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.width = 500
        self.height = 500
        self.bg = 'red'
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.n_label = tk.Label(self)
        self.n_label['text'] = 'n:'
        self.n_label.pack(side = 'left')

        self.m_label = tk.Label(self)
        self.m_label['text'] = 'm:'
        self.m_label.pack(side = 'top')

        self.row_entry = tk.Entry(self)
        self.row_entry.pack()

        self.column_entry = tk.Entry(self)
        self.column_entry.pack()

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Enter"
        self.hi_there["command"] = self.create_matrix(self.row_entry.get(), self.column_entry.get())
        self.hi_there.pack(side="top")
        

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_matrix(self, rows, column):
        pass

root = tk.Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
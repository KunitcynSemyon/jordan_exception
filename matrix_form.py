import tkinter as tk

class SimpleTableInput(tk.Frame):

    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)
        self._entry = {}
        self.rows = rows
        self.columns = columns #register a command to use for validation 
        vcmd = (self.register(self._validate), "%P") #create the table of widgets 
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e #adjust column weights so they all expand equally 
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1) #designate a final, empty row to fill up any extra space 
            self.grid_rowconfigure(rows, weight=1)

#Return a list of lists, containing the data in the table
    def get(self):
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):
#Perform input validation. Allow only an empty value, or a value that can be converted to a float
        if P.strip() == "":
            return True
        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True

class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 3, 3)
        self.submit = tk.Button(self, text="Submit", command=self.jordan(self.table.get(), 2, 3))
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="bottom")

    def on_submit(self):
        print(self.table.get())

    def jordan(self, matrix, row, column):
        row -= 1
        column -= 1
        temp_matrix = []
        matrix = [[float(column) for column in row] for row in matrix]
        for i in range(len(matrix)):
            temp_matrix.append([])
            for j in range(len(matrix[i])):
                temp_val = (matrix[i][j] * matrix[row][column] - matrix[i][column] * matrix[row][j]) / matrix[row][column]
                temp_matrix[i].append(temp_val)

        for i in range(len(matrix)):
            temp_matrix[i][column] = matrix[i][column] / matrix[row][column] * -1

        for i in range(len(matrix[row])):
            temp_matrix[row][i] = matrix[row][i] / matrix[row][column]

        temp_matrix[row][column] = 1 / matrix[row][column]

        return temp_matrix

root = tk.Tk()
Example(root).pack(side="top", fill="both", expand=True)
root.mainloop()
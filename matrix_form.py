import tkinter as tk

class SimpleTableInput(tk.Frame):

    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)
        self._entry = {}
        self.rows = rows
        self.columns = columns #register a command to use for validation 
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key")
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
            self.bell()
        except ValueError:
            return False
        return True

class Example(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text = 'Столбец:')
        self.label2 = tk.Label(self, text = 'Строка:')
        self.label3 = tk.Label(self, text = 'Столбец:')
        self.label4 = tk.Label(self, text = 'Строка:')
        self.label = tk.Label(self, height = "10", width = "50")
        self.label5 = tk.Label(self, text = 'Ответ:')
        self.label6 = tk.Label(self, height = "10", width = "50")

        self.n = tk.Entry(self) #столбец
        self.m = tk.Entry(self) #строка
        self.n1 = tk.Entry(self)
        self.m1 = tk.Entry(self)

        self.table = SimpleTableInput(self, 3, 5)
        self.table1 = SimpleTableInput(self, 3, 4)

        self.submit = tk.Button(self, text="Шаг 2", command = lambda : self.jordan(self.table1.get(), self.n1.get(), self.m1.get()))
        self.submit1 = tk.Button(self, text="Шаг 1", command = lambda : self.jordan(self.table.get(), self.n.get(), self.m.get()))

        self.label1.grid(row = 0, column = 0)
        self.n.grid(row = 0, column = 1, sticky = 'NS')

        self.label2.grid(row = 1, column = 0)
        self.m.grid(row = 1, column = 1, sticky = 'NS')

        self.table.grid(row = 2, column = 1)
        self.submit1.grid(row = 3, column = 1)

        self.label3.grid(row = 4, column = 0)
        self.n1.grid(row = 4, column = 1, sticky = 'NS')

        self.label4.grid(row = 5, column = 0)
        self.m1.grid(row = 5, column = 1, sticky = 'NS')

        self.table1.grid(row = 6, column = 1)
        self.submit.grid(row = 7, column = 1)

        self.label.grid(row = 8, column = 1)

        self.label5.grid(row = 9, column = 0)
        self.label6.grid(row = 9, column = 1)


        #self.n.pack(side = 'top')
        # self.m.pack(side = 'top')
        # self.n1.pack(side = 'top')
        # self.m1.pack(side = 'top')
        # self.label.pack(side="bottom")
        # self.table.pack(side="top", fill="both", expand=True)
        # self.table1.pack(side="top", fill="both", expand=True)
        # self.submit.pack(side="bottom")
        # self.submit1.pack(side="bottom")

        

    def delete_colomn(self, a, n):

        """
            a - список, где удаляем строку
            n - номер столбца, который удаляем
        """
        new_list = []
        #print(a)
        #print(n)
        for i in range(len(a)):
            new_list[i] = []
            row = a[i]
            for j in range(len(row)):
                if j != n:
                    new_list[i].append(row[j])
        return new_list            

    def jordan(self, mat, n, m):
        
        row = int(m) - 1 
        column = int(n) - 1
        matrix = [[float(columns) for columns in rows] for rows in mat]

        #print(matrix)
        #print(row)
        #print(column)

        temp_matrix = []
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

        print(temp_matrix)
        #temp_matrix = self.delete_colomn(temp_matrix, column)

        
        for i in temp_matrix:
            i = i.pop()

        self.label['text'] = temp_matrix
        self.label6['text'] = f'x1={temp_matrix[0][1]}a\n x2={temp_matrix[1][1]}b\n x3={temp_matrix[0][0]}-{temp_matrix[0][1]}a-{temp_matrix[0][2]}b\n x4={temp_matrix[1][0]}-{temp_matrix[1][1]}a-{temp_matrix[1][2]}b'

        return temp_matrix

root = tk.Tk()
Example(root).pack(side="top", fill="both", expand=True)
root.mainloop()
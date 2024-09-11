import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator OOP")

        self.entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 4)
        ]

        for (text, row, column, *span) in buttons:
            if text == '=':
                button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 18), command=self.calculate)
            elif text == 'C':
                button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 18), command=self.clear_entry)
            else:
                button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: self.click_button(t))
            button.grid(row=row, column=column, columnspan=span[0] if span else 1)

    def click_button(self, value):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + value)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

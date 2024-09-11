import tkinter as tk
from calculator.calc_ui import Calculator

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
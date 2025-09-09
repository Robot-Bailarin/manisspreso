import tkinter as tk
from visual.principal import ManisspresoApp

def inicio()->None:
    root = tk.Tk()
    app = ManisspresoApp(root)
    root.mainloop()

if __name__ == "__main__":
    inicio()


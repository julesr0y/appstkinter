import tkinter as tk
def clear():
    texte.delete("1.0","end")
gui = tk.Tk()
gui.geometry("300x150")
texte = tk.Text(gui, height=5)
texte.pack(pady=10)
btn = tk.Button(gui, text="Effacer", command=clear)
btn.pack()
gui.mainloop()
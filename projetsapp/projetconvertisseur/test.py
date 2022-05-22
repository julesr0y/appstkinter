from cgitb import text
import tkinter as tk

def action():
    lblResultat['text']=champNom.get()

app = tk.Tk()
app.geometry("800x800")

ok = tk.Button(app, text="Valider", command = action)
lblNom = tk.Label(app, text="Saisir nom")
champNom = tk.Entry(app)
lblResultat = tk.Label(app, text="Resultat...")
lblNom.pack()
champNom.pack()
lblResultat.pack()
ok.pack()

app.mainloop()
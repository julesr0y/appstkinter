from ntpath import join
from tkinter import *

app = Tk()
app.title("Rendu monnaie")
app.minsize(320, 100)

txt = Entry(app) #entrée utilisateur
ch = Label(app) #label qui affiche le resultat, vide au demarrage

txt.grid(row=0, column=0, sticky=W)
txt.focus_force() #force le curseur (oblige l'activation de la barre)
ch.grid(row=1, column=0)

def glouton():
    arendre = int(txt.get()) #int permet de convertir l'entree en nombre
    billet500 = 0
    billet200 = 0
    billet100 = 0
    billet50 = 0
    billet20 = 0
    billet10 = 0
    billet5 = 0
    piece2 = 0
    piece1 = 0
    while arendre != 0:
        
        if arendre >= 500:
            arendre -= 500
            billet500 += 1
            
        elif arendre >= 200:
            arendre -= 200
            billet200 += 1
            
        elif arendre >= 100:
            arendre -= 100
            billet100 += 1
            
        elif arendre >= 50:
            arendre -= 50
            billet50 += 1
            
        elif arendre >= 20:
            arendre -= 20
            billet20 += 1
            
        elif arendre >= 10:
            arendre -= 10
            billet10 += 1
            
        elif arendre >= 5:
            arendre -= 5
            billet5 += 1
            
        elif arendre >= 2:
            arendre -= 2
            piece2 += 1
            
        elif arendre >= 1:
            arendre -= 1
            piece1 += 1
    
    reponse = billet500, billet200, billet100, billet50, billet20, billet10, billet5, piece2, piece1
    ch.configure(text = reponse)

Button(app,text='Vérifier',command=glouton).grid(row=0 , column=1) # bouton qui lance la commande

app.mainloop()
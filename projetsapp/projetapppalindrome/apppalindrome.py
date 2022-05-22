from tkinter import *
from turtle import bgcolor

app = Tk()
app.title("Vérification palindrome")
app.geometry("320x120")
app.resizable(width=False, height=False)
app.configure(bg='#21272c')
txt = Entry(app) #entrée utilisateur
ch = Label(app) #label qui affiche le resultat, vide au demarrage

txt.grid(row=0, column=0)
txt.focus_force() #force le curseur (oblige l'activation de la barre)
ch.grid(row=1, column=0)
ch.configure(bg='#21272c', fg="white")

#fonction de verification du palindrome
def palindrome():
    ch.grid(row=3, column=0) #permet de réafficher un resultat si la fonction de nettoyage d'écran a été utilisée
    mot = txt.get()
    mot = mot.lower()
    if mot == "":
        reponse = "Veuillez indiquez un mot ou un nombre"
        ch.configure(text = reponse)
    else:
        motinverse = ''.join(reversed(mot))
        if mot == motinverse:
            reponse = mot + " est un palindrome"
            ch.configure(text = reponse)
        else:
            reponse = mot + " n'est pas un palindrome"
            ch.configure(text = reponse)

verifier = Button(app,text='Vérifier', anchor='center', command=palindrome).grid(row=1 , column=0) # bouton qui lance la commande

#fonction de "nettoyage" de l'ecran
def clear():
    ch.grid_forget()
    txt.delete("0","end")

vider = Button(app,text='Vider', anchor='center', command=clear).grid(row=2 , column=0) # bouton qui lance la commande
app.mainloop()
from tkinter import *

app = Tk()
app.title("Vérification palindrome")
app.geometry("300x140")
app.resizable(width=False, height=False)
app.configure(bg='#21272c')
txt = Entry(app) #entrée utilisateur
ch = Label(app) #label qui affiche le resultat, vide au demarrage

txt.pack(side=TOP, padx=5, pady=5)
txt.focus_force() #force le curseur (oblige l'activation de la barre)

#fonction de verification du palindrome
def palindrome():
    mot = txt.get()
    mot = mot.lower()
    if mot == "":
        reponse = "Veuillez indiquez un mot ou un nombre"
        ch.configure(text = reponse)
    elif len(mot) > 22:
        reponse = "Ce mot est trop long"
        ch.configure(text = reponse)
    else:
        motinverse = ''.join(reversed(mot))
        if mot == motinverse:
            reponse = mot + " est un palindrome"
            ch.configure(text = reponse)
        else:
            reponse = mot + " n'est pas un palindrome"
            ch.configure(text = reponse)

verifier = Button(app,text='Vérifier', anchor='center', command=palindrome).pack() #bouton qui lance la commande

#fonction de "nettoyage" de l'ecran
def clear():
    ch.pack_forget()
    txt.delete("0","end")
    ch.pack() #permet de réafficher un resultat si la fonction de nettoyage d'écran a été utilisée

vider = Button(app,text='Vider', anchor='center', command=clear).pack() #bouton qui lance la commande

ch.pack()
ch.configure(bg='#21272c', fg="white")

app.mainloop()
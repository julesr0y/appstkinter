from tkinter import * 
 
fenetre = Tk() 
fenetre.title("Conversions € - $") 
 
eur=Entry(fenetre) 
doll=Entry(fenetre) 
ch = Label(fenetre)
eur.grid(row=0, column=1) 
doll.grid(row=1, column=1) 
ch.grid(row=2, column=1) 


def eurotodollar(): 
    #Récupération des variables
    euro = float(eur.get())
    dollar = euro*1.1
    euro = str(euro) + "€ valent"
    dollar = euro + str(dollar) + "$"
    ch.configure(text = dollar)

def dollartoeuro(): 
    #Récupération des variables
    dollar = float(doll.get())
    euro = dollar*0.9
    ch.configure(text = euro)
 
txt1=Label(fenetre, text="Valeur en euros : ").grid(row=0, column=0) 
txt2=Label(fenetre, text="Valeur en dollars : ").grid(row=1, column=0) 
 
Button(fenetre,text='€ -> $',command=eurotodollar).grid(row=0 , column=3) 
Button(fenetre,text='$ -> €',command=dollartoeuro).grid(row=1, column=3) 
 
fenetre.mainloop()
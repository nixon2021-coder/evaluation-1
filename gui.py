
#from tkinter import *
#from types import MappingProxyType
#Manger= Tk()
#l= Label(Manger,text="vilain")
#e= Entry(Manger,bg="red")
#l.pack()
#e.pack()
#Manger.mainloop()

from tkinter import *
screen = Tk()
screen.geometry("500x500")
screen.title("Formulaire d'enregistrement")
heading = Label(text="Formulaire d'enregistrement",bg="blue", fg="red", width="500",
height="3")
heading.pack()

Nom_text = Label(text = "Nom:",)
Prenom_text = Label(text = "Prenom:",)
Email_text = Label(text = "Email:",)
Telephone_text = Label(text = "Telephone:",)  
Nom_text.place(x = 15, y = 70)
Prenom_text.place(x = 15, y = 140)
Email_text.place(x = 15, y = 210)
Telephone_text.place(x = 15, y = 280)


Nom = StringVar()
Prenom = StringVar()
Email = StringVar()
Telephone = StringVar()

Nom_entry = Entry(textvariable = Nom, width="30")
Prenom_entry = Entry(textvariable = Prenom, width="30")
Email_entry = Entry(textvariable = Email, width="30")
Telephone_entry = Entry(textvariable = Telephone, width="30")

Nom_entry.config(relief=SUNKEN)
Prenom_entry.config(relief=SUNKEN)
Email_entry.config(relief=SUNKEN)
Telephone_entry.config(relief=SUNKEN)

def enregistrer_informations():

    f = open("name.json", "a")
    f.write("Nom: %s\nPrenom: %s\nEmail: %s\nTelephone: %s" % (Nom_entry.get(), Prenom_entry.get(), Email_entry.get(), Telephone_entry.get()))
    Nom_entry.delete(0,END)
    Prenom_entry.delete(0,END)
    Email_entry.delete(0,END)
    Telephone_entry.delete(0,END)
    f.close()

Nom_entry.place(x = 15, y = 100)
Prenom_entry.place(x = 15, y = 180)
Email_entry.place(x = 15, y = 240)
Telephone_entry.place(x = 15, y = 320)

Valider = Button(screen,text="Valider", width="30", height="2", bg="grey", command=enregistrer_informations)
Valider.place(x = 15, y = 380)

screen.mainloop()































 
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk

login=ctk.CTk()
login.title('authenitification')
login.geometry('800x500+300+200')
login.columnconfigure(0,weight=350)
login.resizable(False,False)


imag = PhotoImage(file='background (3).png')
Label(login,image=imag,bg="white").place(x=0,y=0)


frame =ctk.CTkFrame(login,width=400,height=500 , fg_color='#FFFFFF')
frame.place(x=400,y=0)

image_path = 'Hemato Desk logo.png'
original_image = PhotoImage(file=image_path)
# Redimensionner l'image
nouvelle_image = original_image.subsample(4,4)  # Redimensionne à la moitié de la taille originale
label_image = Label(frame, image=nouvelle_image, bg="white")
label_image.place(x=410, y=20)

label_image2 = Label(frame, image=nouvelle_image, bg="white")
label_image2.place(x=20, y=20)

heading=Label(frame,text='Connecter Vous ',fg='#3088BD',bg='#FFFFFF',font=('Karla',30,'bold'))
heading.place(x=107,y=45)

#####-----------------------------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Entrer votre matricule')

user_matricule=ctk.CTkLabel(frame,text="Matricule :",text_color='#263A5F',font=('Karla',20,'bold'))
user_matricule.place(x=80,y=120)
user=ctk.CTkEntry(frame,width=250,height=40,border_width=2,border_color='#263A5F',font=('Karla',16))
user.place(x=80,y=150)
user.insert(0,'Entrer votre matricule')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

#####-------------------------------

def on_enter(e):
    MP.delete(0,'end')

def on_leave(e):
    name=MP.get()
    if name=='':
       MP.insert(0,'Entrer votre mot de passe')

motDP=ctk.CTkLabel(frame,text="Mot De Passe :",text_color='#263A5F',font=('Karla',20,'bold'))
motDP.place(x=80,y=200)
MP=ctk.CTkEntry(frame,width=250,height=40,border_width=2,border_color='#263A5F',font=('Karla',16))
MP.place(x=80,y=230)
MP.insert(0,'Entrer votre mot de passe')
MP.bind('<FocusIn>',on_enter)
MP.bind('<FocusOut>',on_leave)


########################################
button = ctk.CTkButton(frame, text="Se Connecter", width=150, height=50, corner_radius=15,font=('Karla',20,'bold'),fg_color='#263A5F',text_color='#FFFFFF', command=None)
button.place(x=125,y=300)
nouveau_AM= ctk.CTkLabel(frame, text="Je n'ai pas de compte ",font=('Karla',12), fg_color="transparent",text_color='#263A5F')
nouveau_AM.place(x=100,y=370)
inscrire=Button(frame, text="S'inscrire",font=('Karla',12,'bold'),border=0,bg='white',cursor='hand2',fg='#DD2F2E' ,command=None)
inscrire.place(x=270,y=467)




login.mainloop()
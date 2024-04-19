from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import pymysql

'''def connection():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='hematodisk_data_base'
    )
    return conn'''

class login():
    def __init__(self,root):
        super().__init__()
        self.root = root
        self.root.title('Authentification')
        self.root.geometry('800x500+300+200')
        self.root.columnconfigure(0, weight=350)
        self.root.resizable(False, False)

        imag = PhotoImage(file='background.png')
        label = Label(self.root, image=imag)
        label.grid()

        frame = ctk.CTkFrame(self.root, width=400, height=500, fg_color='#FFFFFF')
        frame.place(x=400, y=0)

        original_image = PhotoImage(file='Hemato Desk logo.png')
        # Redimensionner l'image
        nouvelle_image = original_image.subsample(4, 4)  # Redimensionne à la moitié de la taille originale
        label_image = Label(frame, image=nouvelle_image, bg="white")
        label_image.place(x=410, y=20)

        label_image2 = Label(frame, image=nouvelle_image, bg="white")
        label_image2.place(x=20, y=20)

        heading = Label(frame, text='Connecter Vous ', fg='#3088BD', bg='#FFFFFF', font=('Karla', 30, 'bold'))
        heading.place(x=107, y=45)

        #####-----------------------------------

        def on_enter(e):
            self.root.user.delete(0, 'end')

        def on_leave(e):
            self.root.name = self.root.user.get()
            if self.root.name == '':
                self.root.user.insert(0, 'Entrer votre matricule')

        user_matricule = ctk.CTkLabel(frame, text="Matricule :", text_color='#263A5F', font=('Karla', 20, 'bold'))
        user_matricule.place(x=80, y=120)
        self.root.user = ctk.CTkEntry(frame, width=250, height=40, border_width=2, border_color='#263A5F',font=('Karla', 16))
        self.root.user.place(x=80,y=150)
        self.root.user.insert(0, 'Entrer votre matricule')
        self.root.user.bind('<FocusIn>', on_enter)
        self.root.user.bind('<FocusOut>', on_leave)

        #####-------------------------------

        def on_enter(e):
            self.root.MP.delete(0, 'end')

        def on_leave(e):
            self.root.name = self.root.MP.get()
            if self.root.name == '':
                self.root.MP.insert(0, 'Entrer votre mot de passe')

        motDP = ctk.CTkLabel(frame, text="Mot De Passe :", text_color='#263A5F', font=('Karla', 20, 'bold'))
        motDP.place(x=80, y=200)
        self.root.MP = ctk.CTkEntry(frame, width=250, height=40, border_width=2, border_color='#263A5F', font=('Karla', 16))
        self.root.MP.place(x=80, y=230)
        self.root.MP.insert(0, 'Entrer votre mot de passe')
        self.root.MP.bind('<FocusIn>', on_enter)
        self.root.MP.bind('<FocusOut>', on_leave)

        ########################################
        button = ctk.CTkButton(frame, text="Se Connecter", width=150, height=50, corner_radius=15,font=('Karla', 20, 'bold'), fg_color='#263A5F', cursor='hand2', text_color='#FFFFFF',command=None)
        button.place(x=125, y=300)
        nouveau_AM = ctk.CTkLabel(frame, text="Je n'ai pas de compte ", font=('Karla', 12), fg_color="transparent",
                                  text_color='#263A5F')
        nouveau_AM.place(x=100, y=370)
        inscrire = Button(frame, text="S'inscrire", font=('Karla', 12, 'bold'), border=0, bg='white', cursor='hand2',
                          fg='#DD2F2E', command=None)
        inscrire.place(x=270, y=467)




app = ctk.CTk()
Login_page = login(app)
app.mainloop()
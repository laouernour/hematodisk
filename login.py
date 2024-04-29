from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
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
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title('Authentification')
        self.root.geometry('800x500+300+200')
        self.root.columnconfigure(0, weight=350)
        self.root.resizable(False, False)

        # Charger les images avec Pillow
        background_image = Image.open('background.png')
        logo_image = Image.open('Hemato Desk logo.png')

        # Convertir les images en format compatible avec Tkinter
        self.background_img = ImageTk.PhotoImage(background_image)
        self.logo_img = ImageTk.PhotoImage(logo_image.resize((logo_image.width // 4, logo_image.height // 4)))  # Redimensionner l'image

        # Afficher l'image de fond à gauche
        label_background = Label(self.root, image=self.background_img)
        label_background.place(x=0, y=0)

        frame = ctk.CTkFrame(self.root, width=400, height=500, fg_color='#FFFFFF')
        frame.place(x=400, y=0)

        label_image = Label(frame, image=self.logo_img, bg="white")
        label_image.place(x=460, y=20)

        label_image2 = Label(frame, image=self.logo_img, bg="white")
        label_image2.place(x=50, y=20)

        heading = Label(frame, text='Connecter Vous ', fg='#3088BD', bg='#FFFFFF', font=('Karla', 30, 'bold'))
        heading.place(x=148, y=45)
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

        # Bind the hide function to KeyRelease event of the password field
        self.root.MP.bind('<KeyRelease>', lambda event: hide())


        ########################################
        button = ctk.CTkButton(frame, text="Se Connecter", width=150, height=50, corner_radius=15,font=('Karla', 20, 'bold'), fg_color='#263A5F', cursor='hand2', text_color='#FFFFFF',command=None)
        button.place(x=125, y=300)
        nouveau_AM = ctk.CTkLabel(frame, text="Je n'ai pas de compte ", font=('Karla', 12), fg_color="transparent",
                                  text_color='#263A5F')
        nouveau_AM.place(x=100, y=370)
        inscrire = Button(frame, text="S'inscrire", font=('Karla', 12, 'bold'), border=0, bg='white', cursor='hand2',activebackground='white',fg='#DD2F2E', command=None)
        inscrire.place(x=362, y=562)

        # Définir les méthodes show() et hide()
        def hide():
            self.eyebutton.configure(image=self.closeeyeresize, command=show)
            self.root.MP.configure(show='*')
        def show():
            self.eyebutton.configure(image=self.openeyeresize, command=hide)
            self.root.MP.configure(show='')

        # Charger les images des yeux ouverts et fermés
        self.openeye = Image.open('eye open.png')
        self.closeeye = Image.open('close eye.png')

        # Convertir les images en format compatible avec Tkinter et redimensionner
        self.openeyeresize = ImageTk.PhotoImage(self.openeye.resize((self.openeye.width // 7, self.openeye.height // 7)))
        self.closeeyeresize = ImageTk.PhotoImage(self.closeeye.resize((self.closeeye.width // 10, self.closeeye.height // 10)))

        # Créer le bouton des yeux avec l'image des yeux fermés
        self.eyebutton = Button(frame, image=self.closeeyeresize, bd=0, bg="#FFFFFF", command=hide)
        self.eyebutton.place(x=440, y=360)

        # Désactiver le bouton de l'œil
        self.eyebutton.config(state=DISABLED)

        # Suivre si le mot de passe a été entré
        def on_key_release(e):
            self.root.name = self.root.MP.get()
            if self.root.name == '':
                self.eyebutton.config(state=DISABLED)  # Désactiver le bouton si le mot de passe n'est pas entré
            else:
                self.eyebutton.config(state=NORMAL)  # Activer le bouton si le mot de passe est entré

        self.root.MP.bind('<KeyRelease>', on_key_release)

app = ctk.CTk()
Login_page = login(app)
app.mainloop()
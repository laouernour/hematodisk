from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox  # Importer messagebox depuis tkinter
import customtkinter as ct  # Importer les widgets customtkinter

class login(ct.CTk):
    def __init__(self):
        super().__init__()
        # Utilisez simplement `self` à la place de `self.root`
        self.title('Authentification')
        self.geometry('800x500+300+100')
        self.columnconfigure(0, weight=350)
        self.resizable(False, False)

        # Charger les images avec Pillow
        background_image = Image.open('background.png')
        logo_image = Image.open('Hemato Desk logo.png')

        # Convertir les images en format compatible avec Tkinter
        self.background_img = ImageTk.PhotoImage(background_image)
        self.logo_img = ImageTk.PhotoImage(logo_image.resize((logo_image.width // 4, logo_image.height // 4))) # Redimensionner l'image

        # Afficher l'image de fond à gauche
        label_background = Label(self, image=self.background_img)
        label_background.place(x=0, y=0)

        frame = ct.CTkFrame(self, width=400, height=500, fg_color='#FFFFFF')  # Utiliser root à la place de self.root
        frame.place(x=400, y=0)

        label_image = Label(frame, image=self.logo_img, bg="white")
        label_image.place(x=460, y=20)

        label_image2 = Label(frame, image=self.logo_img, bg="white")
        label_image2.place(x=50, y=20)

        heading = Label(frame, text='Connecter Vous ', fg='#3088BD', bg='#FFFFFF', font=('Karla', 30, 'bold'))
        heading.place(x=148, y=45)

        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            self.name = self.user.get()
            if self.name == '':
                self.user.insert(0, 'Entrer votre matricule')

        user_matricule = ct.CTkLabel(frame, text="Matricule :", text_color='#263A5F', font=('Karla', 20, 'bold'))
        user_matricule.place(x=80, y=120)
        self.user = ct.CTkEntry(frame, width=250, height=40, border_width=2, border_color='#263A5F',font=('Karla', 16))
        self.user.place(x=80,y=150)
        self.user.insert(0, 'Entrer votre matricule')
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)

        def on_enter(e):
            self.MP.delete(0, 'end')

        def on_leave(e):
            self.name = self.MP.get()
            if self.name == '':
                self.MP.insert(0, 'Entrer votre mot de passe')

        motDP = ct.CTkLabel(frame, text="Mot De Passe :", text_color='#263A5F', font=('Karla', 20, 'bold'))
        motDP.place(x=80, y=200)
        self.MP = ct.CTkEntry(frame, width=250, height=40, border_width=2, border_color='#263A5F', font=('Karla', 16))
        self.MP.place(x=80, y=230)
        self.MP.insert(0, 'Entrer votre mot de passe')
        self.MP.bind('<FocusIn>', on_enter)
        self.MP.bind('<FocusOut>', on_leave)

        def hide():
            self.eyebutton.configure(image=self.closeeyeresize, command=show)
            self.MP.configure(show='*')
        def show():
            self.eyebutton.configure(image=self.openeyeresize, command=hide)
            self.MP.configure(show='')

        self.openeye = Image.open('eye open.png')
        self.closeeye = Image.open('close eye.png')

        self.openeyeresize = ImageTk.PhotoImage(self.openeye.resize((self.openeye.width // 7, self.openeye.height // 7)))
        self.closeeyeresize = ImageTk.PhotoImage(self.closeeye.resize((self.closeeye.width // 10, self.closeeye.height // 10)))

        self.eyebutton = Button(frame, image=self.closeeyeresize, bd=0, bg="#FFFFFF", command=hide)
        self.eyebutton.place(x=440, y=360)

        self.eyebutton.config(state=DISABLED)

        def on_key_release(e):
            self.name = self.MP.get()
            if self.name == '':
                self.eyebutton.config(state=DISABLED)
            else:
                self.eyebutton.config(state=NORMAL)

        self.MP.bind('<KeyRelease>', on_key_release)

        ########################################
        button = ct.CTkButton(frame, text="Se Connecter", width=150, height=50, corner_radius=15,
                               font=('Karla', 20, 'bold'), fg_color='#263A5F', cursor='hand2', text_color='#FFFFFF',
                               command=self.connecter)
        button.place(x=125, y=300)
        nouveau_AM = ct.CTkLabel(frame, text="Je n'ai pas de compte ", font=('Karla', 12), fg_color="transparent",
                                  text_color='#263A5F')
        nouveau_AM.place(x=100, y=370)
        inscrire = Button(frame, text="S'inscrire", font=('Karla', 12, 'bold'), border=0, bg='white', cursor='hand2',
                          activebackground='white', fg='#DD2F2E', command=self.fenetre_authentification)
        inscrire.place(x=362, y=562)

    def connecter(self):
        if self.user.get() == "" or self.MP.get() == "" :
            messagebox.showerror("Erreur", f"Veuillez saisir le Matricule et le Mot de passe ", parent=self)
        else:
            try:
                mydb = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                mycursor = mydb.cursor()
                mycursor.execute("select * from administrateur where matricule_administrateur=%s and mot_de_passe=%s",(self.user.get(),self.MP.get()))
                row=mycursor.fetchone()
                if row == None:
                    messagebox.showerror("Erreur", f"Information Invalidée ", parent=self)
                else:
                    messagebox.showinfo("Success", f"Bienvenu ", parent=self)
                    mydb.close()
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)
    def fenetre_authentification(self):
        self.destroy()
        import authentification


Login_page = login()
Login_page.mainloop()

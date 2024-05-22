import customtkinter as ct
import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Import PIL for image handling

class Inscrire(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#263A5F')

        self.formulaire_frame = ct.CTkFrame(self, fg_color='#FFFFFF', width=w, height=h, border_width=2,
                                            border_color='#263A5F')
        self.formulaire_frame.pack(expand=True, fill='both')

        # Frame for the title label
        self.label_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.label_frame.pack(pady=10)

        self.label = ct.CTkLabel(self.label_frame, text="S'inscrire Administrateur :", font=('Karla', 26,'bold'))
        self.label.pack(expand=True, pady=20)

        # Frame for inscription form using grid
        self.inscription_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.inscription_frame.pack(pady=10)

        # Nom and Prénom in the same row
        self.nomADM_label = ct.CTkLabel(self.inscription_frame, text="Nom :", font=('Karla', 18))
        self.nomADM_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.nomADM_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10, font=('Karla', 14))
        self.nomADM_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenomADM_label = ct.CTkLabel(self.inscription_frame, text="Prénom :", font=('Karla', 18))
        self.prenomADM_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")
        self.prenomADM_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                        font=('Karla', 14))
        self.prenomADM_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Other fields using pack
        # Date de Naissance
        self.date_naissanceADM_label = ct.CTkLabel(self.inscription_frame, text="Date de Naissance :", font=('Karla', 18))
        self.date_naissanceADM_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.date_naissanceADM_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                                font=('Karla', 14))
        self.date_naissanceADM_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Wilaya
        self.wilayaADM_label = ct.CTkLabel(self.inscription_frame, text="Wilaya :", font=('Karla', 18))
        self.wilayaADM_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.wilayaADM_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                        font=('Karla', 14))
        self.wilayaADM_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Téléphone
        self.phone_nmbrADM_label = ct.CTkLabel(self.inscription_frame, text="Téléphone:", font=('Karla', 18))
        self.phone_nmbrADM_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbrADM_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                            font=('Karla', 14))
        self.phone_nmbrADM_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        # Matricule
        self.matricule_ADM_label = ct.CTkLabel(self.inscription_frame, text="Matricule :", font=('Karla', 18))
        self.matricule_ADM_label.grid(row=2, column=2, padx=20, pady=20, sticky="w")
        self.matricule_ADM_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                               font=('Karla', 14))
        self.matricule_ADM_entry.grid(row=2, column=3, padx=20, pady=20, sticky="w")

        # Load eye images
        self.open_eye_image = Image.open('eye open.png').resize((25, 25))
        self.close_eye_image = Image.open('close eye.png').resize((25, 25))
        self.open_eye = ImageTk.PhotoImage(self.open_eye_image)
        self.close_eye = ImageTk.PhotoImage(self.close_eye_image)

        # Mot de Passe
        self.MP_ADM_label = ct.CTkLabel(self.inscription_frame, text="Mot de passe :", font=('Karla', 18))
        self.MP_ADM_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        self.MP_ADM_entry = ct.CTkEntry(self.inscription_frame, show="*", width=250, height=35, corner_radius=10,
                                    font=('Karla', 14))
        self.MP_ADM_entry.grid(row=3, column=1, padx=20, pady=20, sticky="w")
        self.show_pass_button = Button(self.inscription_frame, image=self.close_eye, command=self.toggle_password,bd=0, bg='#FFFFFF', state=DISABLED)
        self.show_pass_button.place(x=665,y=380)

        # Confirmation Mot de Passe
        self.confirmation_MP_ADM_label = ct.CTkLabel(self.inscription_frame, text="Confirmation du mot de passe :",
                                                 font=('Karla', 18))
        self.confirmation_MP_ADM_label.grid(row=3, column=2, padx=20, pady=20, sticky="w")
        self.confirmation_MP_ADM_entry = ct.CTkEntry(self.inscription_frame, show="*", width=250, height=35,
                                                 corner_radius=10, font=('Karla', 16))
        self.confirmation_MP_ADM_entry.grid(row=3, column=3, padx=20, pady=20, sticky="w")
        self.show_confirm_pass_button = Button(self.inscription_frame, image=self.close_eye, command=self.toggle_confirm_password,bd=0, bg='#FFFFFF', state=DISABLED)
        self.show_confirm_pass_button.place(x=1540,y=380)

        # Bind key release event to password and confirmation password entries
        self.MP_ADM_entry.bind('<KeyRelease>', self.on_key_release)
        self.confirmation_MP_ADM_entry.bind('<KeyRelease>', self.on_key_release)

        # Button to Create Account
        self.enregistrer_ADM = ct.CTkButton(self.inscription_frame, text="Créer", command=self.creer, width=250,
                                            height=40, corner_radius=15, font=('Karla', 18, 'bold'), fg_color='#263A5F',
                                            cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_ADM.grid(row=4, column=1, columnspan=2, pady=20)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Redimensionne à la moitié de la taille originale
        label_image = Label(self.label_frame, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Garde une référence à l'image
        label_image.pack()  # Ajustez la position selon vos besoins

    def toggle_password(self):
        if self.MP_ADM_entry.cget('show') == '*':
            self.MP_ADM_entry.configure(show='')
            self.show_pass_button.configure(image=self.open_eye)
        else:
            self.MP_ADM_entry.configure(show='*')
            self.show_pass_button.configure(image=self.close_eye)

    def toggle_confirm_password(self):
        if self.confirmation_MP_ADM_entry.cget('show') == '*':
            self.confirmation_MP_ADM_entry.configure(show='')
            self.show_confirm_pass_button.configure(image=self.open_eye)
        else:
            self.confirmation_MP_ADM_entry.configure(show='*')
            self.show_confirm_pass_button.configure(image=self.close_eye)

    def on_key_release(self, event):
        if self.MP_ADM_entry.get() == '':
            self.show_pass_button.config(state=DISABLED)
        else:
            self.show_pass_button.config(state=NORMAL)

        if self.confirmation_MP_ADM_entry.get() == '':
            self.show_confirm_pass_button.config(state=DISABLED)
        else:
            self.show_confirm_pass_button.config(state=NORMAL)

    def creer(self):
        if self.nomADM_entry.get() == "" or self.prenomADM_entry.get() == "" or self.date_naissanceADM_entry.get() == "" or self.wilayaADM_entry.get() == "" or self.phone_nmbrADM_entry.get() == "" or self.matricule_ADM_entry.get() == "" or self.MP_ADM_entry.get() == "" or self.confirmation_MP_ADM_entry.get() == "":
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        elif self.MP_ADM_entry.get() != self.confirmation_MP_ADM_entry.get():
            messagebox.showerror("Erreur", "Les mots de passe ne sont pas conformes", parent=self)
        else:
            try:
                mydb = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                mycursor = mydb.cursor()
                mycursor.execute(
                    "insert into administrateur (matricule_administrateur,mot_de_passe,confirmer_mot_passe,nom,prenom,date_de_naissance,telephone,wilaya)values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.matricule_ADM_entry.get(),
                        self.MP_ADM_entry.get(),
                        self.confirmation_MP_ADM_entry.get(),
                        self.nomADM_entry.get(),
                        self.prenomADM_entry.get(),
                        self.date_naissanceADM_entry.get(),
                        self.phone_nmbrADM_entry.get(),
                        self.wilayaADM_entry.get()
                    ))
                messagebox.showinfo("Success", f"Administrateur enregistré", parent=self)
                mydb.commit()
                mydb.close()
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)


# Création d'une instance de la classe Inscrire et démarrage de la boucle principale
app = Inscrire()
app.mainloop()

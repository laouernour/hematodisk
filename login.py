import customtkinter as ct
from tkinter import *
from tkinter import messagebox
import pymysql
from datetime import datetime
from PIL import Image, ImageTk
import re
def wilaya():
    wilaya_list = ['01 Adrar','02 Chlef','03 Laghouat','04 Oum El Bouaghi','05 Batna','06 Béjaïa','07 Biskra','08 Béchar','09 Blida','10 Bouira',
                   '11 Tamanrasset','12 Tébessa','13 Tlemcen','14 Tiaret','15 Tizi Ouzou','16 Alger','17 Djelfa','18 Jijel','19 Sétif','20 Saïda',
                   '21 Skikda','22 Sidi Bel Abbès','23 Annaba','24 Guelma','25 Constantine','26 Médéa','27 Mostaganem','28 MSila','29 Mascara',
                   '30  Ouargla','31 Oran','32 El Bayadh','33 Illizi','34 Bordj Bou Arreridj','35 Boumerdès','36 El Tarf','37 Tindouf','38 Tissemsilt',
                   '39 El Oued','40 Khenchela','41 Souk Ahras','42 Tipaza','43 Mila','44 Aïn Defla','45 Naâma','46 Aïn Témouchent','47 Ghardaïa','48 Relizane','49 Timimmoun',
                   '50 Bordj Badji Mokhtar','53 Ouled Djellal','54 Béni Abbès','53 In Salah','54 Guessam','55 Touggourt','56 Djanet','57 El Mghair','58El Meniaa']
    return wilaya_list

def invalid_characters(entry):
    pattern = re.compile(r'[0-9!@#$%^&*(),.?":{}|<>/-]')
    return bool(pattern.search(entry))
def invalid_characters_numbr(entry):
    pattern1 = re.compile(r'[!@#$%^&*(),.?":{}|<>/-]')
    return bool(pattern1.search(entry))

def transform_date(date_str):
    # Convertit la date du format 'dd-mm-yyyy' au format 'yyyy-mm-dd'
    try:
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        return date_obj.strftime('%Y/%m/%d')
    except ValueError as e:
        messagebox.showerror("Erreur de date", f"Format de date incorrect: {date_str}. Utilisez le format 'jj-mm-aaaa'.\nErreur: {e}")
        return None

class Inscrire_ADM(ct.CTkToplevel):
    def __init__(self, parent):  # Add parent as an argument
        super().__init__(parent)
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
        self.wilayaADM_entry = ct.CTkComboBox(self.inscription_frame, width=250, height=35, corner_radius=10,
                                        font=('Karla', 14), values=wilaya())
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
        #validation_code
        self.validation_code_label = ct.CTkLabel(self.inscription_frame, text="Code de validation :",
                                                 font=('Karla', 18))
        self.validation_code_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        self.validation_code_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                                 font=('Karla', 14))
        self.validation_code_entry.grid(row=4, column=1, padx=20, pady=20, sticky="w")

        # Button to Create Account
        self.enregistrer_ADM = ct.CTkButton(self.inscription_frame, text="Créer", command=self.creer, width=250,
                                            height=40, corner_radius=15, font=('Karla', 18, 'bold'), fg_color='#263A5F',
                                            cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_ADM.grid(row=4, column=2, columnspan=2, pady=20)

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
        validation_code_attendu = '20245'  # Code de validation attendu, à remplacer par le code réel ou une vérification dynamique
        validation_code = self.validation_code_entry.get()

        if validation_code == validation_code_attendu:
            if self.nomADM_entry.get() == "" or self.prenomADM_entry.get() == "" or self.date_naissanceADM_entry.get() == "" or self.wilayaADM_entry.get() == "" or self.phone_nmbrADM_entry.get() == "" or self.matricule_ADM_entry.get() == "" or self.MP_ADM_entry.get() == "" or self.confirmation_MP_ADM_entry.get() == "":
                messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
            elif self.MP_ADM_entry.get() != self.confirmation_MP_ADM_entry.get():
                messagebox.showerror("Erreur", "Les mots de passe ne sont pas conformes", parent=self)
            else:
                if invalid_characters(self.nomADM_entry.get()) or invalid_characters(
                        self.prenomADM_entry.get()) or invalid_characters_numbr(
                        self.matricule_ADM_entry.get()) or invalid_characters_numbr(self.phone_nmbrADM_entry.get()):
                    messagebox.showerror("Erreur",
                                         "Les champs ne doivent pas contenir de chiffres ou de caractères spéciaux",
                                         parent=self)
                else:
                    try:
                        mydb = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                        mycursor = mydb.cursor()
                        mycursor.execute(
                            "INSERT INTO administrateur (matricule_administrateur, mot_de_passe, confirmer_mot_passe, nom, prenom, date_de_naissance, telephone, wilaya) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (
                                self.matricule_ADM_entry.get(),
                                self.MP_ADM_entry.get(),
                                self.confirmation_MP_ADM_entry.get(),
                                self.nomADM_entry.get(),
                                self.prenomADM_entry.get(),
                                transform_date(self.date_naissanceADM_entry.get()),
                                self.phone_nmbrADM_entry.get(),
                                self.wilayaADM_entry.get()
                            ))
                        messagebox.showinfo("Success", "Administrateur enregistré", parent=self)
                        mydb.commit()
                        self.vider()
                        mydb.close()
                    except Exception as es:
                        messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)
        else:
            messagebox.showerror("Erreur", "Code de validation incorrect", parent=self)

    #vider les cellules d'entrée
    def vider(self):
        self.matricule_ADM_entry.delete(0,END),
        self.MP_ADM_entry.delete(0,END),
        self.confirmation_MP_ADM_entry.delete(0,END),
        self.nomADM_entry.delete(0,END),
        self.prenomADM_entry.delete(0,END),
        self.date_naissanceADM_entry.delete(0,END),
        self.phone_nmbrADM_entry.delete(0,END),
        self.validation_code_entry.delete(0, 'end')


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

        self.toplevelADM_window = None

        def on_enter_user(e):
            self.user.delete(0, 'end')

        def on_leave_user(e):
            self.name = self.user.get()
            if self.name == '':
                self.user.insert(0, 'Entrer votre matricule')

        user_matricule = ct.CTkLabel(frame, text="Matricule :", text_color='#263A5F', font=('Karla', 20, 'bold'))
        user_matricule.place(x=80, y=120)
        self.user = ct.CTkEntry(frame, width=250, height=40, border_width=2, border_color='#263A5F',font=('Karla', 16))
        self.user.place(x=80,y=150)
        self.user.insert(0, 'Entrer votre matricule')
        self.user.bind('<FocusIn>', on_enter_user)
        self.user.bind('<FocusOut>', on_leave_user)

        def on_enter_pass(e):
            self.MP.delete(0, 'end')
            self.MP.configure(show='*')
        def on_leave_pass(e):
            self.name = self.MP.get()
            if self.name == '':
                self.MP.insert(0, 'Entrer votre mot de passe')

        motDP = ct.CTkLabel(frame, text="Mot De Passe :", text_color='#263A5F', font=('Karla', 20, 'bold'))
        motDP.place(x=80, y=200)
        self.MP = ct.CTkEntry(frame, width=250, height=40, border_width=2, border_color='#263A5F', font=('Karla', 16))
        self.MP.place(x=80, y=230)
        self.MP.insert(0, 'Entrer votre mot de passe')
        self.MP.bind('<FocusIn>', on_enter_pass)
        self.MP.bind('<FocusOut>', on_leave_pass)

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

        button = ct.CTkButton(frame, text="Se Connecter", width=150, height=50, corner_radius=15,
                               font=('Karla', 20, 'bold'), fg_color='#263A5F', cursor='hand2', text_color='#FFFFFF',
                               command=self.connecter)
        button.place(x=125, y=300)
        nouveau_AM = ct.CTkLabel(frame, text="Je n'ai pas de compte ", font=('Karla', 12), fg_color="transparent",
                                  text_color='#263A5F')
        nouveau_AM.place(x=100, y=370)
        inscrire = Button(frame, text="S'inscrire", font=('Karla', 12, 'bold'), border=0, bg='white', cursor='hand2',
                          activebackground='white', fg='#DD2F2E', command=self.open_toplevelADM)
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
                    self.destroy()
                    import accueil
                    mydb.close()
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)

    def open_toplevelADM(self):
        if self.toplevelADM_window is None or not self.toplevelADM_window.winfo_exists():
            self.toplevelADM_window = Inscrire_ADM(self)  # Pass self as an argument
            self.toplevelADM_window.grab_set()  # Make the new window modal
        else:
            self.toplevelADM_window.focus()  # if window exists focus it


Login_page = login()
Login_page.mainloop()

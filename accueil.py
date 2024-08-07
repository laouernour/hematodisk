import customtkinter as ct
from tkinter import  ttk
from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk
import re
def get_medical_gestures_from_db():
    try:
        # Connect to the database
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()

        # Execute a query to fetch all medical gestures
        cur.execute("SELECT geste FROM geste_medicale")

        # Fetch all rows
        gestes = [row[0] for row in cur.fetchall()]

        # Close the database connection
        con.close()

        return gestes
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la récupération des gestes médicaux depuis la base de données : {str(e)}")
def wilaya():
    wilaya_list = ['01 Adrar', '02 Chlef', '03 Laghouat', '04 Oum El Bouaghi', '05 Batna', '06 Béjaïa', '07 Biskra','08 Béchar', '09 Blida','10 Bouira',
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

class Inscrire(ct.CTkToplevel):
    #Médecin
    def __init__(self, parent):  # Add parent as an argument
        super().__init__(parent)
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#263A5F')
        self.bind('<Return>', self.creer)


        self.formulaire_frame = ct.CTkFrame(self, fg_color='#FFFFFF', width=w, height=h, border_width=2,
                                            border_color='#263A5F')
        self.formulaire_frame.pack(expand=True, fill='both')

        # Frame for doctor
        self.label_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.label_frame.pack(pady=10)

        self.label = ct.CTkLabel(self.label_frame, text="Inscrire Docteur :", font=('Karla', 26,'bold'))
        self.label.pack(expand=True, pady=20)

        # Frame for inscription form using grid
        self.inscription_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.inscription_frame.pack(pady=10)

        # Nom and Prénom in the same row
        self.nom_label = ct.CTkLabel(self.inscription_frame, text="Nom :", font=('Karla', 18))
        self.nom_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.nom_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10, font=('Karla', 14))
        self.nom_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenom_label = ct.CTkLabel(self.inscription_frame, text="Prénom :", font=('Karla', 18))
        self.prenom_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")
        self.prenom_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                        font=('Karla', 14))
        self.prenom_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Téléphone
        self.phone_nmbr_label = ct.CTkLabel(self.inscription_frame, text="Téléphone:", font=('Karla', 18))
        self.phone_nmbr_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbr_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                            font=('Karla', 14))
        self.phone_nmbr_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Matricule
        self.matricule_doctor_label = ct.CTkLabel(self.inscription_frame, text="Matricule Médecin:", font=('Karla', 18))
        self.matricule_doctor_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.matricule_doctor_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                                  font=('Karla', 14))
        self.matricule_doctor_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Grad
        self.grad_label = ct.CTkLabel(self.inscription_frame, text="Grade:", font=('Karla', 18))
        self.grad_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        grad = ["Généraliste", "Résident", "Assistant", "Maître Assistant", "Professeur"]
        self.grad_entry = ct.CTkComboBox(self.inscription_frame, values=grad, dropdown_font=('Karla', 14), width=250,
                                         height=35, corner_radius=10,
                                         font=('Karla', 14), dropdown_fg_color='#FFFFFF')
        self.grad_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        # Button to Create Account
        self.enregistrer_doctor = ct.CTkButton(self.inscription_frame, text="Créer", command=self.creer, width=250,
                                            height=40, corner_radius=15, font=('Karla', 18, 'bold'), fg_color='#263A5F',
                                            cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_doctor.grid(row=3, column=1, columnspan=2, pady=10)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Redimensionne à la moitié de la taille originale
        label_image = Label(self.label_frame, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Garde une référence à l'image
        label_image.pack()  # Ajustez la position selon vos besoins

    def creer(self,event=None):
        # Vérification des champs obligatoires
        if (self.nom_entry.get() == "" or self.prenom_entry.get() == "" or  self.phone_nmbr_entry.get() == ""
                or self.matricule_doctor_entry.get() == ""):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        else:
            # Vérification des caractères non autorisés dans les champs

            if (invalid_characters(self.nom_entry.get()) or
                    invalid_characters(self.prenom_entry.get()) or
                    invalid_characters_numbr(self.phone_nmbr_entry.get()) or
                    invalid_characters_numbr(self.matricule_doctor_entry.get())):

                messagebox.showerror("Erreur",
                                     "Les champs ne doivent pas contenir de chiffres ou de caractères spéciaux",
                                     parent=self)
            else:
                try:
                    mydb = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                    mycursor = mydb.cursor()
                    mycursor.execute(
                        "insert into medecin (matricule_medecin,nom,prenom,telephone,grade)values(%s,%s,%s,%s,%s)",
                        (
                            self.matricule_doctor_entry.get(),
                            self.nom_entry.get(),
                            self.prenom_entry.get(),
                            self.phone_nmbr_entry.get(),
                            self.grad_entry.get(),
                        ))
                    messagebox.showinfo("Success", "Médecin enregistré", parent=self)
                    mydb.commit()
                    self.vider()
                    mydb.close()
                except Exception as es:
                    messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)

    def vider(self):
        self.matricule_doctor_entry.delete(0, END),
        self.nom_entry.delete(0, END),
        self.prenom_entry.delete(0, END),
        self.phone_nmbr_entry.delete(0, END),



class Inscrire_patient(ct.CTkToplevel):
    def __init__(self, parent):  # Add parent as an argument
        super().__init__(parent)
        self.title("S'inscrire")
        self.geometry('850x590+300+50')
        self.configure(bg='#263A5F')
        self.resizable(False, False)


        self.formulaire_frame = ct.CTkFrame(self, fg_color='#FFFFFF', width=800, height=490, border_width=2,
                                            border_color='#263A5F',corner_radius= 0)
        self.formulaire_frame.pack(expand=True, fill='both')

        # Frame for the title label
        self.label_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.label_frame.pack(pady=2)

        self.label = ct.CTkLabel(self.label_frame, text="Inscrire Patient :", font=('Karla', 18, 'bold'))
        self.label.pack(expand=True, pady=10)

        # Frame for inscription form using grid
        self.inscription_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.inscription_frame.pack(pady=10)

        # Nom and Prénom in the same row du patient
        self.nomP_label = ct.CTkLabel(self.inscription_frame, text="Nom :", font=('Karla', 16))
        self.nomP_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.nomP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                      font=('Karla', 14))
        self.nomP_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        self.prenomP_label = ct.CTkLabel(self.inscription_frame, text="Prénom :", font=('Karla', 16))
        self.prenomP_label.grid(row=0, column=2, padx=20, pady=10, sticky="w")
        self.prenomP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                         font=('Karla', 14))
        self.prenomP_entry.grid(row=0, column=3, padx=20, pady=10, sticky="w")

        # Matricule
        self.matriculeP_label = ct.CTkLabel(self.inscription_frame, text="Matricule :", font=('Karla', 16))
        self.matriculeP_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.matriculeP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                            font=('Karla', 14))
        self.matriculeP_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Date de Naissance
        self.date_naissanceP_label = ct.CTkLabel(self.inscription_frame, text="Date de Naissance :", font=('Karla', 16))
        self.date_naissanceP_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.date_naissanceP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                                 font=('Karla', 14))
        self.date_naissanceP_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Wilaya
        self.wilayaP_label = ct.CTkLabel(self.inscription_frame, text="Wilaya :", font=('Karla', 16))
        self.wilayaP_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.wilayaP_entry = ct.CTkComboBox(self.inscription_frame, width=200, height=30, corner_radius=10,
                                            font=('Karla', 14), values=wilaya())
        self.wilayaP_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        # Téléphone
        self.phone_nmbrP_label = ct.CTkLabel(self.inscription_frame, text="Téléphone:", font=('Karla', 16))
        self.phone_nmbrP_label.grid(row=2, column=2, padx=20, pady=20, sticky="w")
        self.phone_nmbrP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                             font=('Karla', 14))
        self.phone_nmbrP_entry.grid(row=2, column=3, padx=20, pady=20, sticky="w")

        # Sexe
        self.sexe_Patient_label = ct.CTkLabel(self.inscription_frame, text="Sexe :", font=('Karla', 16))
        self.sexe_Patient_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        sexe = ['Homme', 'Femme']
        self.sexe_Patient_entry = ct.CTkComboBox(self.inscription_frame, width=200, height=30, corner_radius=10,
                                                 values=sexe, dropdown_fg_color='#FFFFFF',
                                                 font=('Karla', 14))
        self.sexe_Patient_entry.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        # Groupage
        self.groupage_label = ct.CTkLabel(self.inscription_frame, text="Groupage: ", font=('Karla', 16))
        self.groupage_label.grid(row=3, column=2, padx=20, pady=20, sticky="w")
        groupage = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        self.groupage_entry = ct.CTkComboBox(self.inscription_frame, values=groupage, dropdown_font=('Karla', 14),
                                             width=200)

        self.groupage_entry = ct.CTkComboBox(self.inscription_frame, values=groupage, dropdown_font=('Karla', 14),
                                             width=200, height=30, corner_radius=10, font=('Karla', 14),
                                             dropdown_fg_color='#FFFFFF')
        self.groupage_entry.grid(row=3, column=3, padx=20, pady=20, sticky="w")
        # Antecedents
        self.antecedents_label = ct.CTkLabel(self.inscription_frame, text="Antécédents", font=('Karla', 16))
        self.antecedents_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        self.antecedents_entry = ct.CTkTextbox(self.inscription_frame, width=200, height=100, corner_radius=10,
                                               font=('Karla', 14))
        self.antecedents_entry.grid(row=4, column=1, columnspan=3, padx=20, pady=20, sticky="w")

        # diagnostique
        self.diagnostique_label = ct.CTkLabel(self.inscription_frame, text="Diagnostique", font=('Karla', 16))
        self.diagnostique_label.grid(row=4, column=2, padx=20, pady=20, sticky="w")
        self.diagnostique_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                               font=('Karla', 14))
        self.diagnostique_entry.grid(row=4, column=3, columnspan=3, padx=20, pady=20, sticky="w")


        # Button to Create Account
        self.enregistrer_patient = ct.CTkButton(self.inscription_frame, text="Créer", command=self.creer, width=250,
                                                height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                                fg_color='#263A5F',
                                                cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_patient.grid(row=5, column=1, columnspan=2,  pady=0)
        # Liaison de la touche "Enter" à la fonction submit_form
        self.bind('<Return>', self.creer)

        # Load the image

        image_path = 'Hemato Desk logo.png'  # Ensure this path is correct
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(3, 3)  # Resize to one-third of the original size

        # Create the Label with the image
        label_image = Label(self.label_frame, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Keep a reference to the image to prevent garbage collection
        label_image.pack()

    def creer(self, event=None):
        if (
                self.nomP_entry.get() == "" or self.prenomP_entry.get() == "" or self.matriculeP_entry.get() == "" or self.date_naissanceP_entry.get() == ""
                or self.wilayaP_entry.get() == "" or self.phone_nmbrP_entry.get() == ""):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)

        # Vérifier les entrées
        else:
            if invalid_characters(self.nomP_entry.get()) or invalid_characters(
                    self.prenomP_entry.get()) or invalid_characters_numbr(self.phone_nmbrP_entry.get()):
                messagebox.showerror("Erreur",
                                     "Les champs ne doivent pas contenir de chiffres ou de caractères spéciaux",
                                     parent=self)
                return
            else:
                try:
                    # Établir une connexion à la base de données
                    con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                    cur = con.cursor()

                    # Vérifier si le matricule du patient existe déjà
                    cur.execute("SELECT * FROM patient WHERE matricule_patient = %s", (self.matriculeP_entry.get(),))
                    if cur.fetchone():
                        messagebox.showerror("Erreur", "Le patient existe déjà", parent=self)
                        return

                    # Récupération du matricule_administrateur à partir de la table administrateur
                    cur.execute("SELECT matricule_administrateur FROM administrateur")
                    matricule_administrateur = cur.fetchone()[0]

                    # Insertion des données dans la table patient avec vérification de l'existence du matricule_administrateur
                    cur.execute("""
                               INSERT INTO patient (matricule_patient, nom, prenom, date_de_naissance, sexe, wilaya, telephone, groupage, antecedents,diagnostique, FKmatricule_administrateur) 
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
                           """,
                                (
                                    self.matriculeP_entry.get(), self.nomP_entry.get(), self.prenomP_entry.get(),
                                    transform_date(self.date_naissanceP_entry.get()), self.sexe_Patient_entry.get(),
                                    self.wilayaP_entry.get(), self.phone_nmbrP_entry.get(),
                                    self.groupage_entry.get(), self.antecedents_entry.get("1.0", END),self.diagnostique_entry.get(),
                                    matricule_administrateur
                                ))

                    # Committez les changements
                    con.commit()
                    messagebox.showinfo("Succès", "Inscription réussie", parent=self)

                except Exception as e:
                    messagebox.showerror("Erreur", f"Erreur lors de l'inscription : {str(e)}", parent=self)
                    print(str(e))
                finally:
                    # Fermez la connexion
                    if con:
                        self.vider()
                        con.close()

    def vider(self):
        self.nomP_entry.delete(0, END),
        self.prenomP_entry.delete(0, END),
        self.matriculeP_entry.delete(0,END),
        self.date_naissanceP_entry.delete(0, END),
        self.phone_nmbrP_entry.delete(0, END),
        self.antecedents_entry.delete("1.0", END)

class Accueil(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Accueil")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.resizable(False,True)
        self.configure(bg='#78BDCC')
        # Top frame
        self.top_frame = ct.CTkFrame(self, fg_color='#28A0C6', width=w, height=200, corner_radius=0)
        self.top_frame.place(x=0, y=0)
        label_text = Label(self.top_frame, text="Service Hématologie", font=('Karla', 48, 'bold'), bg="#28A0C6")
        label_text.place(x=750, y=60)
        #ajouter geste medicale
        self.ajouter_geste_button = ct.CTkButton(self.top_frame, text="+ Geste", command=self.geste_medicale,
                                                 width=125, height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                                 fg_color='#00555D', cursor='hand2', text_color='#FFFFFF')
        self.ajouter_geste_button.place(x=910, y=120)

        #button ajouter patient
        self.ajouter_patient = ct.CTkButton(self.top_frame, text="+ Ajouter Patient", command=self.open_toplevelP,
                                            width=200, height=40,
                                            corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#EF3535',
                                            cursor='hand2', text_color='#FFFFFF')
        self.ajouter_patient.place(x=1050, y=120)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(1, 1)  # Resize to half the original size
        label_imageL = Label(self.top_frame, image=nouvelle_image, bg="#28A0C6")
        label_imageL.image = nouvelle_image  # Keep a reference to the image
        label_imageL.place(x=50, y=0)

        # Recherche
        self.rech_txt = ct.CTkEntry(self.top_frame, width=300, height=35, corner_radius=10,
                                    font=('Karla', 14))
        self.rech_txt.place(x=250, y=130)
        self.rech_txt_butt = ct.CTkButton(self.top_frame, text="Recherche", command=self.rechercher_patient, width=110,
                                          height=30,
                                          corner_radius=15, font=('Karla', 14, 'bold'), fg_color='#2FC16A',
                                          cursor='hand2', text_color='#FFFFFF')
        self.rech_txt_butt.place(x=555, y=132)
        self.rech_txt.focus_set()
        self.rech_txt.bind('<Return>', self.rechercher_patient)


        # Left frame
        self.left_frame = ct.CTkFrame(self, fg_color='#28A0C6', width=250, height=h - 240, corner_radius=0)
        self.left_frame.place(x=0, y=200)
        # Down frame
        self.down_frame = ct.CTkFrame(self, fg_color='#28A0C6', width=1600, height=50, corner_radius=0)
        self.down_frame.place(x=0, y=self.winfo_screenheight() - 95)

        # Ajouter votre nom
        label_nom = Label(self.down_frame, text="Rèaliser par : - AFANE NORHAN AMARIA : afanenorhan@gmail.com et - LAOUER NOUR EL IMENE : laouernourelimene@yahoo.com", font=('Karla', 11, 'bold'), bg="#28A0C6")
        label_nom.place(x=800, y=10)

        # Ajouter le logo
        image_path = 'logo univ 1.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Resize to half the original size
        label_imageL = Label(self.down_frame, image=nouvelle_image, bg="#28A0C6")
        label_imageL.image = nouvelle_image  # Keep a reference to the image
        label_imageL.place(x=1808, y=0)

        buttons_info = [
            ("Liste des Patients", self.show_patients_tab),
            ("Consultation", self.show_consultations),
            ("Liste des Rendez-vous", self.show_appointments_tab),
            ("Ajouter Médecin", self.report_appointments),
            ("Liste des Médecin", self.show_doctors_tab),
            ("Statistique", self.create_statistics_frame),
            ("Paramètres", self.show_settings)
        ]

        for idx, (text, command) in enumerate(buttons_info):
            button = ct.CTkButton(self.left_frame, text=text, command=command, width=200,
                                  height=45, corner_radius=15, font=('Karla', 16, 'bold'), fg_color="transparent",
                                  cursor='hand2', text_color='#FFFFFF', hover_color="#1E88E5")
            button.place(x=25, y=30 + 58 * idx)

        # Center frame
        self.center_frame = ct.CTkFrame(self, fg_color='#ffffff', border_width=2, border_color='#263A5F', width=w - 260, height=h - 270, corner_radius=0)
        self.center_frame.place(x=250, y=200)
        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.rowconfigure(0, weight=1)

        self.show_consultations()  # Appel sans argument explicite

        def show_consultations(self, center_frame=None):
            if center_frame is None:
                center_frame = self.center_frame
            print(f"Affichage des consultations pour: {center_frame}")
            # Implémentez la logique de la méthode en utilisant center_frame

        self.toplevelDocteur_window = None
        self.toplevelP_window = None
        self.toplevelRDV_window = None

    def geste_medicale(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()
        self.geste_label = ct.CTkLabel(self.center_frame, text="Nouveau Geste Médicale :", font=('Karla', 22, 'bold'),
                                       text_color='#263A5F')
        self.geste_label.place(x=350, y=100)

        self.geste_entry = ct.CTkEntry(self.center_frame, width=200, height=35, corner_radius=10, font=('Karla', 14))
        self.geste_entry.place(x=385, y=150)
        self.bind('<Return>', self.ajouter_geste)


        self.ajouter_g_button = ct.CTkButton(self.center_frame, text="Ajouter", command=self.ajouter_geste,
                                             width=110, height=30, corner_radius=15, font=('Karla', 14, 'bold'),
                                             cursor='hand2', text_color='#FFFFFF')
        self.ajouter_g_button.place(x=420, y=200)

    def ajouter_geste(self,event=None):
        geste = self.geste_entry.get()
        if geste == "":
            messagebox.showerror("Erreur", "Le champ de geste médicale est vide", parent=self.center_frame)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()

                # Vérifiez si le geste existe déjà
                cur.execute("SELECT * FROM geste_medicale WHERE geste = %s", (geste,))
                result = cur.fetchone()

                if result:
                    messagebox.showerror("Erreur", "Le geste médicale existe déjà", parent=self.center_frame)
                else:
                    # Insertion du nouveau geste dans la table geste_medicle
                    cur.execute("INSERT INTO geste_medicale (geste) VALUES (%s)", (geste,))
                    con.commit()
                    messagebox.showinfo("Succès", "Geste médicale ajouté avec succès", parent=self.center_frame)

                con.close()
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self.center_frame)

    def rechercher_patient(self,event=None):
        nom_prenom = self.rech_txt.get().split()  # Récupérer le nom et prénom du patient saisi dans la barre de recherche

        if self.current_search_list == "patients":
            # Rechercher dans la liste des patients
            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
            cur = con.cursor()

            if len(nom_prenom) == 1:
                # Rechercher par nom ou prénom ou matricule
                cur.execute(
                    "SELECT matricule_patient, nom, prenom, date_de_naissance, telephone, groupage, Antecedents  FROM patient WHERE nom LIKE %s OR prenom LIKE %s OR matricule_patient LIKE %s",
                    (f"%{nom_prenom[0]}%", f"%{nom_prenom[0]}%", f"%{nom_prenom[0]}%"))
            else:
                # Rechercher par nom et prénom
                nom, prenom = nom_prenom
                cur.execute(
                    "SELECT matricule_patient, nom, prenom, date_de_naissance, telephone, groupage, Antecedents  FROM patient WHERE nom LIKE %s AND prenom LIKE %s",
                    (f"%{nom}%", f"%{prenom}%"))

            patients = cur.fetchall()

            # Effacer le Treeview
            for item in self.treeview_patients.get_children():
                self.treeview_patients.delete(item)

            # Ajouter les patients trouvés dans le Treeview
            for patient in patients:
                self.add_patient(self.treeview_patients, patient)
            # Supprimer le texte de la barre de recherche
            self.rech_txt.delete(0, 'end')
            con.close()


        elif self.current_search_list == "rdv":

            # Recherche dans la liste des rendez-vous

            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')

            cur = con.cursor()

            recherche = " ".join(nom_prenom)

            if len(nom_prenom) == 1:
                cur.execute(
                    "SELECT id_rendez_vous, patient, date_du_rendez_vous, geste_medical FROM rendez_vous WHERE patient LIKE %s",
                    (f"%{recherche}%",)
                )
            else:
                nom, prenom = nom_prenom
                cur.execute(
                    "SELECT id_rendez_vous, patient, date_du_rendez_vous, geste_medical FROM rendez_vous WHERE patient LIKE %s AND patient LIKE %s",
                    (f"%{nom}%", f"%{prenom}%")
                )

            rdv = cur.fetchall()

            # Effacer le Treeview
            for item in self.treeview_appointments.get_children():
                self.treeview_appointments.delete(item)

            # Ajouter les rendez-vous trouvés dans le Treeview
            for rendez_vous in rdv:
                self.add_appointment(self.treeview_appointments, rendez_vous)

            # Supprimer le texte de la barre de recherche
            self.rech_txt.delete(0, 'end')

            con.close()

    def create_patients_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff",
                        font=('Karla', 16), rowheight=61)
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 18, 'bold'), foreground="#1C1278")

        # Tableau Treeview
        columns = ('ID', 'Nom', 'Prénom', 'Age', 'Téléphone', 'Groupage','Diagnostique', 'Antécédent')
        self.treeview_patients = ttk.Treeview(self.center_frame, columns=columns, show='headings',
                                              style="Custom.Treeview")

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.center_frame, orient="vertical", command=self.treeview_patients.yview)
        scrollbar.pack(side="right", fill="y")
        self.treeview_patients.configure(yscrollcommand=scrollbar.set)

        self.treeview_patients.pack(expand=True, fill='both')

        # Définition des en-têtes
        for col in columns:
            self.treeview_patients.heading(col, text=col, anchor='center')
            width = 100 if col == "ID" else 201
            self.treeview_patients.column(col, anchor='center', width=width)

    def create_appointments_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff",
                        rowheight=60,
                        font=('Karla', 16))
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 26, 'bold'))

        columns = ('N°RDV', 'Patient', 'Date','geste_medical')
        self.treeview_appointments = ttk.Treeview(self.center_frame, columns=columns, show='headings',
                                                  style="Custom.Treeview")
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.center_frame, orient="vertical", command=self.treeview_appointments.yview)
        scrollbar.pack(side="right", fill="y")
        self.treeview_appointments.configure(yscrollcommand=scrollbar.set)
        self.treeview_appointments.pack(expand=True, fill='both')

        # Définition des en-têtes
        for col in columns:
            self.treeview_appointments.heading(col, text=col, anchor='center')
            width = 253 if col == "N°RDV" else 419
            self.treeview_appointments.column(col, anchor='center',width=width)

        self.treeview_appointments.bind("<Button-1>", self.on_click_RDV)

    def create_doctor_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff", font=('Karla', 16), rowheight=60)
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 26, 'bold'))

        # Treeview Table
        columns = ('Matricule', 'Nom','Prénom', 'Grade', 'Téléphone')
        self.treeview_doctors = ttk.Treeview(self.center_frame, columns=columns, show='headings',
                                                  style="Custom.Treeview")
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.center_frame, orient="vertical", command=self.treeview_doctors.yview)
        scrollbar.pack(side="right", fill="y")
        self.treeview_doctors.configure(yscrollcommand=scrollbar.set)
        self.treeview_doctors.pack(expand=True, fill='both')

        # Définition des en-têtes
        for col in columns:
            self.treeview_doctors.heading(col, text=col, anchor='center')
            width = 250 if col == "N°RDV" else 301
            self.treeview_doctors.column(col, anchor='center',width=width )

    def add_patient(self, treeview, row):
        # Insérer une ligne dans le Treeview avec les données du patient
        treeview.insert('', 'end', values=row)

    def add_doctor(self, treeview, row):
        treeview.insert('', 'end', values=row)

    def add_appointment(self, treeview, row):
        treeview.insert('', 'end', values=row)

    def show_patients_tab(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        self.current_search_list = "patients"

        # Create and display the treeview for patients
        self.create_patients_treeview()
        # Clear the Treeview
        for item in self.treeview_patients.get_children():
            self.treeview_patients.delete(item)

        try:
            # Connect to the database
            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
            cur = con.cursor()

            # Fetch patient data from the table
            cur.execute(
                "SELECT matricule_patient, nom, prenom, age, telephone, groupage, diagnostique, Antecedents FROM patient")
            rows = cur.fetchall()
            for row in rows:
                # Add patient to the treeview
                self.add_patient(self.treeview_patients, row)

            # Bind the click event to the on_click function
            self.treeview_patients.bind("<Button-1>", self.on_click)
        except Exception as e:
            print(f"Error connecting to database: {e}")
        finally:
            con.close()

    def on_click(self, event):
        # Get the item clicked
        item_id = self.treeview_patients.identify_row(event.y)
        if not item_id:
            return

        # Fetch the values for the clicked item
        values = self.treeview_patients.item(item_id, 'values')
        if values:
            # Ouvre une nouvelle fenêtre avec les valeurs de l'élément
            self.new_window = ct.CTkToplevel(self)
            self.new_window .grab_set()
            self.new_window.title("Détails du Patient")
            self.new_window.geometry("790x500+400+200")
            # Configure la fenêtre pour désactiver le redimensionnement en largeur et autoriser le redimensionnement en hauteur
            self.new_window.resizable(width=False, height=False)


            self.menu_frame = ct.CTkFrame(self.new_window, width=790, height=50, border_width=0,corner_radius=0,
                                     fg_color='#B8F9FF')
            self.menu_frame.pack()

            show_butt = ct.CTkButton(self.menu_frame, text="Voir dossier patient", command=lambda: self.afficher_informations_patient(self.info_frame, values), width=50, height=30,
                                     corner_radius=15, font=('Karla', 14, 'bold'), fg_color='#FF0000', cursor='hand2',
                                     text_color='#FFFFFF')
            show_butt.place(x=20, y=10)

            history_butt = ct.CTkButton(self.menu_frame, text="Voir suivi patient", command=lambda: self.afficher_suivi_patient(values[0]), width=50, height=30,
                                        corner_radius=15, font=('Karla', 14, 'bold'), fg_color='#FF0000', cursor='hand2',
                                        text_color='#FFFFFF')
            history_butt.place(x=210, y=10)

            modifier_butt = ct.CTkButton(self.menu_frame, text="Consultation", command=lambda: self.ajouter_consultation_patient(self.info_frame, values[0], values[1]),
                                         corner_radius=15, font=('Karla', 14, 'bold'), fg_color='#FF0000', cursor='hand2',
                                         text_color='#FFFFFF')
            modifier_butt.place(x=385, y=10)

            rdv_butt = ct.CTkButton(self.menu_frame, text="Prochain Rendez_vous",
                                         command=lambda: self.ajouter_rdv_prochain(self.info_frame,values[0], values[1], values[2]),
                                         corner_radius=15, font=('Karla', 14, 'bold'), fg_color='#FF0000',
                                         cursor='hand2',
                                         text_color='#FFFFFF')
            rdv_butt.place(x=555, y=10)

            self.info_frame = ct.CTkFrame(self.new_window, width=697, height=550, border_color='#FF0000', border_width=2,
                                          fg_color='transparent')
            self.info_frame.pack(fill='both', expand=True)
            # Appeler afficher_informations_patient pour afficher les informations par défaut
            self.afficher_informations_patient(self.info_frame, values)

    def afficher_informations_patient(self, info_frame, values):
        for widget in self.info_frame.winfo_children():
            widget.destroy()
        # Crée un cadre pour afficher les informations du patient
        details_frame = ct.CTkScrollableFrame(self.info_frame, fg_color='#ffffff')
        details_frame.pack(fill='both', expand=True)
        #Modifier dossier patient
        self.modifier_butt=ct.CTkButton(details_frame, text="Modifier ", command=lambda: self.modifier_patient(values), width=250,
                                                height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                                fg_color='#263A5F',
                                                cursor='hand2', text_color='#FFFFFF')
        self.modifier_butt.grid(row=8, column=2, columnspan=2, pady=20)

        # Ajoute des libellés pour afficher les détails du patient
        labels = ['Matricule:', 'Nom:', 'Prénom:', 'Age:', 'Téléphone:', 'Groupage:','Diagnostique:','Antécédent:']
        for i, (label_text, value) in enumerate(zip(labels, values)):
            label = ct.CTkLabel(details_frame, text=label_text, font=('Karla', 16))
            label.grid(row=i, column=0, sticky='w', padx=10, pady=5)
            value_label = ct.CTkLabel(details_frame, text=value, font=('Karla', 16))
            value_label.grid(row=i, column=1, sticky='w', padx=10, pady=5)

    def modifier_patient(self, values):
        try:
            # Établir une connexion à la base de données
            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
            cur = con.cursor()

            # Récupérer les antécédents et le numéro de téléphone actuels du patient
            cur.execute("""
                SELECT matricule_patient ,antecedents,diagnostique, telephone
                FROM patient
                WHERE nom = %s AND prenom = %s
            """, (values[1], values[2]))  # Utilise les valeurs passées comme arguments

            patient_info = cur.fetchone()

            # Si des informations sont disponibles, afficher la fenêtre de modification
            if patient_info:
                for widget in self.info_frame.winfo_children():
                    widget.destroy()
                    # Crée un cadre pour afficher les informations du patient
                modification_frame = ct.CTkFrame(self.info_frame, fg_color='#ffffff')
                modification_frame.grid(row=0, column=0, sticky="nsew")
                self.info_frame.grid_rowconfigure(0, weight=1)
                self.info_frame.grid_columnconfigure(0, weight=1)

                self.matriculeP_label = ct.CTkLabel(modification_frame, text="Matricule :", font=('Karla', 16))
                self.matriculeP_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
                self.matriculeP_entry = ct.CTkEntry(modification_frame, width=200, height=30, corner_radius=10,
                                                    font=('Karla', 14))
                self.matriculeP_entry.insert(0, patient_info[0])  # Afficher le matricule du patient
                self.matriculeP_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

                # Création des widgets pour la modification
                self.antecedents_label = ct.CTkLabel(modification_frame, text="Antécédents :", font=('Karla', 14))
                self.antecedents_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
                self.antecedents_entry = ct.CTkTextbox(modification_frame, font=('Karla', 14))
                self.antecedents_entry.insert("1.0", patient_info[1])  # Afficher les antécédents actuels
                self.antecedents_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

                # Création des widgets pour la nouvelle fenêtre
                self.diagnostique_label = ct.CTkLabel(modification_frame, text="Diagnostique :", font=('Karla', 14))
                self.diagnostique_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")
                self.diagnostique_entry = ct.CTkEntry(modification_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
                self.diagnostique_entry.insert(0, patient_info[2])  # Afficher les antécédents actuels
                self.diagnostique_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")


                self.telephone_label = ct.CTkLabel(modification_frame, text="Numéro de téléphone :", font=('Karla', 14))
                self.telephone_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
                self.telephone_entry = ct.CTkEntry(modification_frame, font=('Karla', 14))
                self.telephone_entry.insert(0, patient_info[3])  # Afficher le numéro de téléphone actuel
                self.telephone_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

                # Ajouter une lambda pour passer les valeurs du nom et du prénom à la fonction enregistrer
                self.enregistrer_button = ct.CTkButton(modification_frame, text="Enregistrer",
                                                       command=lambda: self.enregistrer(values[1], values[2]), font=('Karla', 14))
                self.enregistrer_button.grid(row=3, column=0, columnspan=2, pady=10)
                self.enregistrer_button.focus_set()
                self.bind_all('<Return>', lambda event: self.enregistrer(values[1], values[2]))

        except Exception as e:
            # Afficher une erreur en cas de problème
            messagebox.showerror("Erreur", f"Erreur lors de la récupération des informations du patient : {str(e)}",
                                 parent=self)
            print(str(e))
        finally:
            # Fermer la connexion à la base de données
            if con:
                con.close()

    def enregistrer(self, nom, prenom):
        if invalid_characters_numbr(self.telephone_entry.get()):
            messagebox.showerror("Erreur", "Le numéro de téléphone ne doit pas contenir de caractères spéciaux",
                                 parent=self)
            return
        else:
            try:
                # Établir une connexion à la base de données
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                # Mise à jour des antécédents et du numéro de téléphone du patient dans la base de données
                cur = con.cursor()
                cur.execute("""
                    UPDATE patient 
                    SET  matricule_patient = %s,antecedents = %s, telephone = %s,diagnostique = %s
                    WHERE nom = %s AND prenom = %s
                """, (
                    self.matriculeP_entry.get(),
                    self.antecedents_entry.get("1.0", END),
                    self.telephone_entry.get(),
                    self.diagnostique_entry.get(),
                    nom,
                    prenom
                ))
                con.commit()
                messagebox.showinfo("Succès", "Les modifications ont été enregistrées avec succès", parent=self)
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement des modifications : {str(e)}",
                                     parent=self)
                print(str(e))


    def afficher_suivi_patient(self, matricule_patient):
        try:
            # Établir une connexion à la base de données
            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
            cur = con.cursor()

            # Requête SQL pour obtenir les consultations du patient avec les noms des médecins
            cur.execute(
                """
                SELECT hc.date_de_consultation, hc.geste_medical, hc.diagnostique,hc.traitement, m.nom AS medecin
                FROM historique_consultations hc
                JOIN medecin m ON hc.matricule_medecin = m.matricule_medecin
                WHERE hc.matricule_patient = %s AND hc.date_de_consultation <= %s
                """,
                (matricule_patient, datetime.now().date())
            )
            rows = cur.fetchall()

            # Afficher les consultations dans un nouveau cadre
            for widget in self.info_frame.winfo_children():
                widget.destroy()

            consultations_frame = ct.CTkScrollableFrame(self.info_frame, fg_color='#ffffff', corner_radius=0)
            consultations_frame.pack(fill='both', expand=True)

            # Ajouter des libellés pour les colonnes
            headers = ['Date de Consultation', 'Geste Médical', 'CAT','Traitement', 'Médecin traitant']
            for i, header in enumerate(headers):
                header_label = ct.CTkLabel(consultations_frame, text=header, font=('Karla', 16, 'bold'))
                header_label.grid(row=0, column=i, padx=10, pady=5)

            # Ajouter les consultations
            for row_num, row in enumerate(rows, start=1):
                for col_num, value in enumerate(row):
                    value_label = ct.CTkLabel(consultations_frame, text=value, font=('Karla', 14))
                    value_label.grid(row=row_num, column=col_num, padx=10, pady=5)

        except Exception as e:
            # Afficher une erreur en cas de problème
            messagebox.showerror("Erreur", f"Erreur lors de la récupération des consultations : {str(e)}", parent=self)
            print(str(e))
        finally:
            # Fermer la connexion à la base de données
            if con:
                con.close()

    def ajouter_consultation_patient(self, window, matricule_patient, nom_patient):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

        # Crée un cadre pour afficher les informations du patient
        Consultation_frame = ct.CTkFrame(window, fg_color='#ffffff')
        Consultation_frame.pack(fill='both', expand=True)

        # Date de création
        self.titre_label = ct.CTkLabel(Consultation_frame, text="Ajouter une consultation :",
                                       font=('Karla', 18, 'bold'),
                                       text_color='#263A5F')
        self.titre_label.grid(row=0,column=1,padx=10,pady=10,sticky="w")
        # Date de création
        self.date_de_creation_label = ct.CTkLabel(Consultation_frame, text="Date de création :", font=('Karla', 16),
                                             text_color='#263A5F')
        self.date_de_creation_label.grid(row=5, column=2, padx=10, pady=10, sticky="w")

        today_date = datetime.now().strftime('%d/%m/%Y')
        self.date_de_creation_entry = ct.CTkEntry(Consultation_frame, width=200, height=35, corner_radius=10,
                                             font=('Karla', 14))
        self.date_de_creation_entry.insert(0, today_date)
        self.date_de_creation_entry.configure(state='readonly')
        self.date_de_creation_entry.grid(row=5, column=3, padx=10, pady=10, sticky="w")

        # Libellé et champ pour le matricule du patient
        self.matricule_patient_label = ct.CTkLabel(Consultation_frame, text="Matricule Patient :", font=('Karla', 16),
                                              text_color='#263A5F')
        self.matricule_patient_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.matricule_patient_entry = ct.CTkEntry(Consultation_frame, width=200, height=35, corner_radius=10,
                                              font=('Karla', 14))
        self.matricule_patient_entry.insert(0, matricule_patient)
        self.matricule_patient_entry.configure(state='readonly')
        self.matricule_patient_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Libellé et champ pour le nom du patient
        self.nom_patient_label = ct.CTkLabel(Consultation_frame, text="Nom Patient :", font=('Karla', 16),
                                        text_color='#263A5F')
        self.nom_patient_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.nom_patient_entry = ct.CTkEntry(Consultation_frame, width=200, height=35, corner_radius=10, font=('Karla', 14))
        self.nom_patient_entry.insert(0, nom_patient)
        self.nom_patient_entry.configure(state='readonly')
        self.nom_patient_entry.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        # Geste medical
        self.geste_medical_label = ct.CTkLabel(Consultation_frame, text="Geste médical :", font=('Karla', 16),
                                               text_color='#263A5F')
        self.geste_medical_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        gestes = get_medical_gestures_from_db()
        self.geste_medical_combobox = ct.CTkComboBox(Consultation_frame, values=gestes, width=200, height=35,
                                                     corner_radius=10, font=('Karla', 14), dropdown_fg_color='#FFFFFF')
        self.geste_medical_combobox.grid(row=3, column=1, padx=10, pady=10, sticky="w")


        # le médecin de la consultation

        self.nom_medecin_label = ct.CTkLabel(Consultation_frame, text="Médecin:", font=('Karla', 16),
                                        text_color='#263A5F')
        self.nom_medecin_label.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        self.nom_medecin_entry = ct.CTkEntry(Consultation_frame, width=200, height=35, corner_radius=10, font=('Karla', 14))
        self.nom_medecin_entry.grid(row=3, column=3, padx=10, pady=10, sticky="w")

        # Libellé pour le conduite à tenire
        self.CAT_label = ct.CTkLabel(Consultation_frame, text="CAT :", font=('Karla', 16),
                                         text_color='#263A5F')
        self.CAT_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Champ de saisie de texte pour le diagnostique
        self.CAT_entry = ct.CTkTextbox(Consultation_frame, width=200, height=100, corner_radius=10,
                                           font=('Karla', 14))
        self.CAT_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # le traitement de la consultation
        self.traitement_label = ct.CTkLabel(Consultation_frame, text="Traitement :", font=('Karla', 16),
                                            text_color='#263A5F')
        self.traitement_label.grid(row=4, column=2, padx=10, pady=10, sticky="w")

        self.traitement_entry = ct.CTkEntry(Consultation_frame, width=200, height=35, corner_radius=10,
                                             font=('Karla', 14))
        self.traitement_entry.grid(row=4, column=3, padx=10, pady=10, sticky="w")
        # Lier la touche "Enter" à la fonction creer_consultation
        self.bind('<Return>', self.creer_consultation)

        # Button to add consultation
        self.enregistrer_consultation= ct.CTkButton(Consultation_frame, text="+Ajouter Consultation", command=self.creer_consultation, width=250,
                                                height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                                fg_color='#263A5F',
                                                cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_consultation.grid(row=6, column=1, columnspan=2, pady=0)
        # Assurez-vous qu'un widget a le focus pour que la liaison fonctionne
        self.enregistrer_consultation.focus_set()
        self.bind_all('<Return>', lambda event: self.creer_consultation())

    def creer_consultation(self,event=None):
        if self.nom_medecin_entry.get() == "" or self.CAT_entry.get("1.0", tk.END) == "":
            messagebox.showerror("Erreur", "Consultation incomplète", parent=self)
        else:
            try:
                # Établir une connexion à la base de données
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()

                # Requête SQL pour obtenir le matricule du médecin à partir de son nom
                nom_medecin = self.nom_medecin_entry.get()
                query = "SELECT matricule_medecin FROM medecin WHERE nom = %s"
                cur.execute(query, (nom_medecin,))
                row = cur.fetchone()

                if row:
                    matricule_medecin = row[0]

                    # Récupérer les autres valeurs des champs de saisie
                    matricule_patient = self.matricule_patient_entry.get()
                    date_creation = transform_date(self.date_de_creation_entry.get())
                    geste_medical = self.geste_medical_combobox.get()
                    diagnostique = self.CAT_entry.get("1.0", tk.END)  # Récupérer tout le texte
                    traitament = self.traitement_entry.get()

                    # Requête SQL pour insérer les données de consultation
                    query_insert = "INSERT INTO  historique_consultations (matricule_patient, matricule_medecin, date_de_consultation, geste_medical, diagnostique,traitement) VALUES (%s, %s, %s, %s, %s,%s)"

                    # Exécuter la requête SQL pour l'insertion
                    cur.execute(query_insert,
                                (matricule_patient, matricule_medecin, date_creation, geste_medical, diagnostique,traitament))

                    # Valider la transaction
                    con.commit()

                    # Afficher un message de succès
                    messagebox.showinfo("Succès", "Consultation enregistrée avec succès", parent=self)
                else:
                    messagebox.showerror("Erreur", "Médecin introuvable", parent=self)

            except Exception as e:
                # Afficher une erreur en cas d'échec de l'opération
                messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement de la consultation : {str(e)}",
                                     parent=self)
                print(str(e))
            finally:
                # Fermer la connexion à la base de données
                if con:
                    con.close()

#ajouter_rdv_prochain
    def ajouter_rdv_prochain(self, window, matricule_patient, nom_patient, prenom_patient):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

        # Crée un cadre pour afficher les informations du patient
        self.rdv_prochain_frame = ct.CTkFrame(window, fg_color='#ffffff')
        self.rdv_prochain_frame.pack(fill='both', expand=True)
        self.calender_image = Image.open('calendar-removebg-preview.png').resize((45, 45))
        self.calender_icon = ImageTk.PhotoImage(self.calender_image)

        # Date de création
        self.titre_label = ct.CTkLabel(self.rdv_prochain_frame, text="Rendez-vous prochain :",
                                       font=('Karla', 18, 'bold'),
                                       text_color='#263A5F')
        self.titre_label.grid(row=0,column=1,padx=5,pady=10,sticky="w")
        # Date de création
        self.date_de_creation_label = ct.CTkLabel(self.rdv_prochain_frame, text="Date de création :", font=('Karla', 16),
                                             text_color='#263A5F')
        self.date_de_creation_label.grid(row=4, column=0, padx=10, pady=20, sticky="w")

        today_date = datetime.now().strftime('%d/%m/%Y')
        self.date_de_creation_entry = ct.CTkEntry(self.rdv_prochain_frame, width=200, height=35, corner_radius=10,
                                             font=('Karla', 14))
        self.date_de_creation_entry.insert(0, today_date)
        self.date_de_creation_entry.configure(state='readonly')
        self.date_de_creation_entry.grid(row=4, column=1, padx=10, pady=20, sticky="w")
        # Date du rendez-vous
        self.date_rdv_label = ct.CTkLabel(self.rdv_prochain_frame, text="Date du rendez-vous :", font=('Karla', 16),
                                          text_color='#263A5F')
        self.date_rdv_label.grid(row=3, column=2, padx=10, pady=20, sticky="w")

        self.date_rdv_entry = ct.CTkEntry(self.rdv_prochain_frame, width=200, height=35, corner_radius=10,
                                          font=('Karla', 14))
        self.date_rdv_entry.grid(row=3, column=3, padx=10, pady=20, sticky="w")

        # Ajouter l'icône de calendrier
        self.show_calendar_button = Button(self.rdv_prochain_frame, image=self.calender_icon, width=25, height=30,
                                           command=self.open_calendar, bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                                           highlightthickness=0)
        self.show_calendar_button.place(x=1100, y=340)

        # Libellé et champ pour le matricule du patient
        self.matricule_patient_label = ct.CTkLabel(self.rdv_prochain_frame, text="Matricule Patient :", font=('Karla', 16),
                                              text_color='#263A5F')
        self.matricule_patient_label.grid(row=1, column=0, padx=10, pady=20, sticky="w")

        self.matricule_patient_entry = ct.CTkEntry(self.rdv_prochain_frame, width=200, height=35, corner_radius=10,
                                              font=('Karla', 14))
        self.matricule_patient_entry.insert(0, matricule_patient)
        self.matricule_patient_entry.configure(state='readonly')
        self.matricule_patient_entry.grid(row=1, column=1, padx=10, pady=20, sticky="w")

        # Libellé et champ pour le nom du patient
        self.nom_patient_label = ct.CTkLabel(self.rdv_prochain_frame, text="Nom Patient :", font=('Karla', 16),
                                             text_color='#263A5F')
        self.nom_patient_label.grid(row=1, column=2, padx=10, pady=20, sticky="w")

        self.nom_patient_entry = ct.CTkEntry(self.rdv_prochain_frame, width=200, height=35, corner_radius=10,
                                             font=('Karla', 14))
        self.nom_patient_entry.insert(0, nom_patient)
        self.nom_patient_entry.configure(state='readonly')
        self.nom_patient_entry.grid(row=1, column=3, padx=10, pady=20, sticky="w")

        # Libellé et champ pour le prénom du patient
        self.prenom_patient_label = ct.CTkLabel(self.rdv_prochain_frame, text="Prénom Patient :", font=('Karla', 16),
                                                text_color='#263A5F')
        self.prenom_patient_label.grid(row=2, column=0, padx=10, pady=20, sticky="w")

        self.prenom_patient_entry = ct.CTkEntry(self.rdv_prochain_frame, width=200, height=35, corner_radius=10,
                                                font=('Karla', 14))
        self.prenom_patient_entry.insert(0, prenom_patient)
        self.prenom_patient_entry.configure(state='readonly')
        self.prenom_patient_entry.grid(row=2, column=1, padx=10, pady=20, sticky="w")
        # Geste medical
        self.geste_medical_label = ct.CTkLabel(self.rdv_prochain_frame, text="Geste médical :", font=('Karla', 16),
                                               text_color='#263A5F')
        self.geste_medical_label.grid(row=3, column=0, padx=10, pady=20, sticky="w")
        gestes = get_medical_gestures_from_db()
        self.geste_medical_combobox = ct.CTkComboBox(self.rdv_prochain_frame, values=gestes, width=200, height=35,
                                                     corner_radius=10, font=('Karla', 14), dropdown_fg_color='#FFFFFF')
        self.geste_medical_combobox.grid(row=3, column=1, padx=10, pady=20, sticky="w")


        # le médecin de la consultation

        self.nom_medecin_label = ct.CTkLabel(self.rdv_prochain_frame, text="Médecin:", font=('Karla', 16),
                                        text_color='#263A5F')
        self.nom_medecin_label.grid(row=2, column=2, padx=10, pady=20, sticky="w")

        self.nom_medecin_entry = ct.CTkEntry(self.rdv_prochain_frame, width=200, height=35, corner_radius=10, font=('Karla', 14))
        self.nom_medecin_entry.grid(row=2, column=3, padx=10, pady=20, sticky="w")
        # Liaison de la touche "Enter" à la fonction creer
        self.bind('<Return>', self.creer_rdv_prochain)

        # Button to Create appoiments
        self.enregistrer_rdv= ct.CTkButton(self.rdv_prochain_frame, text="+Ajouter Le Rendez-vous", command=self.creer_rdv_prochain, width=250,
                                                height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                                fg_color='#263A5F',
                                                cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_rdv.grid(row=5, column=1, columnspan=2, pady=5)
        self.enregistrer_rdv.focus_set()
        self.bind_all('<Return>', lambda event: self.creer_rdv_prochain())
    def creer_rdv_prochain(self,event=None):
        # Récupérer le nom complet du patient en combinant le nom et le prénom
        nom_complet = f"{self.nom_patient_entry.get()} {self.prenom_patient_entry.get()}"
        if (
                self.date_rdv_entry.get() == "" or self.date_de_creation_entry.get() == "" or nom_complet == "" or self.matricule_patient_entry.get() == "" or
                self.nom_medecin_entry.get() == "" or self.geste_medical_combobox.get() == ""
        ):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        else:
            try:
                # Établir une connexion à la base de données
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()

                # Vérifier si le patient existe déjà
                cur.execute("SELECT * FROM patient WHERE nom = %s AND prenom = %s AND matricule_patient = %s",
                            (self.nom_patient_entry.get(), self.prenom_patient_entry.get(),
                             self.matricule_patient_entry.get()))
                patient_exists = cur.fetchone()

                if patient_exists:
                    # Récupération du matricule_medecin à partir de la table medecin
                    cur.execute("SELECT matricule_medecin FROM medecin WHERE nom = %s", (self.nom_medecin_entry.get(),))
                    matricule_medecin = cur.fetchone()
                    if matricule_medecin is None:
                        messagebox.showerror("Erreur", "Médecin non trouvé", parent=self)
                        return
                    matricule_medecin = matricule_medecin[0]

                    # Insertion des données dans la table des rendez-vous avec le nom complet du patient
                    cur.execute(
                        """INSERT INTO rendez_vous (date_creation_du_rendez_vous, date_du_rendez_vous, patient,matricule_patient, geste_medical, medecin, matricule_medecin, validation) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s,%s)""",
                        (transform_date(self.date_de_creation_entry.get()), transform_date(self.date_rdv_entry.get()),
                         nom_complet, self.matricule_patient_entry.get(), self.geste_medical_combobox.get(),
                         self.nom_medecin_entry.get(), matricule_medecin,
                         'Non validé')
                    )
                    con.commit()
                    # Afficher un message de succès
                    messagebox.showinfo("Succès", "Rendez-vous enregistrée avec succès", parent=self)
                else:
                    messagebox.showerror("Erreur", "Médecin introuvable", parent=self)

            except Exception as e:
                # Afficher une erreur en cas d'échec de l'opération
                messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement de la consultation : {str(e)}",
                                     parent=self)
                print(str(e))
            finally:
                # Fermer la connexion à la base de données
                if con:
                    con.close()

    def open_calendar(self):
        # Crée un frame flottant pour le calendrier
        self.calendar_frame = Frame(self.rdv_prochain_frame, bg='#FFFFFF', bd=2, relief='raised')
        self.calendar_frame.place(x=900, y=330)  # Ajustez les coordonnées selon vos besoins

        self.cal = Calendar(self.calendar_frame, selectmode="day", locale="fr_FR", date_pattern="dd/mm/yyyy")
        self.cal.pack(padx=10, pady=5)

        self.select_button = Button(self.calendar_frame, text="Sélectionner", command=self.select_date, bg='#263A5F',
                                    fg='#FFFFFF')
        self.select_button.pack(pady=10)

    def select_date(self):
        # Récupérer la date sélectionnée et l'afficher dans l'entrée
        selected_date = self.cal.get_date()
        self.date_rdv_entry.delete(0, END)
        self.date_rdv_entry.insert(0, selected_date)
        self.calendar_frame.destroy()

    def show_appointments_tab(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        self.current_search_list = "rdv"

        # Create and display the treeview for appointments
        self.create_appointments_treeview()
        # Effacer le Treeview
        for item in self.treeview_appointments.get_children():
            self.treeview_appointments.delete(item)

        # Connexion à la base de données
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()

        # Récupération des données des patients depuis la table
        cur.execute("SELECT id_rendez_vous , patient,date_du_rendez_vous, geste_medical,validation FROM rendez_vous")
        rows = cur.fetchall()
        for row in rows:
            # Appeler add_patient avec les valeurs appropriées
            self.add_appointment(self.treeview_appointments, row)  # Sélectionnez les six premières valeurs de la ligne

        self.treeview_appointments.bind("<Button-1>", self.on_click_RDV)
    def on_click_RDV(self, event):
        item_id = self.treeview_appointments.identify_row(event.y)# Obtient l'élément actuellement sélectionné dans Treeview
        if not item_id:
            return
        values = self.treeview_appointments.item(item_id, 'values')  # Obtient les valeurs des colonnes de l'élément
        if values:
            # Obtenez la valeur de matricule_RDV (remplacez l'index 0 par l'index correct)
            self.id_rendez_vous = values[0]
            # Ouvre une nouvelle fenêtre avec les valeurs de l'élément
            self.new_window = ct.CTkToplevel(self)
            self.new_window.grab_set()
            self.new_window.title("Détails du Rendez-vous")
            self.new_window.geometry("650x400+400+200")
            # Configure la fenêtre pour désactiver le redimensionnement en largeur et autoriser le redimensionnement en hauteur
            self.new_window.resizable(width=False, height=False)

            self.menu_frame = ct.CTkFrame(self.new_window, width=760, height=50, border_width=0, corner_radius=0,
                                          fg_color='#B8F9FF')
            self.menu_frame.pack()

            showRDV_butt = ct.CTkButton(self.menu_frame, text="Voir détails du Rendez-vous",
                                        command=lambda: self.afficher_détails_RDV(self.info_frame, values),
                                        width=50, height=30, corner_radius=15, font=('Karla', 14, 'bold'),
                                        fg_color='#FF0000', cursor='hand2', text_color='#FFFFFF')
            showRDV_butt.place(x=35, y=10)

            reporterRDV_butt = ct.CTkButton(self.menu_frame, text="Reporter Rendez-vous",
                                            command=lambda: self.reporter_RDV(self.info_frame, values),
                                            width=50, height=30, corner_radius=15, font=('Karla', 14, 'bold'),
                                            fg_color='#FF0000', cursor='hand2', text_color='#FFFFFF')
            reporterRDV_butt.place(x=400, y=10)

            self.info_frame = ct.CTkFrame(self.new_window, width=697, height=400, border_color='#FF0000',
                                          border_width=2,
                                          fg_color='transparent')
            self.info_frame.pack(fill='both', expand=True)
            # Appeler afficher_détails_RDV pour afficher les informations par défaut
            self.afficher_détails_RDV(self.info_frame, values)

    def afficher_détails_RDV(self, info_frame, values):
        # Clear the existing content of the info_frame
        for widget in info_frame.winfo_children():
            widget.destroy()

        # Create a frame to display the appointment details
        details_frame = ct.CTkFrame(info_frame, fg_color='#ffffff')
        details_frame.pack(fill='both', expand=True)

        # Define labels and corresponding values for appointment details
        labels = ['N°RDV :', 'Patient :', 'Date du Rendez-vous :','Geste médical :']
        for i, (label_text, value) in enumerate(zip(labels, values)):
            label = ct.CTkLabel(details_frame, text=label_text, font=('Karla', 16))
            label.grid(row=i, column=0, sticky='w', padx=10, pady=5)
            value_label = ct.CTkLabel(details_frame, text=value, font=('Karla', 16))
            value_label.grid(row=i, column=1, sticky='w', padx=10, pady=5)

    def reporter_RDV(self, window, values):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

        # Create a frame to display the appointment details
        self.RDV_frame = ct.CTkFrame(window, fg_color='#ffffff')
        self.RDV_frame.pack(fill='both', expand=True)

        self.report_label = ct.CTkLabel(self.RDV_frame, text="Raporter Rendez-vous :", font=('Karla', 16,'bold'),
                                                  text_color='#263A5F')
        self.report_label.grid(row=0, column=1, sticky="w")

        # Date de creation
        self.date_de_creation_label = ct.CTkLabel(self.RDV_frame, text="Date de création :", font=('Karla', 16),
                                                  text_color='#263A5F')
        self.date_de_creation_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.calender_image = Image.open('calendar-removebg-preview.png').resize((45, 45))
        self.calender_icon = ImageTk.PhotoImage(self.calender_image)

        today_date = datetime.now().strftime('%d/%m/%Y')
        self.date_de_creation_entry = ct.CTkEntry(self.RDV_frame, width=200, height=35, corner_radius=10,
                                                  font=('Karla', 14))
        self.date_de_creation_entry.insert(0, today_date)
        self.date_de_creation_entry.configure(state='readonly')
        self.date_de_creation_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Date du rendez-vous
        self.date_rdv_label = ct.CTkLabel(self.RDV_frame, text="Nouvelle date de rendez-vous :", font=('Karla', 16),
                                          text_color='#263A5F')
        self.date_rdv_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")

        self.date_rdv_entry = ct.CTkEntry(self.RDV_frame, width=200, height=35, corner_radius=10,
                                          font=('Karla', 14))
        self.date_rdv_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        # Ajouter l'icône de calendrier
        self.show_calendar_button = Button(self.RDV_frame, image=self.calender_icon, width=25, height=30,
                                           command=self.open_calendar_report, bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                                           highlightthickness=0)
        self.show_calendar_button.place(x=690, y=195)
        self.bind('<Return>',self.report_RDV_to_database)

        # Button to report RDV
        self.report_button = ct.CTkButton(self.RDV_frame, text="Reporter RDV",
                                          command=lambda: self.report_RDV_to_database(self.id_rendez_vous),
                                          width=250, height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                          fg_color='#263A5F', cursor='hand2', text_color='#FFFFFF')
        self.report_button.grid(row=3, column=1, pady=30)
        self.report_button.focus_set()
        self.bind_all('<Return>', lambda event: self.report_RDV_to_database(self.id_rendez_vous))

    def open_calendar_report(self):
        # Crée un frame flottant pour le calendrier
        self.calendar_frame = Frame(self.RDV_frame, bg='#FFFFFF', bd=2, relief='raised')
        self.calendar_frame.place(x=460, y=230)  # Ajustez les coordonnées selon vos besoins

        self.cal = Calendar(self.calendar_frame, selectmode="day", locale="fr_FR", date_pattern="dd/mm/yyyy")
        self.cal.pack(padx=10, pady=10)

        self.select_button = Button(self.calendar_frame, text="Sélectionner", command=self.select_date, bg='#263A5F',
                                    fg='#FFFFFF')
        self.select_button.pack(pady=10)
    def select_date(self):
        # Récupérer la date sélectionnée et l'afficher dans l'entrée
        selected_date = self.cal.get_date()
        self.date_rdv_entry.delete(0, tk.END)
        self.date_rdv_entry.insert(0, selected_date)
        self.calendar_frame.destroy()

    def report_RDV_to_database(self, matricule_RDV,event=None):
        if self.date_rdv_entry.get() == "":
            messagebox.showerror("Erreur", "Veuillez entrer la date de report")
        else:
            new_date = transform_date(self.date_rdv_entry.get())
            creation_date = transform_date(self.date_de_creation_entry.get())
            if new_date and creation_date:  # Vérifie si les dates sont valides
                try:
                    con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                    cur = con.cursor()

                    # Update the rendez_vous table with the new date
                    cur.execute(
                        "UPDATE rendez_vous SET date_du_rendez_vous = %s, date_creation_du_rendez_vous = %s WHERE id_rendez_vous = %s",
                        (new_date, creation_date, matricule_RDV))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Succès", "RDV reporté avec succès")
                except Exception as es:
                    messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}")
                    print("{str(es)}")
    def show_doctors_tab(self):
        # Clear the center fram
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Create and display the treeview for doctors
        self.create_doctor_treeview()
        # Connexion à la base de données
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()

        # Récupération des données des patients depuis la table
        cur.execute("SELECT matricule_medecin  , nom,prenom,grade,telephone FROM medecin")
        rows = cur.fetchall()
        for row in rows:
            # Appeler add_patient avec les valeurs appropriées
            self.add_doctor(self.treeview_doctors, row)  # Sélectionnez les six premières valeurs de la ligne

    def report_appointments(self):
        self.open_toplevelDocteur()


    def filter_appointments(self, date):
        filtered_appointments = []
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()
        cur.execute(
            "SELECT id_rendez_vous, patient, date_du_rendez_vous, geste_medical FROM rendez_vous WHERE date_du_rendez_vous = %s",
            (date,))
        rows = cur.fetchall()
        for row in rows:
            patient_name = row[1]  # Nom complet du patient (nom et prénom)
            medical_gesture_name = row[3]
            filtered_appointments.append({
                "N°RDV": row[0],
                'date': row[2],
                'patient': patient_name,
                'medical_gesture': medical_gesture_name,
            })
        con.close()
        return filtered_appointments

    def show_consultations(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Get the current date
        today = datetime.now().strftime('%Y-%m-%d')

        # Filter the appointments for the current date
        appointments = self.filter_appointments(today)

        # Create and display the treeview for consultations
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff",
                        font=('Karla', 16), rowheight=60)
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 24, 'bold'), foreground="#1C1278")

        columns = ("N°Consultation", "N°RDV", "Date", "Patient", "Geste médical")
        self.treeview_consultations = ttk.Treeview(self.center_frame, columns=columns, show="headings",
                                                   style="Custom.Treeview")
        # Ajouter une barre de défilement verticale
        scrollbar = ttk.Scrollbar(self.center_frame, orient="vertical", command=self.treeview_consultations.yview)
        scrollbar.pack(side="right", fill="y")
        self.treeview_consultations.configure(yscrollcommand=scrollbar.set)
        self.treeview_consultations.pack(expand=True, fill='both')

        # Définir les en-têtes
        for col in columns:
            self.treeview_consultations.heading(col, text=col, anchor='center')
            width = 245 if col == "N°Consultation" else (120 if col == "N°RDV" else 380)
            self.treeview_consultations.column(col, anchor='center', width=width)

        # Ajouter les rendez-vous au treeview avec numérotation séquentielle pour "N°Consultation"
        for idx, appointment in enumerate(appointments, start=1):
            self.treeview_consultations.insert('', 'end', values=(
                idx, appointment['N°RDV'], appointment['date'], appointment['patient'], appointment['medical_gesture']
            ))

        # Lier l'événement de clic à une méthode
        self.treeview_consultations.bind("<Double-1>", self.on_click_consultation)

    def on_click_consultation(self, event):
        item = self.treeview_consultations.focus()  # Get the currently selected item in Treeview
        values = self.treeview_consultations.item(item, 'values')  # Get the values of the item's columns
        if values:
            # Obtenez la valeur de l'identifiant du rendez-vous
            self.id_rendez_vous = values[0]
            # Open a new window with the values of the item
            self.new_window = ct.CTkToplevel(self)
            self.new_window.grab_set()
            self.new_window.title("Détails de la Consultation")
            self.new_window.geometry("650x400+400+200")
            # Configure la fenêtre pour désactiver le redimensionnement en largeur et autoriser le redimensionnement en hauteur
            self.new_window.resizable(width=False, height=False)

            self.menu_frame = ct.CTkFrame(self.new_window, width=760, height=50, border_width=0, corner_radius=0,
                                          fg_color='#B8F9FF')
            self.menu_frame.pack()

            showConsult_butt = ct.CTkButton(self.menu_frame, text="Voir détails de la Consultation",
                                            command=None,
                                            width=50, height=30, corner_radius=15, font=('Karla', 14, 'bold'),
                                            fg_color='#FF0000', cursor='hand2', text_color='#FFFFFF')
            showConsult_butt.place(x=35, y=10)

            self.info_frame = ct.CTkFrame(self.new_window, width=697, height=400, border_color='#FF0000',
                                          border_width=2,
                                          fg_color='transparent')
            self.info_frame.pack(fill='both', expand=True)
            # Call afficher_détails_consult to display the default information
            self.afficher_détails_consult(self.info_frame, values)

    def afficher_détails_consult(self, info_frame, values):
        # Clear the frame
        for widget in info_frame.winfo_children():
            widget.destroy()

        # Create a frame to display the appointment details
        self.details_frame = ct.CTkFrame(info_frame, fg_color='#ffffff')
        self.details_frame.pack(fill='both', expand=True)

        # Add details to the frame
        labels = ["N°RDV: ", "Date:", "Patient:", "Geste médical:"]
        for i, label in enumerate(labels):
            lbl = ct.CTkLabel(self.details_frame, text=label, font=('Karla', 16, 'bold'), text_color='#1C1278')
            lbl.grid(row=i, column=0, padx=10, pady=10, sticky='w')
            val = ct.CTkLabel(self.details_frame, text=values[i+1], font=('Karla', 16), text_color='#000000')
            val.grid(row=i, column=1, padx=10, pady=10, sticky='w')

        # Add the Checkbutton to validate the appointment
        validate_var = tk.BooleanVar()
        validate_checkbox = ct.CTkCheckBox(self.details_frame, text="Valider le RDV", variable=validate_var,
                                           command=lambda: self.update_validation(values[1], validate_var,
                                                                                  validate_checkbox))
        validate_checkbox.grid(row=len(labels), columnspan=3, padx=50, pady=20)

        # Retrieve the validation status from the database for this appointment
        appointment_id = values[1]
        validation_status = self.get_validation_status(appointment_id)
        validate_var = tk.BooleanVar(value=validation_status == "oui validé")

        # Add the Checkbutton to validate the appointment
        validate_checkbox = ct.CTkCheckBox(self.details_frame, text="Valider le RDV", variable=validate_var,
                                           command=lambda: self.update_validation(appointment_id, validate_var,
                                                                                  validate_checkbox))
        validate_checkbox.grid(row=len(labels), columnspan=3, padx=50, pady=20)

        # If the RDV is already validated, disable the checkbox
        if validation_status == "oui validé":
            validate_checkbox.select()
            validate_checkbox.configure(state=tk.DISABLED)

    def get_validation_status(self, appointment_id):
        try:
            # Connect to the database
            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
            cur = con.cursor()

            # Retrieve the validation status from the database
            cur.execute("SELECT validation FROM rendez_vous WHERE id_rendez_vous = %s", (appointment_id,))
            result = cur.fetchone()

            # Close the connection
            con.close()

            if result:
                return result[0]
            else:
                return "non"  # Default validation status if not found

        except Exception as e:
            print("Error fetching validation status:", e)
            return "non"  # Default validation status in case of error

    def update_validation(self, appointment_id, validate_var, validate_checkbox):
        try:
            # Retrieve the current validation status
            validation_status = 'oui validé' if validate_var.get() else 'non'

            # Connect to the database
            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
            cur = con.cursor()

            # Update the validation status in the database
            cur.execute(
                "UPDATE rendez_vous SET validation = %s WHERE id_rendez_vous = %s",
                (validation_status, appointment_id)
            )

            # Commit the transaction
            con.commit()

            # Close the connection
            con.close()

            # Show success message
            messagebox.showinfo("Succès", "Validation du RDV mise à jour avec succès")

            # Disable the checkbox after validation
            self.disable_checkbox(validate_checkbox)

        except Exception as e:
            # Show error message in case of failure
            messagebox.showerror("Erreur", f"Erreur lors de la mise à jour de la validation du RDV : {str(e)}")
            print("Error updating validation status:", e)

        except Exception as e:
            # Show error message in case of failure
            messagebox.showerror("Erreur", f"Erreur lors de la mise à jour de la validation du RDV : {str(e)}")
            print("Error updating validation status:", e)

    def disable_checkbox(self, checkbox):
        checkbox.configure(state=tk.DISABLED)

    def create_administrateur_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff",
                        font=('Karla', 16), rowheight=60)
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 24, 'bold'), foreground="#1C1278")

        # Tableau Treeview
        columns = ("Matricule", "Nom", "Prénom", "Date de naissance", "Téléphone")
        self.treeview_administrateurs = ttk.Treeview(self.center_frame, columns=columns, show="headings",
                                                     style="Custom.Treeview")
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.center_frame, orient="vertical", command=self.treeview_administrateurs.yview)
        scrollbar.pack(side="right", fill="y")
        self.treeview_administrateurs.configure(yscrollcommand=scrollbar.set)
        self.treeview_administrateurs.pack( expand=True ,fill='both')

        # Définition des en-têtes
        for col in columns:
            self.treeview_administrateurs.heading(col, text=col, anchor='center')
            width = 250 if columns == "Matricule" else 301
            self.treeview_administrateurs.column(col, anchor='center', width=width)

        # Bind the Treeview select event to the on_row_select method
        self.treeview_administrateurs.bind('<<TreeviewSelect>>', self.on_row_select)

        def add_administrateur(self, treeview, row):
            treeview.insert('', 'end', values=row)

    def add_administrateur(self, treeview, row):
        treeview.insert('', 'end', values=row)

    def show_settings(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Create and display the Treeview for administrateurs
        self.create_administrateur_treeview()

        # Connexion à la base de données
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()

        # Récupération des données des administrateurs depuis la table
        cur.execute("SELECT matricule_administrateur, nom, prenom, date_de_naissance, telephone FROM administrateur")
        rows = cur.fetchall()
        cur.close()
        con.close()

        for row in rows:
            # Appeler add_administrateur avec les valeurs appropriées
            self.add_administrateur(self.treeview_administrateurs, row)

    def on_row_select(self, event):
        # Get selected row
        selected_item = self.treeview_administrateurs.selection()[0]
        values = self.treeview_administrateurs.item(selected_item, "values")

        # Open new window with detailed information
        self.new_window = ct.CTkToplevel(self)
        self.new_window.grab_set()
        self.new_window.title("Détails de l'administrateur")
        self.new_window.geometry("400x300+300+300")
        # Configure la fenêtre pour désactiver le redimensionnement en largeur et autoriser le redimensionnement en hauteur
        self.new_window.resizable(width=False, height=False)
        self.frameADV = ct.CTkFrame(self.new_window, fg_color='#ffffff', corner_radius=0, border_width=2,
                                    border_color='#263A5F')
        self.frameADV.pack(expand=True, fill='both')

        labels = ["Matricule", "Nom", "Prénom", "Date de naissance", "Téléphone"]
        for idx, label in enumerate(labels):
            ct.CTkLabel(self.frameADV, text=f"{label}:", font=('Karla', 16, 'bold')).grid(row=idx, column=0, padx=10,
                                                                                          pady=10, sticky='e')
            ct.CTkLabel(self.frameADV, text=values[idx], font=('Karla', 16)).grid(row=idx, column=1, padx=10, pady=10,
                                                                                  sticky='w')

            # Add the delete button
            self.delete_adm_button = ct.CTkButton(self.frameADV, text="Supprimer l'administrateur",
                                                  command=lambda: self.delete_administrateur(values[0], selected_item),
                                                  width=250,
                                                  height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                                  fg_color='#263A5F',
                                                  cursor='hand2', text_color='#FFFFFF')
            self.delete_adm_button.place(x=80, y=245)

    def delete_administrateur(self, matricule, item):
        # Confirmation dialog
        if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer cet administrateur ?"):
            try:
                # Connexion à la base de données
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()

                # Suppression de l'administrateur dans la base de données
                cur.execute("DELETE FROM administrateur WHERE matricule_administrateur = %s", (matricule,))
                con.commit()
                cur.close()
                con.close()

                # Suppression de l'administrateur dans le Treeview
                self.treeview_administrateurs.delete(item)

                messagebox.showinfo("Succès", "Administrateur supprimé avec succès.")
                self.new_window.destroy()

            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")

    def calculate_nombre_rdv_valider(self):
        try:
            # Connect to the database
            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
            cur = con.cursor()

            # Retrieve the number of validated appointments for the current month and year
            cur.execute("""
                SELECT COUNT(*) 
                FROM rendez_vous 
                WHERE validation = 'oui validé' 
                AND MONTH(date_du_rendez_vous) = MONTH(CURRENT_DATE) 
                AND YEAR(date_du_rendez_vous) = YEAR(CURRENT_DATE)
            """)
            result = cur.fetchone()

            # Close the connection
            con.close()

            if result:
                return str(result[0])
            else:
                return "0"

        except Exception as e:
            print("Error fetching number of validated appointments:", e)
            return "0"

    def count_new_patients(self, month, year):
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()
        cur.execute("""SELECT COUNT(*) FROM patient WHERE MONTH(création) = %s AND YEAR(création) = %s
            """, (month, year))
        count = cur.fetchone()[0]
        con.close()
        return count

    def count_new_patients_femme(self, month, year):
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()
        cur.execute("""SELECT COUNT(*) FROM patient WHERE sexe = 'Femme' AND MONTH(création) = %s AND YEAR(création) = %s
            """, (month, year))
        count = cur.fetchone()[0]
        con.close()
        return count

    def count_new_patients_homme(self, month, year):
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()
        cur.execute("""SELECT COUNT(*) FROM patient WHERE sexe = 'Homme' AND MONTH(création) = %s AND YEAR(création) = %s
            """, (month, year))
        count = cur.fetchone()[0]
        con.close()
        return count

    def calculate_nombre_traitement_total(self):
        try:
            # Connect to the database
            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
            cur = con.cursor()

            # Retrieve the number of treatments for the current month and year
            cur.execute("""
                SELECT COUNT(traitement) 
                FROM historique_consultations 
                WHERE MONTH(date_de_consultation) = MONTH(CURRENT_DATE) 
                AND YEAR(date_de_consultation) = YEAR(CURRENT_DATE)
            """)
            result = cur.fetchone()

            # Close the connection
            con.close()

            if result:
                return str(result[0])
            else:
                return "0"

        except Exception as e:
            print("Error fetching number of treatments:", e)
            return "0"
    def count_diagnostic_types(self, month, year):
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()
        cur.execute("""SELECT diagnostique, sexe FROM patient 
                       WHERE MONTH(création) = %s AND YEAR(création) = %s
                    """, (month, year))
        diagnostics = cur.fetchall()

        diagnostic_types = {}
        for diagnostic, sexe in diagnostics:
            if diagnostic not in diagnostic_types:
                diagnostic_types[diagnostic] = {'total': 1, 'homme': 0, 'femme': 0}
            else:
                diagnostic_types[diagnostic]['total'] += 1

            if sexe == 'Homme':
                diagnostic_types[diagnostic]['homme'] += 1
            elif sexe == 'Femme':
                diagnostic_types[diagnostic]['femme'] += 1

        con.close()
        return diagnostic_types

    def count_medical_gestures(self):
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()
        cur.execute("""SELECT hc.geste_medical, p.sexe 
                       FROM historique_consultations hc 
                       INNER JOIN patient p ON hc.matricule_patient = p.matricule_patient
                       WHERE MONTH(hc.	date_de_consultation) = MONTH(CURRENT_DATE) 
                       AND YEAR(hc.	date_de_consultation) = YEAR(CURRENT_DATE)
                    """)
        gestures = cur.fetchall()

        gesture_counts = {}
        for gesture, sexe in gestures:
            if gesture not in gesture_counts:
                gesture_counts[gesture] = {'total': 1, 'homme': 0, 'femme': 0}
            else:
                gesture_counts[gesture]['total'] += 1

            if sexe == 'Homme':
                gesture_counts[gesture]['homme'] += 1
            elif sexe == 'Femme':
                gesture_counts[gesture]['femme'] += 1

        con.close()
        return gesture_counts

    def create_statistic(self, parent, label, value, column, row):
        # Create a frame with a rounded black border
        border_frame = ct.CTkFrame(parent, fg_color="#ffffff", border_color="#263A5F", border_width=2, corner_radius=10)
        border_frame.grid(row=row, column=column, padx=2, pady=10, sticky='nsew')

        # Create a frame inside the border frame to hold the statistic labels
        stat_frame = ct.CTkFrame(border_frame, fg_color="white", width=800)
        stat_frame.pack(padx=8, pady=8, expand=True, fill='both')

        # Create the statistic labels
        label_widget = ct.CTkLabel(stat_frame, text=label, font=('Karla', 18, 'bold'), text_color='#263A5F')
        label_widget.pack(pady=(0, 5), anchor='w')

        if isinstance(value, dict):
            if label == "Nombre de diagnostiques : " or label == "Nombre de gestes medicales  : ":
                # Create a table to display the diagnostics or medical gestures
                table_frame = tk.Frame(stat_frame)
                table_frame.pack(pady=(0, 5), anchor='w')

                headers = ['Type', 'Total', 'Homme', 'Femme']
                for i, header in enumerate(headers):
                    header_label = tk.Label(table_frame, text=header, font=('Karla', 14, 'bold'), bg='white')
                    header_label.grid(row=0, column=i, padx=5, pady=5)

                for i, (key, counts) in enumerate(value.items(), start=1):
                    type_label = tk.Label(table_frame, text=key, font=('Karla', 14), bg='white')
                    type_label.grid(row=i, column=0, padx=5, pady=5)

                    total_label = tk.Label(table_frame, text=str(counts['total']), font=('Karla', 14), bg='white')
                    total_label.grid(row=i, column=1, padx=5, pady=5)

                    homme_label = tk.Label(table_frame, text=str(counts['homme']), font=('Karla', 14), bg='white')
                    homme_label.grid(row=i, column=2, padx=5, pady=5)

                    femme_label = tk.Label(table_frame, text=str(counts['femme']), font=('Karla', 14), bg='white')
                    femme_label.grid(row=i, column=3, padx=5, pady=5)
            else:
                value_text = str(value)
                value_widget = ct.CTkLabel(stat_frame, text=value_text, font=('Karla', 18, 'bold'),
                                           text_color='#263A5F')
                value_widget.pack(pady=(0, 5), anchor='w')
        else:
            value_widget = ct.CTkLabel(stat_frame, text=str(value), font=('Karla', 18, 'bold'), text_color='#263A5F')
            value_widget.pack(pady=(0, 5), anchor='w')

    def create_statistics_frame(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Create a canvas with a scrollbar
        canvas = tk.Canvas(self.center_frame, width=1500, height=634)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.center_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas
        stats_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=stats_frame, anchor='nw')

        # Grid configuration
        for i in range(3):
            stats_frame.columnconfigure(i, weight=1)

        import datetime
        current_date = datetime.datetime.now()
        current_month = current_date.month
        current_year = current_date.year

        # Create statistics
        self.create_statistic(stats_frame, "Nombre de nouveaux patients :", self.count_new_patients(current_month, current_year), 0, 0)
        self.create_statistic(stats_frame, "Femme :",self.count_new_patients_femme(current_month, current_year), 1, 0)
        self.create_statistic(stats_frame, "Homme :",self.count_new_patients_homme(current_month, current_year), 2, 0)
        self.create_statistic(stats_frame, "Nombre de rdv validees : ", self.calculate_nombre_rdv_valider(), 0, 3)
        self.create_statistic(stats_frame, "Nombre de diagnostiques : ", self.count_diagnostic_types(current_month, current_year), 0, 1)
        self.create_statistic(stats_frame, "Nombre de gestes medicales  : ", self.count_medical_gestures(), 1, 1)
        self.create_statistic(stats_frame, "Nombre de traitements : ", self.calculate_nombre_traitement_total(), 1, 3)

        # Update the canvas to show the scrollbar
        stats_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
    def open_toplevelP(self):
        if self.toplevelP_window is None or not self.toplevelP_window.winfo_exists():
            self.toplevelP_window = Inscrire_patient(self)  # create window if its None or destroyed
            self.toplevelP_window.grab_set()  # Make the new window modal
        else:
            self.toplevelP_window.focus()  # if window exists focus it

    def open_toplevelDocteur(self):
        if self.toplevelDocteur_window is None or not self.toplevelDocteur_window.winfo_exists():
            self.toplevelDocteur_window= Inscrire(self)  # create window if its None or destroyed
            self.toplevelDocteur_window.grab_set()  # Make the new window modal
        else:
            self.toplevelDocteur_window.focus()  # if window exists focus it



app = Accueil()
app.mainloop()


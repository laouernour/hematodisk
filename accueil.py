import customtkinter as ct
from tkinter import  ttk
from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk

def transform_date(date_str):
    # Convertit la date du format 'dd-mm-yyyy' au format 'yyyy-mm-dd'
    try:
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        return date_obj.strftime('%Y/%m/%d')
    except ValueError as e:
        messagebox.showerror("Erreur de date", f"Format de date incorrect: {date_str}. Utilisez le format 'jj-mm-aaaa'.\nErreur: {e}")
        return None

class Inscrire(ct.CTkToplevel):
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

        self.label = ct.CTkLabel(self.label_frame, text="Inscrire Doctor :", font=('Karla', 26,'bold'))
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

        # Date de Naissance
        self.date_naissance_label = ct.CTkLabel(self.inscription_frame, text="Date de Naissance :", font=('Karla', 18))
        self.date_naissance_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.date_naissance_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                                font=('Karla', 14))
        self.date_naissance_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Wilaya
        self.wilaya_label = ct.CTkLabel(self.inscription_frame, text="Wilaya :", font=('Karla', 18))
        self.wilaya_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.wilaya_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                        font=('Karla', 14))
        self.wilaya_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Téléphone
        self.phone_nmbr_label = ct.CTkLabel(self.inscription_frame, text="Téléphone:", font=('Karla', 18))
        self.phone_nmbr_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbr_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                            font=('Karla', 14))
        self.phone_nmbr_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        # Matricule
        self.matricule_doctor_label = ct.CTkLabel(self.inscription_frame, text="Matricule Médecin:", font=('Karla', 18))
        self.matricule_doctor_label.grid(row=2, column=2, padx=20, pady=20, sticky="w")
        self.matricule_doctor_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                                  font=('Karla', 14))
        self.matricule_doctor_entry.grid(row=2, column=3, padx=20, pady=20, sticky="w")

        # Grad
        self.grad_label = ct.CTkLabel(self.inscription_frame, text="Grade:", font=('Karla', 18))
        self.grad_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        grad = ["Généraliste", "Résident", "Assistant", "Maître Assistant", "Professeur"]
        self.grad_entry = ct.CTkComboBox(self.inscription_frame, values=grad, dropdown_font=('Karla', 14), width=250,
                                         height=35, corner_radius=10,
                                         font=('Karla', 14), dropdown_fg_color='#FFFFFF')
        self.grad_entry.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        # Button to Create Account
        self.enregistrer_doctor = ct.CTkButton(self.inscription_frame, text="Créer", command=self.creer, width=250,
                                            height=40, corner_radius=15, font=('Karla', 18, 'bold'), fg_color='#263A5F',
                                            cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_doctor.grid(row=5, column=1, columnspan=2, pady=10)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Redimensionne à la moitié de la taille originale
        label_image = Label(self.label_frame, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Garde une référence à l'image
        label_image.pack()  # Ajustez la position selon vos besoins

    def creer(self):
        if (self.nom_entry.get() == "" or self.prenom_entry.get() == "" or self.date_naissance_entry.get() == ""
                or self.wilaya_entry.get() == "" or self.phone_nmbr_entry.get() == ""
                or self.matricule_doctor_entry.get() == ""):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        else:
            # Placeholder for database connection and operation
            try:
                mydb = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                mycursor = mydb.cursor()
                mycursor.execute("insert into medecin (matricule_medecin,nom,prenom,date_de_naissance,wilaya,telephone,grade)values(%s,%s,%s,%s,%s,%s,%s)",
                                 (
                                 self.matricule_doctor_entry.get(),
                                 self.nom_entry.get(),
                                 self.prenom_entry.get(),
                                 transform_date(self.date_naissance_entry.get()),
                                 self.wilaya_entry.get(),
                                 self.phone_nmbr_entry.get(),
                                 self.grad_entry.get(),
                ))
                messagebox.showinfo("Success",f"Médecin enregistrer", parent=self )
                mydb.commit()
                self.vider()
                mydb.close
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)

    def vider(self):
        self.matricule_doctor_entry.delete(0, END),
        self.nom_entry.delete(0, END),
        self.prenom_entry.delete(0, END),
        self.date_naissance_entry.delete(0, END),
        self.wilaya_entry.delete(0, END),
        self.phone_nmbr_entry.delete(0, END),



class Inscrire_patient(ct.CTkToplevel):
    def __init__(self, parent):  # Add parent as an argument
        super().__init__(parent)
        self.title("S'inscrire")
        self.geometry('850x500+300+100')
        self.configure(bg='#263A5F')

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
        self.nomP_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.nomP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.nomP_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenomP_label = ct.CTkLabel(self.inscription_frame, text="Prénom :", font=('Karla', 16))
        self.prenomP_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")
        self.prenomP_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.prenomP_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Date de Naissance
        self.date_naissanceP_label = ct.CTkLabel(self.inscription_frame, text="Date de Naissance :", font=('Karla', 16))
        self.date_naissanceP_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.date_naissanceP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.date_naissanceP_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Wilaya
        self.wilayaP_label = ct.CTkLabel(self.inscription_frame, text="Wilaya :", font=('Karla', 16))
        self.wilayaP_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.wilayaP_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.wilayaP_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Téléphone
        self.phone_nmbrP_label = ct.CTkLabel(self.inscription_frame, text="Téléphone:", font=('Karla', 16))
        self.phone_nmbrP_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbrP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.phone_nmbrP_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

       # Matricule
        '''self.matricule_Patient_label = ct.CTkLabel(self.inscription_frame, text="Matricule Patient:", font=('Karla', 16))
        self.matricule_Patient_label.grid(row=2, column=2, padx=20, pady=20, sticky="w")
        self.matricule_Patient_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.matricule_Patient_entry.grid(row=2, column=3, padx=20, pady=20, sticky="w")'''

        # Matricule
        self.sexe_Patient_label = ct.CTkLabel(self.inscription_frame, text="Sexe :",
                                                   font=('Karla', 16))
        self.sexe_Patient_label.grid(row=2, column=2, padx=20, pady=20, sticky="w")
        sexe=['Homme','Femme']
        self.sexe_Patient_entry = ct.CTkComboBox(self.inscription_frame, width=200, height=30, corner_radius=10,values=sexe, dropdown_fg_color='#FFFFFF',
                                                   font=('Karla', 14))
        self.sexe_Patient_entry.grid(row=2, column=3, padx=20, pady=20, sticky="w")

        # Groupage
        self.groupage_label = ct.CTkLabel(self.inscription_frame, text="Groupage: ", font=('Karla', 16))
        self.groupage_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        groupage = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        self.groupage_entry = ct.CTkComboBox(self.inscription_frame, values=groupage, dropdown_font=('Karla', 14),  width=200, height=30, corner_radius=10, font=('Karla', 14), dropdown_fg_color='#FFFFFF')
        self.groupage_entry.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        # Antecedents
        self.antecedents_label = ct.CTkLabel(self.inscription_frame, text="Antécédents", font=('Karla', 16))
        self.antecedents_label.grid(row=3, column=2, padx=20, pady=20, sticky="w")
        self.antecedents_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.antecedents_entry.grid(row=3, column=3, padx=20, pady=20, sticky="w")

        # Button to Create Account
        self.enregistrer_patient = ct.CTkButton(self.inscription_frame, text="Créer", command=self.creer, width=250,
                                                height=40, corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#263A5F',
                                                cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_patient.grid(row=4, column=1, columnspan=2, pady=8)

        # Load the image

        image_path = 'Hemato Desk logo.png'  # Ensure this path is correct
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(3, 3)  # Resize to one-third of the original size

        # Create the Label with the image
        label_image = Label(self.label_frame, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Keep a reference to the image to prevent garbage collection
        label_image.pack()

    def creer(self):
        if (self.nomP_entry.get() == "" or self.prenomP_entry.get() == "" or self.date_naissanceP_entry.get() == ""
                or self.wilayaP_entry.get() == "" or self.phone_nmbrP_entry.get() == ""
                or self.groupage_entry.get() == ""):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        else:
            try:
                # Établir une connexion à la base de données
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()

                # Récupération du matricule_administrateur à partir de la table administrateur
                cur.execute("SELECT matricule_administrateur FROM administrateur")
                matricule_administrateur = cur.fetchone()[0]

                # Insertion des données dans la table patient avec vérification de l'existence du matricule_administrateur
                cur.execute("""
                       INSERT INTO patient (nom, prenom, date_de_naissance, sexe, wilaya, telephone, groupage, antecedents,FKmatricule_administrateur) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                   """,
                            (
                                self.nomP_entry.get(), self.prenomP_entry.get(),
                                transform_date(self.date_naissanceP_entry.get()), self.sexe_Patient_entry.get(),
                                self.wilayaP_entry.get(), self.phone_nmbrP_entry.get(),
                                self.groupage_entry.get(), self.antecedents_entry.get(),
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
        self.date_naissanceP_entry.delete(0, END),
        self.wilayaP_entry.delete(0, END),
        self.phone_nmbrP_entry.delete(0, END),
        self.antecedents_entry.delete(0,END)
class Ajouter_RDV(ct.CTkToplevel):
    def __init__(self, parent):  # Add parent as an argument
        super().__init__(parent)
        self.title("Ajouter RDV")
        self.geometry('850x500+300+100')
        self.configure(bg='#263A5F')

        self.formulaire_frame = ct.CTkFrame(self, fg_color='#FFFFFF', width=800, height=490, border_width=2,
                                            border_color='#263A5F', corner_radius=0)
        self.formulaire_frame.pack(expand=True, fill='both')

        # Frame for the title label
        self.label_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.label_frame.pack(pady=2)

        self.title_label = ct.CTkLabel(self.label_frame, text="Ajouter RDV", font=('Karla', 18, 'bold'),
                                       text_color='#263A5F')
        self.title_label.pack(expand=True, pady=10)

        # Frame for inscription form using grid
        self.inscription_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.inscription_frame.pack(pady=10)

        # Date de creation
        self.date_de_creation_label = ct.CTkLabel(self.inscription_frame, text="Date de création :", font=('Karla', 16),
                                                  text_color='#263A5F')
        self.date_de_creation_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.calender_image = Image.open('calendar-removebg-preview.png').resize((45, 45))
        self.calender_icon = ImageTk.PhotoImage(self.calender_image)

        today_date = datetime.now().strftime('%d/%m/%Y')
        self.date_de_creation_entry = ct.CTkEntry(self.inscription_frame, width=200, height=35, corner_radius=10,
                                                  font=('Karla', 14))
        self.date_de_creation_entry.insert(0, today_date)
        self.date_de_creation_entry.configure(state='readonly')
        self.date_de_creation_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        # Date du rendez-vous
        self.date_rdv_label = ct.CTkLabel(self.inscription_frame, text="Date du rendez-vous :", font=('Karla', 16),
                                          text_color='#263A5F')
        self.date_rdv_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")

        self.date_rdv_entry = ct.CTkEntry(self.inscription_frame, width=200, height=35, corner_radius=10,
                                          font=('Karla', 14))
        self.date_rdv_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Ajouter l'icône de calendrier
        self.show_calendar_button = Button(self.inscription_frame, image=self.calender_icon, width=25, height=30,
                                           command=self.open_calendar, bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                                           highlightthickness=0)
        self.show_calendar_button.place(x=1200, y=40)

        # Patient
        self.patient_label = ct.CTkLabel(self.inscription_frame, text="Patient :", font=('Karla', 16),
                                         text_color='#263A5F')
        self.patient_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.patient_entry = ct.CTkEntry(self.inscription_frame, width=200, height=35, corner_radius=10,
                                         font=('Karla', 14))
        self.patient_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Medecin
        self.medecin_label = ct.CTkLabel(self.inscription_frame, text="Médecin :", font=('Karla', 16),
                                         text_color='#263A5F')
        self.medecin_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")

        self.medecin_entry = ct.CTkEntry(self.inscription_frame, width=200, height=35, corner_radius=10,
                                         font=('Karla', 14))
        self.medecin_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Geste medical
        self.geste_medical_label = ct.CTkLabel(self.inscription_frame, text="Geste médical :", font=('Karla', 16),
                                               text_color='#263A5F')
        self.geste_medical_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")

        gestes = ["Transfusion", "Chimiothérapie", "Frotis", "Contrôle", "BOM", "CUP", "Facteur", "Moelle"]
        self.geste_medical_combobox = ct.CTkComboBox(self.inscription_frame, values=gestes, width=200, height=35,
                                                     corner_radius=10, font=('Karla', 14), dropdown_fg_color='#FFFFFF')
        self.geste_medical_combobox.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        # Button to Create Account
        self.creer_button = ct.CTkButton(self.inscription_frame, text="Créer", command=self.creer, width=250, height=40,
                                         corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#263A5F',
                                         cursor='hand2', text_color='#FFFFFF')
        self.creer_button.grid(row=7, column=1, columnspan=2, pady=30)

        # Image
        image_path = 'Hemato Desk logo.png'
        self.original_image = Image.open(image_path).resize((150, 150))
        self.nouvelle_image = ImageTk.PhotoImage(self.original_image)

        self.logo_label = Label(self.label_frame, image=self.nouvelle_image, bg="white")
        self.logo_label.image = self.nouvelle_image  # Garde une référence à l'image
        self.logo_label.pack()

    def open_calendar(self):
        # Crée un frame flottant pour le calendrier
        self.calendar_frame = Frame(self.formulaire_frame, bg='#FFFFFF', bd=2, relief='raised')
        self.calendar_frame.place(x=1000, y=330)  # Ajustez les coordonnées selon vos besoins

        self.cal = Calendar(self.calendar_frame, selectmode="day",  locale="fr_FR",date_pattern="dd/mm/yyyy")
        self.cal.pack(padx=10, pady=10)

        self.select_button = Button(self.calendar_frame, text="Sélectionner", command=self.select_date, bg='#263A5F',
                                    fg='#FFFFFF')
        self.select_button.pack(pady=10)

    def select_date(self):
        # Récupérer la date sélectionnée et l'afficher dans l'entrée
        selected_date = self.cal.get_date()
        self.date_rdv_entry.delete(0, END)
        self.date_rdv_entry.insert(0, selected_date)
        self.calendar_frame.destroy()

    def creer(self):
        if (self.date_rdv_entry.get() == "" or self.date_de_creation_entry.get() == "" or self.patient_entry.get() == ""
                or self.medecin_entry.get() == "" or self.geste_medical_combobox.get() == ""):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()
                # Récupération du matricule_patient à partir de la table patient
                cur.execute("SELECT matricule_patient FROM patient WHERE nom = %s", (self.patient_entry.get(),))
                matricule_patient = cur.fetchone()
                if matricule_patient is None:
                    messagebox.showerror("Erreur", "Patient non trouvé", parent=self)
                    return
                matricule_patient = matricule_patient[0]

                # Récupération du matricule_medecin à partir de la table medecin
                cur.execute("SELECT matricule_medecin FROM medecin WHERE nom = %s", (self.medecin_entry.get(),))
                matricule_medecin = cur.fetchone()
                if matricule_medecin is None:
                    messagebox.showerror("Erreur", "Médecin non trouvé", parent=self)
                    return
                matricule_medecin = matricule_medecin[0]

                # Insert the data into your database (adjust the table name and columns as needed)
                cur.execute(
                    """INSERT INTO rendez_vous (date_creation_du_rendez_vous, date_du_rendez_vous, patient, matricule_patient, geste_medical, medecin, matricule_medecin, validation) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                    (transform_date(self.date_de_creation_entry.get()), transform_date(self.date_rdv_entry.get()), self.patient_entry.get(),
                     matricule_patient, self.geste_medical_combobox.get(), self.medecin_entry.get(), matricule_medecin,
                     'Non validé')
                )
                con.commit()
                self.vider()
                con.close()
                messagebox.showinfo("Succès", "Inscription réussie", parent=self)
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)

    def vider(self):
        self.date_rdv_entry.delete(0, END),
        self.patient_entry.delete(0, END),
        self.medecin_entry.delete(0, END),

class Accueil(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Accueil")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#78BDCC')
        # Top frame
        self.top_frame = ct.CTkFrame(self, fg_color='#28A0C6', width=w, height=200, corner_radius=0)
        self.top_frame.place(x=0, y=0)
        label_text = Label(self.top_frame, text="Service Hématologie", font=('Karla', 48, 'bold'), bg="#28A0C6")
        label_text.place(x=750, y=60)

        #button ajouter patient
        self.ajouter_patient = ct.CTkButton(self.top_frame, text="+ Ajouter Patient", command=self.open_toplevelP,
                                            width=150, height=40,
                                            corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#EF3535',
                                            cursor='hand2', text_color='#FFFFFF')
        self.ajouter_patient.place(x=1100, y=120)

        self.ajouter_RV = ct.CTkButton(self.top_frame, text="+ Ajouter Rendez-vous", command=self.open_toplevelRDV, width=150,
                                       height=40,
                                       corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#2FC16A',
                                       cursor='hand2', text_color='#FFFFFF')
        self.ajouter_RV.place(x=890, y=120)

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

        # Left frame
        self.left_frame = ct.CTkFrame(self, fg_color='#28A0C6', width=250, height=h - 250, corner_radius=0)
        self.left_frame.place(x=0, y=200)

        buttons_info = [
            ("Liste des Patients", self.show_patients_tab),
            ("Consultation", self.show_consultations),
            ("Liste des Rendez-vous", self.show_appointments_tab),
            ("Ajouter Médecin", self.report_appointments),
            ("Liste des Médecin", self.show_doctors_tab),
            ("Statistique", self.show_statistics),
            ("Paramètres", self.show_settings)
        ]

        for idx, (text, command) in enumerate(buttons_info):
            button = ct.CTkButton(self.left_frame, text=text, command=command, width=200,
                                  height=45, corner_radius=15, font=('Karla', 16, 'bold'), fg_color="transparent",
                                  cursor='hand2', text_color='#FFFFFF', hover_color="#1E88E5")
            button.place(x=25, y=30 + 60 * idx)

        # Center frame
        self.center_frame = ct.CTkScrollableFrame(self, fg_color='#ffffff', border_width=2, border_color='#263A5F', width=w - 275, height=h - 290, corner_radius=0, orientation="vertical")
        self.center_frame.place(x=250, y=200)

        self.toplevelDocteur_window = None
        self.toplevelP_window = None
        self.toplevelRDV_window = None

    def rechercher_patient(self):
        nom_prenom = self.rech_txt.get().split()  # Récupérer le nom et prénom du patient saisi dans la barre de recherche

        # Connexion à la base de données
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()

        # Rechercher le patient dans la table patient
        if len(nom_prenom) == 1:
            # Rechercher par nom ou prénom
            cur.execute("SELECT * FROM patient WHERE nom LIKE %s OR prenom LIKE %s",
                        (f"%{nom_prenom[0]}%", f"%{nom_prenom[0]}%"))
        else:
            # Rechercher par nom et prénom
            nom, prenom = nom_prenom
            cur.execute("SELECT * FROM patient WHERE nom LIKE %s AND prenom LIKE %s", (f"%{nom}%", f"%{prenom}%"))

        patients = cur.fetchall()

        # Effacer le Treeview
        for item in self.treeview_patients.get_children():
            self.treeview_patients.delete(item)

        # Ajouter les patients trouvés dans le Treeview
        for patient in patients:
            self.add_patient(self.treeview_patients, patient)

        # Vider la zone de recherche
        self.rech_txt.delete(0, tk.END)  # <--- Add this line

        con.close()
    def create_patients_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff", font=('Karla', 16), rowheight=60)
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 24, 'bold'), foreground="#1C1278")
        # Tableau Treeview
        columns = ('Matricule', 'Nom', 'Prénom', 'Date de naissance', 'Téléphone', 'Groupage', 'Modifier', 'Voir')
        self.treeview_patients = ttk.Treeview(self.center_frame, columns=columns, show='headings', style="Custom.Treeview")
        self.treeview_patients.pack(expand=True, fill='both')

        # Définition des en-têtes
        for col in columns:
            self.treeview_patients.heading(col, text=col, anchor='center')
            if col not in ['Modifier', 'Voir']:
                self.treeview_patients.column(col, anchor='center', width=150)

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
        self.treeview_appointments.pack(expand=True, fill='both')

        # Définition des en-têtes
        for col in columns:
            self.treeview_appointments.heading(col, text=col, anchor='center')
            self.treeview_appointments.column(col, anchor='center', width=150)

        self.treeview_appointments.bind("<Button-1>", self.on_click_RDV)

    def create_doctor_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff", font=('Karla', 16))
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 26, 'bold'))

        # Treeview Table
        columns = ('Matricule', 'Nom','Prénom', 'Grade', 'Téléphone', 'Modifier', 'Voir')
        self.treeview_doctors = ttk.Treeview(self.center_frame, columns=columns, show='headings',
                                                  style="Custom.Treeview")
        self.treeview_doctors.pack(expand=True, fill='both')

        # Définition des en-têtes
        for col in columns:
            self.treeview_doctors.heading(col, text=col, anchor='center')
            if col not in ['Modifier', 'Voir']:
                self.treeview_doctors.column(col, anchor='center',
                                                  width=150 if col not in ['Modifier', 'Voir'] else 60)




    def add_appointment(self, treeview, date, heure, patient, medecin):
        treeview.insert('', 'end', values=(date, heure, patient, medecin, 'Modifier', 'Voir'))

    def add_consultation(self, treeview, date, heure, patient, medecin, notes):
        treeview.insert('', 'end', values=(date, heure, patient, medecin, notes, 'Modifier', 'Voir'))

    def add_buttons(self, treeview, item):
        # Implementing button-like behavior in Treeview is complex. A common alternative is to add a double-click event or a context menu.
        pass

    def modify_item(self, treeview, item):
        values = treeview.item(item, 'values')
        print(f'Modifying item: {values}')

    def view_item(self, treeview, item):
        values = treeview.item(item, 'values')
        print(f'Viewing item: {values}')

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

        # Create and display the treeview for appointments
        self.create_patients_treeview()
        # Effacer le Treeview
        for item in self.treeview_patients.get_children():
            self.treeview_patients.delete(item)

        # Connexion à la base de données
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()

        # Récupération des données des patients depuis la table
        cur.execute("SELECT matricule_patient, nom, prenom, date_de_naissance, telephone, groupage FROM patient")
        rows = cur.fetchall()
        for row in rows:
            # Appeler add_patient avec les valeurs appropriées
            self.add_patient(self.treeview_patients,row)  # Sélectionnez les six premières valeurs de la ligne

            # Lier l'événement de clic à la fonction on_click
        self.treeview_patients.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        item = self.treeview_patients.focus()  # Obtient l'élément actuellement sélectionné dans Treeview
        values = self.treeview_patients.item(item, 'values')  # Obtient les valeurs des colonnes de l'élément
        if values:
            # Ouvre une nouvelle fenêtre avec les valeurs de l'élément
            self.new_window = ct.CTkToplevel(self)
            self.new_window .grab_set()
            self.new_window.title("Détails du Patient")
            self.new_window.geometry("760x450+300+200")

            self.menu_frame = ct.CTkFrame(self.new_window, width=760, height=50, border_width=0,corner_radius=0,
                                     fg_color='#B8F9FF')
            self.menu_frame.pack()

            show_butt = ct.CTkButton(self.menu_frame, text="Voir dossier patient", command=lambda: self.afficher_informations_patient(self.info_frame, values), width=50, height=30,
                                     corner_radius=15, font=('Karla', 14, 'bold'), fg_color='#FF0000', cursor='hand2',
                                     text_color='#FFFFFF')
            show_butt.place(x=25, y=10)

            history_butt = ct.CTkButton(self.menu_frame, text="Voir suivi patient", command=lambda: self.afficher_suivi_patient(values[0]), width=50, height=30,
                                        corner_radius=15, font=('Karla', 14, 'bold'), fg_color='#FF0000', cursor='hand2',
                                        text_color='#FFFFFF')
            history_butt.place(x=310, y=10)

            modifier_butt = ct.CTkButton(self.menu_frame, text="Consultation", command=lambda: self.ajouter_consultation_patient(self.info_frame, values[0], values[1]),
                                         corner_radius=15, font=('Karla', 14, 'bold'), fg_color='#FF0000', cursor='hand2',
                                         text_color='#FFFFFF')
            modifier_butt.place(x=600, y=10)

            self.info_frame = ct.CTkFrame(self.new_window, width=697, height=400, border_color='#FF0000', border_width=2,
                                          fg_color='transparent')
            self.info_frame.pack(fill='both', expand=True)
            # Appeler afficher_informations_patient pour afficher les informations par défaut
            self.afficher_informations_patient(self.info_frame, values)

    def afficher_informations_patient(self, info_frame, values):
        for widget in self.info_frame.winfo_children():
            widget.destroy()
        # Crée un cadre pour afficher les informations du patient
        details_frame = ct.CTkFrame(self.info_frame, fg_color='#ffffff')
        details_frame.pack(fill='both', expand=True)

        # Ajoute des libellés pour afficher les détails du patient
        labels = ['Matricule:', 'Nom:', 'Prénom:', 'Date de naissance:', 'Téléphone:', 'Groupage:']
        for i, (label_text, value) in enumerate(zip(labels, values)):
            label = ct.CTkLabel(details_frame, text=label_text, font=('Karla', 16))
            label.grid(row=i, column=0, sticky='w', padx=10, pady=5)
            value_label = ct.CTkLabel(details_frame, text=value, font=('Karla', 16))
            value_label.grid(row=i, column=1, sticky='w', padx=10, pady=5)

    def afficher_suivi_patient(self, matricule_patient):
        try:
            # Établir une connexion à la base de données
            con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
            cur = con.cursor()

            # Requête SQL pour obtenir les consultations du patient
            # Requête SQL pour obtenir les consultations du patient avec les noms des médecins
            # Date d'aujourd'hui
            today_date = datetime.now().date()

            # Requête SQL pour obtenir les consultations du patient qui ont eu lieu avant aujourd'hui
            cur.execute(
                """
                SELECT date_de_consultation, geste_medical, diagnostique, medecin
                FROM historique_consultations
                WHERE matricule_patient = %s AND date_de_consultation <= %s
                """,
                (matricule_patient, today_date)
            )
            rows = cur.fetchall()
            # Débogage
            print("Résultats de la requête SQL :")
            for row in rows:
                print(row)

            # Afficher les consultations dans un nouveau cadre
            for widget in self.info_frame.winfo_children():
                widget.destroy()

            consultations_frame = ct.CTkScrollableFrame(self.info_frame, fg_color='#ffffff',corner_radius=0)
            consultations_frame.pack(fill='both', expand=True)

            # Ajouter des libellés pour les colonnes
            headers = ['Date de Consultation', 'Geste Médical', 'Diagnostique','Médecin traitant']
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
        self.titre_label = ct.CTkLabel(Consultation_frame, text="Ajouter une consultation :", font=('Karla',18,'bold'),
                                             text_color='#263A5F')
        self.titre_label.grid(row=0,column=1,padx=10,pady=10,sticky="w")
        # Date de création
        self.date_de_creation_label = ct.CTkLabel(Consultation_frame, text="Date de création :", font=('Karla', 16),
                                             text_color='#263A5F')
        self.date_de_creation_label.grid(row=4, column=2, padx=10, pady=10, sticky="w")

        today_date = datetime.now().strftime('%d/%m/%Y')
        self.date_de_creation_entry = ct.CTkEntry(Consultation_frame, width=200, height=35, corner_radius=10,
                                             font=('Karla', 14))
        self.date_de_creation_entry.insert(0, today_date)
        self.date_de_creation_entry.configure(state='readonly')
        self.date_de_creation_entry.grid(row=4, column=3, padx=10, pady=10, sticky="w")

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
        gestes = ["Transfusion", "Chimiothérapie", "Frotis", "Contrôle", "BOM", "CUP", "Facteur", "Moelle"]
        self.geste_medical_combobox = ct.CTkComboBox(Consultation_frame, values=gestes, width=200, height=30,
                                                     corner_radius=10, font=('Karla', 14), dropdown_fg_color='#FFFFFF')
        self.geste_medical_combobox.grid(row=3, column=1, padx=10, pady=10, sticky="w")


        # le médecin de la consultation

        self.nom_medecin_label = ct.CTkLabel(Consultation_frame, text="Médecin:", font=('Karla', 16),
                                        text_color='#263A5F')
        self.nom_medecin_label.grid(row=3, column=2, padx=10, pady=10, sticky="w")

        self.nom_medecin_entry = ct.CTkEntry(Consultation_frame, width=200, height=35, corner_radius=10, font=('Karla', 14))
        self.nom_medecin_entry.grid(row=3, column=3, padx=10, pady=10, sticky="w")

        # Libellé pour le diagnostique
        self.diagnostique_label = ct.CTkLabel(Consultation_frame, text="Diagnostique :", font=('Karla', 16),
                                         text_color='#263A5F')
        self.diagnostique_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Champ de saisie de texte pour le diagnostique
        self.diagnostique_entry = ct.CTkTextbox(Consultation_frame, width=200, height=150, corner_radius=10,
                                           font=('Karla', 14))
        self.diagnostique_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        # Button to Create Account
        self.enregistrer_consultation= ct.CTkButton(Consultation_frame, text="+Ajouter Consultation", command=self.creer_consultation, width=250,
                                                height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                                fg_color='#263A5F',
                                                cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_consultation.grid(row=5, column=1, columnspan=2, pady=8)

    def creer_consultation(self):
        if self.nom_medecin_entry.get() == "" or self.diagnostique_entry.get("1.0", tk.END) == "":
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
                    diagnostique = self.diagnostique_entry.get("1.0", tk.END)  # Récupérer tout le texte

                    # Requête SQL pour insérer les données de consultation
                    query_insert = "INSERT INTO  historique_consultations (matricule_patient, matricule_medecin, 	date_de_consultation, geste_medical, diagnostique) VALUES (%s, %s, %s, %s, %s)"

                    # Exécuter la requête SQL pour l'insertion
                    cur.execute(query_insert,
                                (matricule_patient, matricule_medecin, date_creation, geste_medical, diagnostique))

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


    def show_appointments_tab(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

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
        item = self.treeview_appointments.focus()  # Obtient l'élément actuellement sélectionné dans Treeview
        values = self.treeview_appointments.item(item, 'values')  # Obtient les valeurs des colonnes de l'élément
        if values:
            # Obtenez la valeur de matricule_RDV (remplacez l'index 0 par l'index correct)
            self.id_rendez_vous = values[0]
            # Ouvre une nouvelle fenêtre avec les valeurs de l'élément
            self.new_window = ct.CTkToplevel(self)
            self.new_window.grab_set()
            self.new_window.title("Détails du Rendez-vous")
            self.new_window.geometry("650x400+400+200")

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
        labels = ['N°RDV','Date de Création du  Rendez-vous', 'Patient', 'Geste médical']
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
        self.show_calendar_button.place(x=680, y=200)

        # Button to report RDV
        self.report_button = ct.CTkButton(self.RDV_frame, text="Reporter RDV",
                                          command=lambda: self.report_RDV_to_database(self.id_rendez_vous),
                                          width=250, height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                          fg_color='#263A5F', cursor='hand2', text_color='#FFFFFF')
        self.report_button.grid(row=3, column=1, pady=30)

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

    def report_RDV_to_database(self, matricule_RDV):
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
        cur.execute("SELECT matricule_medecin  , nom,prenom,grade,grade FROM medecin")
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
            "SELECT patient, date_du_rendez_vous, geste_medical FROM rendez_vous WHERE date_du_rendez_vous = %s",
            (date,))
        rows = cur.fetchall()
        for row in rows:
            patient_name = row[0].split(' ')[0]
            medical_gesture_name = row[2]
            filtered_appointments.append({
                'date': row[1],
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

        columns = ("Date", "Patient", "Geste médical")
        self.treeview_consultations = ttk.Treeview(self.center_frame, columns=columns, show="headings",
                                                   style="Custom.Treeview")
        self.treeview_consultations.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Définition des en-têtes
        for col in columns:
            self.treeview_consultations.heading(col, text=col, anchor='center')
            self.treeview_consultations.column(col, anchor='center', width=150)

        # Add the appointments to the treeview
        for appointment in appointments:
            self.treeview_consultations.insert('', 'end', values=(
                appointment['date'], appointment['patient'], appointment['medical_gesture']
            ))
    def create_administrateur_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff",
                        font=('Karla', 16), rowheight=60)
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 24, 'bold'), foreground="#1C1278")

        # Tableau Treeview
        columns = ("Matricule", "Mot de passe", "Nom", "Prénom", "Date de naissance", "Téléphone", "Supprimer")
        self.treeview_administrateurs = ttk.Treeview(self.center_frame, columns=columns, show="headings",
                                                     style="Custom.Treeview")
        self.treeview_administrateurs.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Définition des en-têtes
        for col in columns:
            self.treeview_administrateurs.heading(col, text=col, anchor='center')
            if col not in ['Supprimer']:
                self.treeview_administrateurs.column(col, anchor='center', width=150)

        # Add a delete button to each row
        def add_delete_button(treeview, row):
            matricule_administrateur = row[0]

            # Create the delete button
            delete_button = ttk.Button(self.center_frame, text="Supprimer", style="Custom.TButton",
                                       command=lambda
                                           matricule_administrateur: self.delete_administrateur(
                                           matricule_administrateur))

            # Add the button to the row
            treeview.insert("", "end", values=row + (delete_button,), tags=("delete_button",))

        # Populate the Treeview with data
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()
        cur.execute(
            "SELECT matricule_administrateur, mot_de_passe, nom, prenom, date_de_naissance, telephone FROM administrateur")
        rows = cur.fetchall()
        cur.close()
        con.close()

        for row in rows:
            add_delete_button(self.treeview_administrateurs, row)

        # Configure the delete button tag
        self.treeview_administrateurs.tag_configure("delete_button",  font=('Karla', 16, 'bold'))

    def show_settings(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Create and display the treeview for administrateurs
        self.create_administrateur_treeview()

        # Connexion à la base de données
        con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
        cur = con.cursor()

        # Récupération des données des administrateurs depuis la table
        cur.execute(
            "SELECT matricule_administrateur, mot_de_passe, nom, prenom, date_de_naissance, telephone FROM administrateur")
        rows = cur.fetchall()
        cur.close()
        con.close()

        for row in rows:
            # Appeler add_administrateur avec les valeurs appropriées
            self.add_administrateur(self.treeview_administrateurs,
                                    row)  # Sélectionnez les six premières valeurs de la ligne

    def add_administrateur(self, treeview, row):
        matricule_administrateur = row[0]
        mot_de_passe = row[1]
        nom = row[2]
        prenom = row[3]
        date_de_naissance = row[4]
        telephone = row[5]
    def show_statistics(self):
        print("Show statistiques")

    def open_toplevelP(self):
        if self.toplevelP_window is None or not self.toplevelP_window.winfo_exists():
            self.toplevelP_window = Inscrire_patient(self)  # create window if its None or destroyed
            self.toplevelP_window.grab_set()  # Make the new window modal
        else:
            self.toplevelP_window.focus()  # if window exists focus it

    def open_toplevelRDV(self):
        if self.toplevelRDV_window is None or not self.toplevelRDV_window.winfo_exists():
            self.toplevelRDV_window = Ajouter_RDV(self)  # create window if its None or destroyed
            self.toplevelRDV_window.grab_set()  # Make the new window modal
        else:
            self.toplevelRDV_window.focus()  # if window exists focus it

    def open_toplevelDocteur(self):
        if self.toplevelDocteur_window is None or not self.toplevelDocteur_window.winfo_exists():
            self.toplevelDocteur_window= Inscrire(self)  # create window if its None or destroyed
            self.toplevelDocteur_window.grab_set()  # Make the new window modal
        else:
            self.toplevelDocteur_window.focus()  # if window exists focus it



app = Accueil()
app.mainloop()


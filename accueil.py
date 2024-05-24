import customtkinter as ct
from tkinter import  ttk
from tkinter import *
from tkinter import messagebox
import pymysql
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk


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
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()

                # Récupération du matricule_administrateur à partir de la table administrateur
                cur.execute("SELECT matricule_administrateur FROM administrateur")
                matricule_administrateur = cur.fetchone()[0]

                # Insertion des données dans la table patient avec vérification de l'existence du matricule_administrateur
                cur.execute("""
                    INSERT INTO patient (nom, prenom, date_naissance, sexe, wilaya, telephone, groupage, antecedents, matricule_administrateur) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                            (
                                self.nomP_entry.get(), self.prenomP_entry.get(),
                                self.date_naissanceP_entry.get(), self.sexe_Patient_entry.get(),
                                self.wilayaP_entry.get(), self.phone_nmbrP_entry.get(),
                                self.groupage_entry.get(), self.antecedents_entry.get(),
                                matricule_administrateur
                            ))

                con.commit()
                con.close()
                messagebox.showinfo("Succès", "Inscription réussie", parent=self)
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'inscription : {str(e)}", parent=self)
                print(str(e))

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
                # Insert the data into your database (adjust the table name and columns as needed)
                cur.execute(
                    "INSERT INTO rendez-vous (date_création_du_rendez-vous, date_du_rendez-vous,matricule_patient, geste_medical,matricule_medecin) VALUES (%s, %s, %s,%s, %s)",
                    (self.date_de_creation_entry.get(), self.date_rdv_entry.get(),self.patient_entry.get(), self.geste_medical_combobox.get(),self.medecin_entry.get()
                     ))
                con.commit()
                con.close()
                messagebox.showinfo("Succès", "Inscription réussie", parent=self)
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)

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
        self.rech_txt_butt = ct.CTkButton(self.top_frame, text="Recherche", command=None, width=110,
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
            ("Reporter Rendez-vous", self.report_appointments),
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

        self.toplevelP_window = None
        self.toplevelRDV_window = None

    def create_patients_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff", font=('Karla', 16), rowheight=60)
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 26, 'bold'), foreground="#1C1278")

        # Treeview Table
        columns = ('Matricule', 'Nom', 'Prénom', 'Age', 'Groupage', 'Modifier', 'Voir')
        self.treeview_patients = ttk.Treeview(self.center_frame, columns=columns, show='headings', style="Custom.Treeview")
        self.treeview_patients.pack(expand=True, fill='both')

        # Define headings
        for col in columns:
            self.treeview_patients.heading(col, text=col, anchor='center')
            self.treeview_patients.column(col, anchor='center', width=150 if col not in ['Modifier', 'Voir'] else 60)  # Changer la largeur au besoin

        # Add some sample data
        self.add_patient(self.treeview_patients, '12345', 'Doe', 'John', '30', 'A+')
        self.add_patient(self.treeview_patients, '67890', 'Smith', 'Anna', '25', 'B+')

    def create_appointments_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff", font=('Karla', 16))
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 26, 'bold'))

        # Treeview Table
        columns = ('Date', 'Heure', 'Patient', 'Médecin', 'Modifier', 'Voir')
        self.treeview_appointments = ttk.Treeview(self.center_frame, columns=columns, show='headings', style="Custom.Treeview")
        self.treeview_appointments.pack(expand=True, fill='both')

        # Define headings
        for col in columns:
            self.treeview_appointments.heading(col, text=col, anchor='center')
            self.treeview_appointments.column(col, anchor='center', width=150 if col not in ['Modifier', 'Voir'] else 60)

        # Add some sample data
        self.add_appointment(self.treeview_appointments, '2024-05-22', '10:00', 'John Doe', 'Dr. Smith')
        self.add_appointment(self.treeview_appointments, '2024-05-23', '14:00', 'Anna Smith', 'Dr. Johnson')

    def create_doctor_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff", font=('Karla', 16))
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 26, 'bold'))

        # Treeview Table
        columns = ('Matricule', 'Nom', 'Grade', 'Téléphone', 'Modifier', 'Voir')
        self.treeview_doctors = ttk.Treeview(self.center_frame, columns=columns, show='headings', style="Custom.Treeview")
        self.treeview_doctors.pack(expand=True, fill='both')

        # Define headings
        for col in columns:
            self.treeview_doctors.heading(col, text=col, anchor='center')
            self.treeview_doctors.column(col, anchor='center', width=150 if col not in ['Modifier', 'Voir'] else 60)

    def create_consultations_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff", font=('Karla', 16))
        style.map("Custom.Treeview", background=[('selected', '#263A5F')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 26, 'bold'))

        # Treeview Table
        columns = ('Date', 'Heure', 'Patient', 'Médecin', 'Notes', 'Modifier', 'Voir')
        self.treeview_consultations = ttk.Treeview(self.center_frame, columns=columns, show='headings', style="Custom.Treeview")
        self.treeview_consultations.pack(expand=True, fill='both')

        # Define headings
        for col in columns:
            self.treeview_consultations.heading(col, text=col, anchor='center')
            self.treeview_consultations.column(col, anchor='center', width=150 if col not in ['Modifier', 'Voir'] else 60)

        # Add some sample data
        self.add_consultation(self.treeview_consultations, '2024-05-22', '10:00', 'John Doe', 'Dr. Smith', 'Regular checkup')
        self.add_consultation(self.treeview_consultations, '2024-05-23', '14:00', 'Anna Smith', 'Dr. Johnson', 'Follow-up')

    def add_patient(self, treeview, matricule, nom, prenom, age, groupage):
        treeview.insert('', 'end', values=(matricule, nom, prenom, age, groupage, 'Modifier', 'Voir'))

    def add_doctor(self, treeview, matricule, nom, grade, telephone):
        treeview.insert('', 'end', values=(matricule, nom, grade, telephone, 'Modifier', 'Voir'))

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

    def show_patients_tab(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Create and display the treeview for patients
        self.create_patients_treeview()

    def show_appointments_tab(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Create and display the treeview for appointments
        self.create_appointments_treeview()

    def show_doctors_tab(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Create and display the treeview for doctors
        self.create_doctor_treeview()

    def report_appointments(self):
        print("Report appointments")

    def show_consultations(self):
        # Clear the center frame
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        # Create and display the treeview for consultations
        self.create_consultations_treeview()

    def show_statistics(self):
        print("Show statistics")

    def show_settings(self):
        print("Show settings")
    def open_toplevelP(self):
        if self.toplevelP_window is None or not self.toplevel_window.winfo_exists():
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


app = Accueil()
app.mainloop()

import customtkinter as ct
from tkinter import PhotoImage, Label, ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
class Inscrire_patient(ct.CTk):
    def __init__(self):
        super().__init__()
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

        # Nom and Prénom in the same row
        self.nom_label = ct.CTkLabel(self.inscription_frame, text="Nom :", font=('Karla', 16))
        self.nom_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.nom_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.nom_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenom_label = ct.CTkLabel(self.inscription_frame, text="Prénom :", font=('Karla', 16))
        self.prenom_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")
        self.prenom_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.prenom_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Date de Naissance
        self.date_naissance_label = ct.CTkLabel(self.inscription_frame, text="Date de Naissance :", font=('Karla', 16))
        self.date_naissance_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.date_naissance_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.date_naissance_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Wilaya
        self.wilaya_label = ct.CTkLabel(self.inscription_frame, text="Wilaya :", font=('Karla', 16))
        self.wilaya_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.wilaya_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.wilaya_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Téléphone
        self.phone_nmbr_label = ct.CTkLabel(self.inscription_frame, text="Téléphone:", font=('Karla', 16))
        self.phone_nmbr_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbr_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.phone_nmbr_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        '''# Matricule
        self.matricule_Patient_label = ct.CTkLabel(self.inscription_frame, text="Matricule Patient:", font=('Karla', 16))
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
        if (self.nom_entry.get() == "" or self.prenom_entry.get() == "" or self.date_naissance_entry.get() == ""
                or self.wilaya_entry.get() == "" or self.phone_nmbr_entry.get() == ""
                or self.matricule_Patient_entry.get() == "" or self.groupage_entry.get() == ""):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()
                # Insert the data into your database (adjust the table name and columns as needed)
                cur.execute("INSERT INTO patient (matricule_patient,nom, prenom, date_naissance, wilaya, telephone, groupage, antecedents) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (self.nom_entry.get(), self.prenom_entry.get(), self.date_naissance_entry.get(),
                             self.wilaya_entry.get(), self.phone_nmbr_entry.get(), self.matricule_Patient_entry.get(),
                             self.groupage_entry.get(), self.antecedents_entry.get()))
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
        self.ajouter_patient = ct.CTkButton(self.top_frame, text="+ Ajouter Patient", command=self.fenetre_patient,
                                            width=150, height=40,
                                            corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#EF3535',
                                            cursor='hand2', text_color='#FFFFFF')
        self.ajouter_patient.place(x=1100, y=120)

        self.ajouter_RV = ct.CTkButton(self.top_frame, text="+ Ajouter Rendez-vous", command=None, width=150,
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
    def fenetre_patient(self):
        import patient


app = Accueil()
app.mainloop()

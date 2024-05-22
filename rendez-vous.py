from tkinter import messagebox

import customtkinter as ct
from tkinter import *

import pymysql
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk


class Ajouter_RDV(ct.CTk):
    def __init__(self):
        super().__init__()
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
        self.date_de_creation_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                                  font=('Karla', 14))
        self.date_de_creation_entry.insert(0, today_date)
        self.date_de_creation_entry.configure(state='readonly')
        self.date_de_creation_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        # Date du rendez-vous
        self.date_rdv_label = ct.CTkLabel(self.inscription_frame, text="Date du rendez-vous :", font=('Karla', 16),
                                          text_color='#263A5F')
        self.date_rdv_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")

        self.date_rdv_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                          font=('Karla', 14))
        self.date_rdv_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Ajouter l'icône de calendrier
        self.show_calendar_button = Button(self.inscription_frame, image=self.calender_icon, width=25, height=36,
                                           command=self.open_calendar, bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                                           highlightthickness=0)
        self.show_calendar_button.place(x=1210, y=34)

        # Patient
        self.patient_label = ct.CTkLabel(self.inscription_frame, text="Patient :", font=('Karla', 16),
                                         text_color='#263A5F')
        self.patient_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.patient_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                         font=('Karla', 14))
        self.patient_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Medecin
        self.medecin_label = ct.CTkLabel(self.inscription_frame, text="Médecin :", font=('Karla', 16),
                                         text_color='#263A5F')
        self.medecin_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")

        self.medecin_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                         font=('Karla', 14))
        self.medecin_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Geste medical
        self.geste_medical_label = ct.CTkLabel(self.inscription_frame, text="Geste médical :", font=('Karla', 16),
                                               text_color='#263A5F')
        self.geste_medical_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")

        gestes = ["Transfusion", "Chimiothérapie", "Frotis", "Contrôle", "BOM", "CUP", "Facteur", "Moelle"]
        self.geste_medical_combobox = ct.CTkComboBox(self.inscription_frame, values=gestes, width=200, height=30,
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


# Create an instance of the Ajouter_RDV class and start the main loop
app = Ajouter_RDV()
app.mainloop()

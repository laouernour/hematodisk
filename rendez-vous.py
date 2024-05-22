import customtkinter as ct
from tkinter import *
from tkinter import messagebox
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

        self.label = ct.CTkLabel(self.label_frame, text="Ajouter RDV :", font=('Karla', 18, 'bold'))
        self.label.pack(expand=True, pady=10)

        # Frame for inscription form using grid
        self.inscription_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.inscription_frame.pack(pady=10)

        # Date de creation
        self.nom_label = ct.CTkLabel(self.inscription_frame, text="Date de creation  :", font=('Karla', 16))
        self.nom_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.calender_image = Image.open('calendar-removebg-preview.png').resize((45, 45))
        self.calender = ImageTk.PhotoImage(self.calender_image)
        today_date = datetime.now().strftime('%d-%m-%Y')
        self.nom_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.nom_entry.insert(0, today_date)
        self.nom_entry.configure(state='readonly')
        self.nom_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        # Date du rendez-vous
        self.prenom_label = ct.CTkLabel(self.inscription_frame, text="Date du rendez-vous :", font=('Karla', 16))
        self.prenom_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")
        self.prenom_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                        font=('Karla', 14))
        self.prenom_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Ajouter l'icône de calendrier
        self.show_pass_button = Button(self.inscription_frame, image=self.calender, width=25, height=36,command=self.open_calendar, bd=0, bg='#FFFFFF', activebackground='#FFFFFF', highlightthickness=0)
        self.show_pass_button.place(x=1210, y=34)  # Ajustez les coordonnées en fonction de vos besoins

        # Patient
        self.date_naissance_label = ct.CTkLabel(self.inscription_frame, text="Patient :", font=('Karla', 16))
        self.date_naissance_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.date_naissance_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                                font=('Karla', 14))
        self.date_naissance_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Medecin
        self.wilaya_label = ct.CTkLabel(self.inscription_frame, text="Medecin :", font=('Karla', 16))
        self.wilaya_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.wilaya_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10,
                                        font=('Karla', 14))
        self.wilaya_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Geste medical
        self.groupage_label = ct.CTkLabel(self.inscription_frame, text="Geste medical: ", font=('Karla', 16))
        self.groupage_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        groupage = ["Transfusion", "Chimiotherapie", "Frotis", "Controle", "BOM", "CUP", "Facteur", "Moille"]
        self.groupage_entry = ct.CTkComboBox(self.inscription_frame, values=groupage, dropdown_font=('Karla', 14),
                                             width=200, height=30, corner_radius=10, font=('Karla', 14),
                                             dropdown_fg_color='#FFFFFF')
        self.groupage_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        # Button to Create Account
        self.enregistrer_patient = ct.CTkButton(self.inscription_frame, text="Créer", command=None, width=250,
                                                height=40, corner_radius=15, font=('Karla', 16, 'bold'),
                                                fg_color='#263A5F', cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_patient.grid(row=7, column=1, columnspan=2, pady=30)

        # Image
        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(3, 3)  # Redimensionne à la moitié de la taille originale
        label_image = Label(self.label_frame, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Garde une référence à l'image
        label_image.pack()  # Ajustez la position selon vos besoins

    def open_calendar(self):
        # Crée une nouvelle fenêtre pour le calendrier
        self.calendar_window = Toplevel(self)
        self.calendar_window.title("Sélectionner une date")

        self.cal = Calendar(self.calendar_window, selectmode="day", date_pattern="dd/mm/yyyy")
        self.cal.pack(padx=10, pady=10)

        self.select_button = Button(self.calendar_window, text="Sélectionner", command=self.select_date)
        self.select_button.pack(pady=10)

    def select_date(self):
        # Récupérer la date sélectionnée et l'afficher dans l'entrée
        selected_date = self.cal.get_date()
        self.prenom_entry.delete(0, END)
        self.prenom_entry.insert(0, selected_date)
        self.calendar_window.destroy()


# Create an instance of the Ajouter_RDV class and start the main loop
app = Ajouter_RDV()
app.mainloop()

import customtkinter as ct
from tkinter import PhotoImage, Label, ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
class Accueil(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Accueil")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#78BDCC')
        # Top frame
        self.top_frame = ct.CTkFrame(self, fg_color='#28A0C6', width=w, height=160, corner_radius=0)
        self.top_frame.place(x=0, y=0)
        label_text = Label(self.top_frame, text="Service Hématologie", font=('Karla', 48, 'bold'), bg="#28A0C6")
        label_text.place(x=750, y=60)
        #button ajouter patient
        self.ajouter_patient = ct.CTkButton(self.top_frame, text="+ Ajouter Patient", command=None,
                                            width=150, height=40,
                                            corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#EF3535',
                                            cursor='hand2', text_color='#FFFFFF')
        self.ajouter_patient.place(x=1100, y=108)


        self.ajouter_RV = ct.CTkButton(self.top_frame, text="+ Ajouter Rendez-vous", command=None, width=150,
                                       height=40,
                                       corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#2FC16A',
                                       cursor='hand2', text_color='#FFFFFF')
        self.ajouter_RV.place(x=890, y=108)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Resize to half the original size
        label_imageL = Label(self.top_frame, image=nouvelle_image, bg="#28A0C6")
        label_imageL.image = nouvelle_image  # Keep a reference to the image
        label_imageL.place(x=80, y=50)

        # Recherche
        self.rech_txt = ct.CTkEntry(self.top_frame, width=300, height=35, corner_radius=10,
                                    font=('Karla', 14))
        self.rech_txt.place(x=250, y=108)
        self.rech_txt_butt = ct.CTkButton(self.top_frame, text="Recherche", command=None, width=110,
                                          height=30,
                                          corner_radius=15, font=('Karla', 14, 'bold'), fg_color='#2FC16A',
                                          cursor='hand2', text_color='#FFFFFF')
        self.rech_txt_butt.place(x=555, y=110)

        # Left frame
        self.left_frame = ct.CTkFrame(self, fg_color='#28A0C6', width=250, height=h - 50, corner_radius=0)
        self.left_frame.place(x=0, y=149)

        buttons_info = [
            ("Liste des Patients", self.show_patients_tab),
            ("Liste des Rendez-vous", self.show_appointments_tab),
            ("Reporter Rendez-vous", self.report_appointments),
            ("Consultation", self.show_consultations),
            ("Statistique", self.show_statistics),
            ("Paramètres", self.show_settings)
        ]

        for idx, (text, command) in enumerate(buttons_info):
            button = ct.CTkButton(self.left_frame, text=text, command=command, width=200,
                                  height=50, corner_radius=15, font=('Karla', 16, 'bold'), fg_color="transparent",
                                  cursor='hand2', text_color='#FFFFFF', hover_color="#1E88E5")
            button.place(x=25, y=50 + 70 * idx)

        # Center frame
        self.center_frame = ct.CTkScrollableFrame(self, fg_color='#ffffff', border_width=2, border_color='#263A5F', width=w - 275, height=h - 160, corner_radius=0)
        self.center_frame.place(x=250, y=150)
        # Définissez la méthode ouvrir_inscription_patient en dehors de __init__

    def create_patients_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff",font=('Karla', 16), rowheight=50)
        style.map("Custom.Treeview", background=[('selected', '#78BDCC')], foreground=[('selected', 'black')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla', 26, 'bold'))

        # Treeview Table
        columns = ('Matricule', 'Nom', 'Prénom', 'Age', 'Groupage', 'Modifier', 'Voir')
        self.treeview_patients = ttk.Treeview(self.center_frame, columns=columns, show='headings',
                                              style="Custom.Treeview")
        self.treeview_patients.pack(expand=True, fill='both')

        # Define headings
        for col in columns:
            self.treeview_patients.heading(col, text=col, anchor='center')
            self.treeview_patients.column(col, width=150, anchor='center')  # Changer la largeur au besoin

        # Add some sample data
        self.add_patient(self.treeview_patients, '12345', 'Doe', 'John', '30', 'A+')
        self.add_patient(self.treeview_patients, '67890', 'Smith', 'Anna', '25', 'B+')

    def create_appointments_treeview(self):
        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff",font=('Karla', 16))
        style.map("Custom.Treeview", background=[('selected', '#78BDCC')], foreground=[('selected', 'black')])

        # Configure the font for the column headings
        style.configure("Custom.Treeview.Heading", font=('Karla',26, 'bold'))

        # Treeview Table
        columns = ('Date', 'Patient','Groupage', 'Geste', 'Modifier', 'Voir')
        self.treeview_appointments = ttk.Treeview(self.center_frame, columns=columns, show='headings',
                                                  style="Custom.Treeview")
        self.treeview_appointments.pack(expand=True, fill='both')

        # Define headings
        for col in columns:
            self.treeview_appointments.heading(col, text=col, anchor='center')
            self.treeview_appointments.column(col, anchor='center',
                                              width=120 if col not in ['Modifier', 'Voir'] else 100)

        # Add some sample data
        self.add_appointment(self.treeview_appointments, '2024-05-22', '10:00', 'John Doe', 'Dr. Smith')
        self.add_appointment(self.treeview_appointments, '2024-05-23', '14:00', 'Anna Smith', 'Dr. Johnson')

    def add_patient(self, treeview, matricule, nom, prenom, age, groupage):
        item = treeview.insert('', 'end', values=(matricule, nom, prenom, age, groupage, 'Modifier', 'Voir'))
        self.add_buttons(treeview, item)

    def add_appointment(self, treeview, date, heure, patient, medecin):
        item = treeview.insert('', 'end', values=(date, heure, patient, medecin, 'Modifier', 'Voir'))
        self.add_buttons(treeview, item)

    def add_buttons(self, treeview, item):
        btn_modif = ct.CTkButton(treeview, text="Modifier", command=lambda: self.modify_item(treeview, item), fg_color='#FFA726', text_color='white', corner_radius=10)
        btn_voir = ct.CTkButton(treeview, text="Voir", command=lambda: self.view_item(treeview, item), fg_color='#42A5F5', text_color='white', corner_radius=10)
        treeview.set(item, 'Modifier', btn_modif)
        treeview.set(item, 'Voir', btn_voir)

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

    def report_appointments(self):
        print("Report appointments")

    def show_consultations(self):
        print("Show consultations")

    def show_statistics(self):
        print("Show statistics")

    def show_settings(self):
        print("Show settings")



app = Accueil()
app.mainloop()

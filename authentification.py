import tkinter as tk
import customtkinter as ct

class GradientFrame(tk.Canvas):
    '''A gradient frame that uses a canvas to draw the background'''
    def __init__(self, parent, color1="#E26D6D", color2="#3C517C", alpha=1.0, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self._alpha = alpha
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")

class login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Authentification")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d" % (w, h))

        # Chargement de l'image de fond
        self.bg_image = tk.PhotoImage(file="background1.png")

        # Création d'une étiquette pour l'image de fond et placement
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Création du frame pour les éléments de login
        frame_width = 600
        frame_height = 400
        frame_x = (w - frame_width) / 2
        frame_y = (h - frame_height) / 2

        self.login_frame = GradientFrame(self, width=frame_width, height=frame_height, alpha=0.5)
        self.login_frame.place(x=frame_x, y=frame_y)

        self.matricule=ct.CTkLabel(self.login_frame,text="Matricule :" ,font=('
        entry_matricule=ct.CTkEntry(self.login_frame,width=300,height=40,corner_radius=10)
        entry_matricule.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

        self.MP=ct.CTkLabel(self.login_frame,text="Mot de passe :" ,font=('Karla',20))
        self.MP.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
        entry_MP= ct.CTkEntry(self.login_frame, width=300, height=40, corner_radius=10)
        entry_MP.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.MP_oublier=ct.CTkLabel(self.login_frame,text='Mot de passe oublié ?',font=('Karla',16),text_color='#FFFFFF')
        self.MP_oublier.place(relx=0.8, rely=0.7, anchor=tk.CENTER)

        self.button=ct.CTkButton(self.login_frame,text='Se Connecter',font=('Karla',25),fg_color="#263A5F")
        self.button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.mainloop()




# Création d'une instance de la classe de fenêtre personnalisée et démarrage de la boucle principale
login()
#login.mainloop()
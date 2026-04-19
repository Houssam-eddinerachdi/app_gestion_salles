import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from services.services_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()


        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.cadreInfo, text="Code salle").grid(row=0, column=0, padx=10, pady=10)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.cadreInfo, text="Description").grid(row=1, column=0, padx=10, pady=10)
        self.entry_description = ctk.CTkEntry(self.cadreInfo)
        self.entry_description.grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.cadreInfo, text="Catégorie").grid(row=2, column=0, padx=10, pady=10)
        self.entry_categorie = ctk.CTkEntry(self.cadreInfo)
        self.entry_categorie.grid(row=2, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.cadreInfo, text="Capacité").grid(row=3, column=0, padx=10, pady=10)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=10)


        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)


        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        self.treeList.column("code", width=80)
        self.treeList.column("description", width=180)
        self.treeList.column("categorie", width=120)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        self.lister_salles()

    def vider_champs(self):
        self.entry_code.delete(0, "end")
        self.entry_description.delete(0, "end")
        self.entry_categorie.delete(0, "end")
        self.entry_capacite.delete(0, "end")

    def ajouter_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_description.get(),
                self.entry_categorie.get(),
                int(self.entry_capacite.get())
            )

            succes, message = self.service_salle.ajouter_salle(salle)
            if succes:
                messagebox.showinfo("Succès", message)
                self.vider_champs()
                self.lister_salles()
            else:
                messagebox.showerror("Erreur", message)

        except ValueError:
            messagebox.showerror("Erreur", "La capacité doit être un nombre entier")

    def modifier_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_description.get(),
                self.entry_categorie.get(),
                int(self.entry_capacite.get())
            )

            succes, message = self.service_salle.modifier_salle(salle)
            if succes:
                messagebox.showinfo("Succès", message)
                self.vider_champs()
                self.lister_salles()
            else:
                messagebox.showerror("Erreur", message)

        except ValueError:
            messagebox.showerror("Erreur", "La capacité doit être un nombre entier")

    def supprimer_salle(self):
        code = self.entry_code.get()
        if not code:
            messagebox.showerror("Erreur", "Entrez le code de la salle")
            return

        self.service_salle.supprimer_salle(code)
        messagebox.showinfo("Succès", "Salle supprimée")
        self.vider_champs()
        self.lister_salles()

    def rechercher_salle(self):
        code = self.entry_code.get()
        if not code:
            messagebox.showerror("Erreur", "Entrez le code de la salle")
            return

        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entry_description.delete(0, "end")
            self.entry_categorie.delete(0, "end")
            self.entry_capacite.delete(0, "end")

            self.entry_description.insert(0, salle.description)
            self.entry_categorie.insert(0, salle.categorie)
            self.entry_capacite.insert(0, salle.capacite)
        else:
            messagebox.showerror("Erreur", "Salle introuvable")

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))
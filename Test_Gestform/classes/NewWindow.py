import tkinter as tk
from tkinter import messagebox
import pandas as pd
from Test_Gestform.functions.functions import checkFileExistance

rules = '''
    Soit une liste aléatoire de nombres entiers compris entre -1000 et 1000.
    Pour chaque nombre n de la liste on veut effectuer les opérations suivantes :
    - Si le nombre est divisible par 3 : on affiche Geste
    - Si le nombre est divisible par 5 : on affiche Forme
    - Si le nombre est divisible par 3 et par 5  : on affiche Gestform
    - Sinon : on affiche n
    '''

class NewWindow(tk.Tk):
    list = []
    def __init__(self, width, height):
        super().__init__()

        self['bg'] = '#e6ffff'
        self.title('Test Gestform')

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)
        self.geometry(f'{width}x{height}+{center_x}+{center_y}')
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=620, height=120, background='pink').grid(row=6, column=2, pady=20)

        tk.Label(self,
                 text="TEST D'ENTRETIENT GESTFORM",
                 font='Corbel 25',
                 relief="ridge",
                 borderwidth=5,
                 pady=15
                 ).grid(row=1, column=2, ipadx=90, ipady=10, pady=20)



        tk.Button(self,
                  text="Comment ça marche ?",
                  font='Corbel 10',
                  relief="ridge",
                  borderwidth=5,
                  width=17,
                  background='yellow',
                  command=self.need_help).place(x=10,y=550)

    def export_buton(self):
        tk.Button(self,
                  text="Exporter",
                  font='Corbel 10',
                  relief="ridge",
                  borderwidth=5,
                  width=15,
                  background='red',
                  command=self.exportation).place(x=760, y=550)

    def getList(self, L):
        self.L = L

    def exportation(self):
        if self.question_export() == True:
            dict = {'Valeur': self.L.L, 'Affichage': self.L.L_string}
            df = pd.DataFrame(dict)

            find = False
            cpt = 1
            s= ""
            while(not find) :
                s = "file" + str(cpt) + ".csv"
                if checkFileExistance(s):
                    cpt +=1
                else:
                    find = True
            df.to_csv(s)

    def need_help(self):
        messagebox.showinfo("Aide", rules)

    def question_export(self):
        return messagebox.askyesno("Exportation", "Est-vous sûre de vouloir\nexporter ce résultat")

    def warning_out_of_range(self):
        messagebox.showwarning("Attention", "Attention, le nombre saisi dépasse les bornes fixées\nSaisissez une nombre entre 1 et 9999")

    def warning_empty(self):
        messagebox.showwarning("Attention", "Attention, la saisie est vide\nSaisissez une nombre entre 1 et 9999")

    def warning_not_numeric(self):
        messagebox.showwarning("Attention", "Attention, la saisie n'est pas un nombre entier\nSaisissez un nombre entre 1 et 9999")

    def createCanvas(self):
        self.canvas = tk.Canvas(self, width=620, height=120, relief="ridge",borderwidth=5).grid(row=6, column=2, pady=20)



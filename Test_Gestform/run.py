import tkinter as tk
from Test_Gestform.classes.List import List
from Test_Gestform.classes.NewWindow import NewWindow

#Creation of the window
width = 900
height = 600
w1 = NewWindow(width, height)

#initialize the list with default constructor
list = List()

#text1 choose random int
texte1 = '''
Saisir un nombre entier entre 0 et 9999
Il déterminera le nombre d'éléments aléatoires
de la liste
'''
#text2 navigate into list
texte2 = '''
Appuyer sur suivant et précédent
Afin de naviguer dans la liste
'''

text_label = tk.Label(w1,text=texte1,font='Corbel 10',borderwidth=2)
text_label.grid(row=3, column=2)
#Entry zone where the number n is entered
entry1 = tk.Entry(w1, width=30)
entry1.grid(row=4, column=2)

#validation button of the input number
def button_command():
    text = entry1.get()
    if text =="":
        w1.warning_empty()
    elif not text.isnumeric():
        w1.warning_not_numeric()
    elif int(text)<1 or int(text)>9999 :
        w1.warning_out_of_range()
    else:
        text_label.configure(text=texte2)
        w1.export_buton()
        w1.getList(list)
        list.init_list(int(text))
        list.printList(canvas, (150, 15), 100)
        generate_button.destroy()
        entry1.destroy()

#Generate the list
generate_button =tk.Button(w1, height=1, width=10, text="Générer", command=button_command)
generate_button.grid(row=5, column=2)

#Canvas
canvas = tk.Canvas(w1, width=620, height=120, relief="ridge",borderwidth=5)
canvas.grid(row=6, column=2, pady=20)

#result print
print_label = tk.Label(w1, background='white',text=list.string,font="Corbel 25", width=10)
print_label.grid(row=7, column=2, pady=20, ipady=10)



#navigate in list to the end
def clear_and_forward():
    if list.n != 0:
        canvas.destroy()
        print_label.destroy()
        new_canvas = tk.Canvas(w1, width=620, height=120, relief="ridge",borderwidth=5)
        new_canvas.grid(row=6, column=2, pady=20)
        list.navigate_forward(new_canvas)
        new_print_label = tk.Label(w1, background='white', text=list.string, font="Corbel 25", width=10) \
            .grid(row=7, column=2, pady=20, ipady=10)


#navigate in list in direction of the begening
def clear_and_backward():
    if list.n != 0:
        canvas.destroy()
        print_label.destroy()
        new_canvas = tk.Canvas(w1, width=620, height=120, relief="ridge",borderwidth=5)
        new_canvas.grid(row=6, column=2, pady=20)
        list.navigate_backward(new_canvas)
        new_print_label = tk.Label(w1, background='white', text=list.string, font="Corbel 25", width=10) \
            .grid(row=7, column=2, pady=20, ipady=10)

#event button backward
navigation_button1 = tk.Button(w1, height=1, width=10, text="Précédent", command=clear_and_backward, padx=25)
navigation_button1.grid(row=6, column=1)

#event button foreward
navigation_button2 = tk.Button(w1, height=1, width=10, text="Suivant", command=clear_and_forward, padx=25)
navigation_button2.grid(row=6, column=3)






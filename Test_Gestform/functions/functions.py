import tkinter as tk
from random import randrange as rand
import csv


def randomList(n):
    L = []
    for i in range(n):
        L.append(rand(-1000, 1000, 1))
    return L


def is_3_mult(n):
    return n % 3 == 0


def is_5_mult(n):
    return n % 5 == 0


def check_file_existance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False


def export_file(list):
    find = False
    cpt = 1
    s= ""
    while(not find) :
        s = "file" + str(cpt) + ".csv"
        if check_file_existance(s):
            cpt +=1
        else:
            find = True
    with open(s, 'w', encoding='UTF8') as f:
        size_list = list.n
        writer = csv.writer(f)
        writer.writerow(["Valeur","Affichage"])
        for i in range(size_list):
            writer.writerow([i, str(list.L[i]), list.L_string[i]])






        
            




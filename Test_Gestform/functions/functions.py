# -*- coding: utf-8 -*-
import tkinter as tk
from random import randrange as rand


def randomList(n):
    L = []
    for i in range(n):
        L.append(rand(-1000, 1000, 1))
    return L


def is_3_mult(n):
    return n % 3 == 0


def is_5_mult(n):
    return n % 5 == 0


def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False


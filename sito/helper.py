# coding=utf-8
from datetime import *


# da che data a che data si visualizzerà l'inverno Da FEBBRAIO A FINE AGOSTO
# da che data a che data si visualizzerà l'estate DA SETTEMBRE A FINE GENNAIO

def get_stagione(inizio, fine):
    oggi = datetime.now().date()
    if inizio < oggi < fine:
        return "INVERNO"
    else:
        return "ESTATE"
    
    
'''
inizio = date(2017, 02, 01)
fine = date(2017, 8, 30)
stagione = get_stagione(inizio, fine)
print stagione
'''

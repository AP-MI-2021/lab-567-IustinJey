from random import randrange
from Logic.CRUD import adauga_rezervare, getById

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def rezervare_random(lista):
    lista_nume = ["Hociung Iustin", "Neamtu Daniel", "Ionescu Vlad", "Morarescu Cristina", "Ion Creanga", "Lucian Blaga" ,"Michael Jackson"]
    lista_clase = ["Economy", "Economy Plus", "Business"]
    lista_checked = ["Da", "Nu"]
    pret = randrange(600,900)

    id = 1
    while getById(id,lista) is not None:
        id = id + 1
    return adauga_rezervare(id, lista_nume[randrange(0,7)], lista_clase[randrange(0,3)], pret, lista_checked[randrange(0,2)], lista)
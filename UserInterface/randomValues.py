from random import randrange
from Logic.CRUD import adauga_rezervare, getById
def rezervare_random(lista):
    lista_nume = ["Hociung Iustin", "Neamtu Daniel", "Ionescu Vlad", "Morarescu Cristina", "Ion Creanga", "Lucian Blaga" ,"Michael Jackson"]
    lista_clase = ["Economy", "Economy Plus", "Business"]
    lista_checked = ["Da", "Nu"]
    pret = randrange(600,900)

    id = 1
    while getById(id,lista) is not None:
        id = id + 1

    print(" ")
    print("  Rezervare generata cu succes!  ")
    print(" ")

    return adauga_rezervare(id, lista_nume[randrange(0,7)], lista_clase[randrange(0,3)], pret, lista_checked[randrange(0,2)], lista)
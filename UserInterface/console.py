import sys
from time import sleep
from random import randrange
from Domain.rezervare import getChecked, getClasa, getId, getNume, getPret, toString
from Logic.CRUD import adauga_rezervare, getById, modificaRezervare, sterge_rezervare
from Logic.functionalitati import ieftinireRezervare, modificaClasa, pretMaximPerClasa, sortareDescrescatoarePret, sumaPretNume
from UserInterface.randomValues import rezervare_random

class bcolors:
    RED     = '\033[31m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ENTER_ADD():
    print(" ")
    input("Apasati " + bcolors.OKCYAN + "ENTER " + bcolors.ENDC + "pentru a continua: ")
    print(" ")


def submenuChecked():
    """submenuChecked submeniul checkin-urilor

    Returns:
        string: valoarea vaiabilei checked 
    """

    print(" ")
    print(bcolors.WARNING + "    (1)" + bcolors.ENDC + " Da")
    print(bcolors.WARNING + "    (2)" + bcolors.ENDC + " Nu")
    print(" ")
    
    optiune = int(input("Checkin facut? : "))

    if optiune == 1:
        return "Da"
    elif optiune == 2:
        return "Nu"
    else:
        print(bcolors.WARNING + "Aceasta actiune nu exista, incercati din nou" + bcolors.ENDC )
        ENTER_ADD()
    submenuChecked()




def submenuClasa():
    """submenuClasa submeniul claselor

    Returns:
        list: noua lista
    """

    print(" ")
    print(bcolors.WARNING + "    (1)" + bcolors.ENDC + " Economy")
    print(bcolors.WARNING + "    (2)" + bcolors.ENDC + " Economy Plus")
    print(bcolors.WARNING + "    (3)" + bcolors.ENDC + " Business")
    print(" ") 

    optiune = int(input("Alegeti clasa pe care o doriti: "))
    if optiune == 1:
        return "Economy"
    elif optiune == 2:
        return "Economy Plus"
    elif optiune == 3:
        return "Business"
    else:
        print(bcolors.WARNING + "Aceasta optiune nu exista, incercati din nou!" + bcolors.ENDC )
        ENTER_ADD()
    submenuClasa()



def submenuCRUD(lista, undoOperations, redoOperations):

    """menuCRUD afiseaza meniul CRUD
    """

    print(" ")
    print(bcolors.WARNING + "    (1.1)" + bcolors.ENDC + " Adaugare rezervare")
    print(bcolors.WARNING + "    (1.2)" + bcolors.ENDC + " Stergere rezervare")
    print(bcolors.WARNING + "    (1.3)" + bcolors.ENDC + " Modificare rezervare")
    print(bcolors.WARNING + "    (x)" + bcolors.ENDC + "   Inapoi")
    print(" ")

    optiune = input("Alegeti optiunea pe care o doriti " + bcolors.OKBLUE + "[1-3]: " + bcolors.ENDC )
    
    if optiune == '1':
        try:
            id = int(input("Introduceti id-ul: "))
            nume = input("Introduceti NUME_PRENUME: ")
            clasa = submenuClasa()
            pret = float(input("Introduceti pretul: "))
            checked = submenuChecked()
            rezultat = adauga_rezervare(id, nume, clasa, pret, checked, lista)
            undoOperations.append(
                [lambda : sterge_rezervare(id,rezultat),
                 lambda : adauga_rezervare(id, nume, clasa, pret, checked, lista)])
        except ValueError as ve:
            print("Error: {}".format(ve))
            return lista
        print(" ")
        print(bcolors.OKGREEN + "   Rezervare adaugata cu succes!   " + bcolors.ENDC)
        ENTER_ADD()
        return rezultat


    if optiune == '2':
        try:
            id = int(input("Introdu id-ul rezervarii ce doresti a fi stearsa: "))
            rezultat = sterge_rezervare(id, lista)
            rezervareDeSters = getById(id, lista) 
            undoOperations.append([lambda : adauga_rezervare(getId(rezervareDeSters),getNume(rezervareDeSters),\
                 getClasa(rezervareDeSters), getPret(rezervareDeSters), getChecked(rezervareDeSters), rezultat),
                                   lambda : sterge_rezervare(id, lista)])
        except ValueError as ve:
            print("Error: {}".format(ve))
            return lista
        print(" ")
        print(bcolors.RED + "X   Rezervare stearsa cu succes!   X" + bcolors.ENDC )
        ENTER_ADD()
        return rezultat
        
    
    if optiune == '3':
        try:
            id = int(input("Introdu id-ul rezervarii ce doresti a fi modificata: "))
            nume = input("Noul nume [NUME_PRENUME]: ")
            clasa = submenuClasa()
            pret = float(input("Introduceti noul pret: "))
            checked = submenuChecked()
            rezultat = modificaRezervare(id, nume, clasa, pret, checked, lista)
            rezervareVeche = getById(id, lista)
            undoOperations.append([lambda : modificaRezervare(id, getNume(rezervareVeche),\
                 getClasa(rezervareVeche), getPret(rezervareVeche), getChecked(rezervareVeche),rezultat),
                                   lambda : modificaRezervare(id, nume, clasa, pret, checked,lista)])
        except ValueError as ve:
            print("Error:".format(ve))
            return lista

        print(" ")
        print(bcolors.OKGREEN + "   Rezervare modificata cu succes!   " + bcolors.ENDC )
        ENTER_ADD()
        return rezultat
    
    if optiune == 'x':
        return lista
        
             
def TrecereaLaClasaSuperioara(lista):
    try:
        nume = input("Introduceti numele pe a caror rezervari doriti sa treceti la o clasa superioara: ")
    except ValueError as ve:
        print("Error: {}".format(ve))
    for x in lista:
        if nume in getNume(x):
            clasa_noua = submenuClasa()
            listaNoua = []
            listaNoua = modificaClasa(lista, nume, clasa_noua)
            print(" ")
            print(bcolors.OKGREEN + "    Modificare realizata cu succes" + bcolors.ENDC )
            ENTER_ADD()
            return listaNoua
    print(" ")
    print(bcolors.WARNING + "   Numele introdus nu exista in baza noastra de date, incercati din nou." + bcolors.ENDC)
    ENTER_ADD()
    return lista


def uiIeftinirePret(lista):
    try:
        procent = int(input("Introduceti procentul cu care doriti sa ieftiniti rezervarile cu checkin: " ))
    except ValueError as ve:
        print("Error: {}".format(ve))
    listaNoua = ieftinireRezervare(lista, procent)
    
    print(" ")
    print(bcolors.OKGREEN + "Toate rezervarile cu checkin au fost ieftinite cu " + bcolors.ENDC + str(procent)+"%")
    ENTER_ADD()
    return listaNoua


def uiClasaPretMaxim(lista):
    print(" ")
    for x in range(1, 1000):
        progress(x, 999, 1)
    print(" ")
    print(" ")
    print( bcolors.HEADER + "      PRETURI MAXIME" + bcolors.ENDC )
    print(" ")
    print(bcolors.OKCYAN + "Economy " + bcolors.ENDC + ": " + str(pretMaximPerClasa("Economy", lista)))
    print(bcolors.OKCYAN + "Economy Plus " + bcolors.ENDC + ": " + str(pretMaximPerClasa("Economy Plus", lista)))
    print(bcolors.OKCYAN + "Business " + bcolors.ENDC + ": " + str(pretMaximPerClasa("Business", lista)))
    ENTER_ADD()

def uiSortareDupaPret(lista):
    print(" ")
    for x in range(1, 1001):
        progress(x, 1000, 1)
    print(" ")
    print(" ")
    print(bcolors.OKGREEN + "Lista a fost sortata cu succes!" + bcolors.ENDC + " Introduceti optiunea "+ bcolors.WARNING +"<8>"+bcolors.ENDC+" pentru a o vizualiza")
    ENTER_ADD()
    return sortareDescrescatoarePret(lista)
    
def uisumaPretNume(lista):
    preturiSuma = sumaPretNume(lista)
    print(" ")
    print(bcolors.HEADER + "     LISTA SUMELOR PRETURILOR IN FUNCTIE DE NUME" + bcolors.ENDC)
    print(" ")
    for nume in preturiSuma:
        print(f"{bcolors.OKCYAN + nume:<30} { bcolors.ENDC + ' suma totala : ':<4} {bcolors.OKCYAN + str(preturiSuma[nume]) + bcolors.ENDC}")
    ENTER_ADD()

    return None



def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    if (100.0 * count / float(total)) < 40:
        bar = (bcolors.RED + '█' + bcolors.ENDC) * filled_len + '-' * (bar_len - filled_len)
    elif (100.0 * count / float(total)) < 80:
        bar = (bcolors.WARNING + '█' + bcolors.ENDC) * filled_len + '-' * (bar_len - filled_len)
    elif (100.0 * count / float(total)) < 101:
        bar = (bcolors.OKGREEN + '█' + bcolors.ENDC) * filled_len + '-' * (bar_len - filled_len)
    if (100.0 * count / float(total)) < 100:
        sys.stdout.write('[%s] %s%s | %s\r' % (bar, percents, '%', 'Please wait...'))
    else:
        sys.stdout.write('[%s] %s%s | %s\r' % (bar, percents, '%', bcolors.OKGREEN +'Completed       ' + bcolors.ENDC ))

    sys.stdout.flush()


def uiUndo(lista,undoOperations, redoOperations):
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        print("Nu se poate face Undo!")
    return lista

    
def uiRedo(lista,undoOperations, redoOperations):
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        print("Nu se poate face redo!")
    return lista


def printMenu():
    """printMenu afiseaza meniul principal
    """

    print(" ")
    print(bcolors.HEADER + "            MENIU PRINCIPAL" + bcolors.ENDC)
    print(" ")
    print(bcolors.WARNING + "    (1)" + bcolors.ENDC + " Adăugare / ștergere / modificare rezervare")
    print(bcolors.WARNING + "    (2)" + bcolors.ENDC + " Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.")
    print(bcolors.WARNING + "    (3)" + bcolors.ENDC + " Ieftineste toate rezervările la care s-a făcut checkin cu un procentaj citit.")
    print(bcolors.WARNING + "    (4)" + bcolors.ENDC + " Determinarea prețului maxim pentru fiecare clasă.")
    print(bcolors.WARNING + "    (5)" + bcolors.ENDC + " Ordonarea rezervărilor descrescător după preț.")
    print(bcolors.WARNING + "    (6)" + bcolors.ENDC + " Afișarea sumelor prețurilor pentru fiecare nume.")
    print(bcolors.WARNING + "    (u)" + bcolors.ENDC + " Undo.")
    print(bcolors.WARNING + "    (r)" + bcolors.ENDC + " Redo.")
    print(bcolors.WARNING + "    (a)" + bcolors.ENDC + " Afiseaza toate rezervarile.")
    print(bcolors.WARNING + "    (x)" + bcolors.ENDC + " Iesire")
    print(bcolors.WARNING + "    (99)" + bcolors.ENDC + " Generare rezervare aleatorie.")
    print(" ")

def runMenu(lista):
    undoOperations = []
    redoOperations = []
    while True:
        printMenu()
        optiune = input(bcolors.OKCYAN + "Alegeti optiunea pe care o doriti: " + bcolors.ENDC)


        if optiune == "1":
            lista = submenuCRUD(lista, undoOperations, redoOperations) 
        elif optiune == "2":
            lista = TrecereaLaClasaSuperioara(lista)
        elif optiune == "3":
            lista = uiIeftinirePret(lista)
        elif optiune == '4':
            uiClasaPretMaxim(lista)
        elif optiune == '5':
            lista = uiSortareDupaPret(lista)
        elif optiune == '6':
            lista = uisumaPretNume(lista)
        elif optiune == 'u':
            lista = uiUndo(lista,undoOperations, redoOperations)
        elif optiune == 'r':
            lista = uiRedo(lista,undoOperations, redoOperations)
        elif optiune == "a":
            if len(lista) == 0:
                print(" ")
                print(bcolors.RED + " !!! Nu exista rezervari disponibile. !!!" + bcolors.ENDC)
                ENTER_ADD()
            else:
                print(" ")
                print(bcolors.HEADER + "  -- LISTA TUTUROR REZERVARILOR -- " + bcolors.ENDC )
                print(" ")
                for rezervare in lista:
                    print(toString(rezervare))
                ENTER_ADD()
        elif optiune == "x":
            break
        elif optiune == "99":
            print(" ")
            nr = int(input("Introduceti numarul rezervarilor ce doriti a fi generate: "))
            print(" ")
            for x in range(nr):
                progress(x, nr-1, 1)
                lista = rezervare_random(lista)
            print(" ")
            if nr == 1:
                print(" ")
                print(bcolors.OKGREEN + "  Rezervare generata cu succes!  " + bcolors.ENDC )
                print(" ")
                ENTER_ADD()
            elif nr == 0:
                print(" ")
                print(bcolors.WARNING + "  Introduceti un numar mai mare decat zero!  " + bcolors.ENDC )
                print(" ")
                ENTER_ADD()
            else:
                print(" ")
                print(bcolors.OKGREEN + "  Toate cele " + bcolors.ENDC + str(nr) +bcolors.OKGREEN + " de rezervari au fost generate cu succes!" + bcolors.ENDC)
                ENTER_ADD()
        else:
            print(" ")
            print(bcolors.WARNING + "Aceasta optiune este momentan indisponibila, incercati una diferita!" + bcolors.ENDC)
            print(" ")
            ENTER_ADD()

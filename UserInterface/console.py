
from Domain.rezervare import getNume, toString
from Logic.CRUD import adauga_rezervare, modificaRezervare, sterge_rezervare
from Logic.functionalitati import ieftinireRezervare, modificaClasa
from UserInterface.randomValues import rezervare_random

def submenuChecked():
    """submenuChecked submeniul checkin-urilor

    Returns:
        string: valoarea vaiabilei checked 
    """

    print(" ")
    print("    (1) Da")
    print("    (2) Nu")
    print(" ")
    
    optiune = int(input("Checkin facut? : "))

    if optiune == 1:
        return "Da"
    elif optiune == 2:
        return "Nu"
    else:
        print("Aceasta actiune nu exista, incercati din nou")
        input("Apasati ENTER pentru a continua: ")
    submenuChecked()




def submenuClasa():
    """submenuClasa submeniul claselor

    Returns:
        list: noua lista
    """

    print(" ")
    print("    (1) Economy")
    print("    (2) Economy Plus")
    print("    (3) Business")
    print(" ") 

    optiune = int(input("Alegeti clasa pe care o doriti: "))
    if optiune == 1:
        return "Economy"
    elif optiune == 2:
        return "Economy Plus"
    elif optiune == 3:
        return "Business"
    else:
        print("Aceasta optiune nu exista, incercati din nou!")
        input("Apasati ENTER pentru a continua: ")
    submenuClasa()



def submenuCRUD(lista):

    """menuCRUD afiseaza meniul CRUD
    """

    print(" ")
    print("    (1.1) Adaugare rezervare")
    print("    (1.2) Stergere rezervare")
    print("    (1.3) Modificare rezervare")
    print("    (x) Inapoi")
    print(" ")

    optiune = int(input("Alegeti optiunea pe care o doriti [1-3]: "))
    
    if optiune == 1:
        try:
            id = int(input("Introduceti id-ul: "))
            nume = input("Introduceti NUME_PRENUME: ")
            clasa = submenuClasa()
            pret = float(input("Introduceti pretul: "))
            checked = submenuChecked()
        except ValueError as ve:
            print("Error: {}".format(ve))

        print(" ")
        print("   Rezervare adaugata cu succes!   ")
        print(" ")
        input("Apasati ENTER pentru a continua: ")
        return adauga_rezervare(id, nume, clasa, pret, checked, lista)


    if optiune == 2:
        try:
            id = int(input("Introdu id-ul rezervarii ce doresti a fi stearsa: "))
        except ValueError as ve:
            print("Error: {}".format(ve))
        print(" ")
        print("   Rezervare stearsa cu succes!   ")
        print(" ")
        input("Apasati ENTER pentru a continua: ")
        return sterge_rezervare(id, lista)
        
    
    if optiune == 3:
        try:
            id = int(input("Introdu id-ul rezervarii ce doresti a fi modificata: "))
            nume = input("Noul nume [NUME_PRENUME]: ")
            clasa = submenuClasa()
            pret = float(input("Introduceti noul pret: "))
            checked = submenuChecked()
        except ValueError as ve:
            print("Error:".format(ve))
            
        print(" ")
        print("   Rezervare modificata cu succes!   ")
        print(" ")
        input("Apasati ENTER pentru a continua: ")
        return modificaRezervare(id, nume, clasa, pret, checked, lista)
        
             
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
            print("    Modificare realizata cu succes")
            input(print(" Apasati ENTER pentru a continua: "))
            print(" ")
            return listaNoua
    print(" ")
    print("   Numele introdus nu exista in baza noastra de date, incercati din nou.")
    print(" ")
    input("Apasati ENTER pentru a continua: ")
    print(" ")
    return lista


def uiIeftinirePret(lista):
    try:
        procent = int(input("Introduceti procentul cu care doriti sa ieftiniti rezervarile cu checkin: " ))
    except ValueError as ve:
        print("Error: {}".format(ve))
    listaNoua = ieftinireRezervare(lista, procent)
    print(" ")
    print("Toate rezervarile cu checkin au fost ieftinite cu "+str(procent)+"%")
    print(" ")
    input("Apasati ENTER pentru a continua: ")
    return listaNoua

def printMenu():
    """printMenu afiseaza meniul principal
    """

    print(" ")
    print("    (1) Adăugare / ștergere / modificare rezervare")
    print("    (2) Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.")
    print("    (3) Ieftineste toate rezervările la care s-a făcut checkin cu un procentaj citit.")
    print("    (4) [INDISPONIBIL] Determina prețului maxim pentru fiecare clasă.")
    print("    (5) [INDISPONIBIL] Ordonarea rezervărilor descrescător după preț.")
    print("    (6) [INDISPONIBIL] Afișarea sumelor prețurilor pentru fiecare nume.")
    print("    (7) [INDISPONIBIL] Undo.")
    print("    (8) Afiseaza toate rezervarile.")
    print("    (x) Iesire")
    print("    (99) Generare rezervare aleatorie.")
    print(" ")

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Alegeti optiunea pe care o doriti: ")


        if optiune == "1":
            lista = submenuCRUD(lista) 
        if optiune == "2":
            lista = TrecereaLaClasaSuperioara(lista)
        if optiune == "3":
            lista = uiIeftinirePret(lista)
        elif optiune == "8":
            if len(lista) == 0:
                print(" !!! Nu exista rezervari disponibile. !!!")
            else:
                print(" ")
                print("  -- LISTA TUTUROR REZERVARILOR -- ")
                print(" ")
                for rezervare in lista:
                    print(toString(rezervare))
                print("     ")
                input("Apasati ENTER pentru a continua: ")
        elif optiune == "x":
            break
        elif optiune == "99":
            lista = rezervare_random(lista)
            input("Apasati ENTER pentru a continua: ")    
        else:
            print(" ")
            print("Aceasta optiune este momentan indisponibila, incercati una diferita!")
            print(" ")

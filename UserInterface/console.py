
from Domain.rezervare import toString
from Logic.CRUD import adauga_rezervare, modificaRezervare, sterge_rezervare

def submenuChecked():
    """submenuChecked submeniul checkin-urilor

    Returns:
        string: valoarea vaiabilei checked 
    """

    print("1.Da")
    print("2.Nu")
    
    optiune = int(input("Alege optiunea pe care o doriti: "))

    if optiune == 1:
        return "Da"
    elif optiune == 2:
        return "Nu"
    else:
        print("Aceasta actiune nu exista, incercati din nou")
    submenuChecked()




def submenuClasa():
    """submenuClasa submeniul claselor

    Returns:
        list: noua lista
    """


    print("1.Economy")
    print("2.Economy Plus")
    print("3.Business")

    optiune = int(input("Alegeti clasa pe care o doriti: "))
    if optiune == 1:
        return "Economy"
    elif optiune == 2:
        return "Economy Plus"
    elif optiune == 3:
        return "Business"
    else:
        print("Aceasta optiune nu exista, incercati din nou!")
    submenuClasa()



def submenuCRUD(lista):
    """menuCRUD afiseaza meniul CRUD
    """
    print("1.1 Adaugare rezervare")
    print("1.2 Stergere rezervare")
    print("1.3 Modificare rezervare")
    print("x.Inapoi")
    
    optiune = int(input("Alegeti optiunea pe care o doriti [1-3]: "))
    
    if optiune == 1:
        id = int(input("Introduceti id-ul: "))
        nume = input("Introduceti NUME_PRENUME: ")
        clasa = submenuClasa()
        pret = float(input("Inreoduceti pretul: "))
        checked = submenuChecked()
        return adauga_rezervare(id, nume, clasa, pret, checked, lista)


    if optiune == 2:
        id = int(input("Introdu id-ul rezervarii ce doresti a fi stearsa: "))
        return sterge_rezervare(id, lista)

    
    if optiune == 3:
        id = int(input("Introdu id-ul rezervarii ce doresti a fi modificata: "))
        nume = input("Noul nume [NUME_PRENUME]: ")
        clasa = submenuClasa()
        pret = float(input("Introduceti noul pret: "))
        checked = submenuChecked()
        return modificaRezervare(id, nume, clasa, pret, checked, lista)
        
        
        





def printMenu():
    """printMenu afiseaza meniul principal
    """
    print("1.Adăugare / ștergere / modificare rezervare")
    print("2.Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.")
    print("3.Ieftineste toate rezervările la care s-a făcut checkin cu un procentaj citit.")
    print("4.Determina prețului maxim pentru fiecare clasă.")
    print("5.Ordonarea rezervărilor descrescător după preț.")
    print("6.Afișarea sumelor prețurilor pentru fiecare nume.")
    print("7.Undo.")
    print("8.   Afisare rezervari    ")
    print("x.Iesire")

def runMenu(lista):
    while True:
        printMenu()
        optiune = int(input("Alegeti optiunea pe care o doriti: "))
        if optiune == 1:
            lista = submenuCRUD(lista)
        
        if optiune == 8:
            if len(lista) == 0:
                print("Nu exista rezervari disponibile.")
            else:
                for rezervare in lista:
                    print(toString(rezervare))

        
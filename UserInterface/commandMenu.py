from Domain.rezervare import toString
from Logic.CRUD import adauga_rezervare, modificaRezervare, sterge_rezervare
from UserInterface.randomValues import rezervare_random

def help():
    """help afiseaza lista cu toate comenzile
    """
    print(" ")
    print("  Scrieti comenzile despartite cu ;, iar parametrii despartiti cu ,")
    print("    Add - adauga o rezervare in lista [ex. (Add,id,Nume,Clasa,Pret,Checkin)")
    print("    Delete - sterge o rezervare din lista [ex. (Delete,id)")
    print("    Update - modifica o rezervare fin lista [ex. (Update,id,Nume,Clasa,Pret,Checkin)")
    print("    Show all - afiseaza toate rezervarile din lista [ex. (Show all)")
    print("    Random - genereaza o rezervare aleatorie [ex. (Random)")
    print(" ")
    input("Apasati ENTER pentru a continua: ")

def runCommandMenu(lista):

    while True:
        print(" ")
        print("    Inserati comanda Help, pentru a afisa lista cu toate comenzile")
        print(" ")
        commandLine = input("Introduceti comanda: ")
        commandPerFunctions = commandLine.split(";")

        for comanda in commandPerFunctions:
            commandPerParam = comanda.split(",")
            if commandPerParam[0] == "Add":
                lista = adauga_rezervare(
                    int(commandPerParam[1]),
                    commandPerParam[2],
                    commandPerParam[3],
                    float(commandPerParam[4]),
                    commandPerParam[5],
                    lista)
            elif commandPerParam[0] == "Delete":
                lista = sterge_rezervare(commandPerParam[1], lista)
            elif commandPerParam[0] == "Update":
                lista = modificaRezervare( int(commandPerParam[1]),
                    commandPerParam[2],
                    commandPerParam[3],
                    float(commandPerParam[4]),
                    commandPerParam[5],
                    lista)
            elif commandPerParam[0] == "Exit":
                break
            elif commandPerParam[0] == "Show all":
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
            elif commandPerParam[0] == "Random":
                lista = rezervare_random(lista)
                input("Apasati ENTER pentru a continua: ")
            elif commandPerParam[0] == "Help":
                help()
            else:
                print(" ")
                print ("    Comanda introduse este invalida, incercati din nou.")
                print(" ")
                input("Apasati ENTER pentru a continua:")
                print(" ")
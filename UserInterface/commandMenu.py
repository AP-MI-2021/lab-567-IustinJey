from Domain.rezervare import toString
from Logic.CRUD import adauga_rezervare, modificaRezervare, sterge_rezervare
from UserInterface.randomValues import rezervare_random

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

def ENTER_ADD():
    print(" ")
    input("Apasati " + bcolors.OKCYAN + "ENTER " + bcolors.ENDC + "pentru a continua: ")
    print(" ")

def help():
    """help afiseaza lista cu toate comenzile
    """
    print(" ")
    print("    LISTA DE COMENZI")
    print(" ")
    print(f"{bcolors.OKGREEN +'        Add '+ bcolors.ENDC + '-> [id,Nume,Clasa,Pret,Checkin]':<70} {'-adauga o rezervare in lista'}")
    print(f"{bcolors.OKGREEN +'        Delete '+ bcolors.ENDC + '-> [id]':<70} {'-sterge o rezervare dupa id'}")
    print(f"{bcolors.OKGREEN +'        Update '+ bcolors.ENDC + '-> [id,Nume,Clasa,Pret,Checkin]':<70} {'-modifica o rezervare in lista'}")
    print(f"{bcolors.OKGREEN +'        Show all'+ bcolors.ENDC:<70} {'-afiseaza toate rezervarile'}")
    print(f"{bcolors.OKGREEN +'        Random '+ bcolors.ENDC:<70} {'-genereaza o rezervare aleatorie'}")
    ENTER_ADD()

def runCommandMenu(lista):

    while True:
        print(" ")
        print("    Inserati comanda Help, pentru a afisa lista cu toate comenzile")
        print(bcolors.WARNING +"    ATENTIE" + bcolors.ENDC + ": Introduceti functiile despartite prin <;> iar parametrii prin <,>)")
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
                ENTER_ADD()
            elif commandPerParam[0] == "Random":
                lista = rezervare_random(lista)
                ENTER_ADD()
            elif commandPerParam[0] == "Help":
                help()
            else:
                print(" ")
                print ("    Comanda introdusa este invalida, incercati din nou.")
                ENTER_ADD()
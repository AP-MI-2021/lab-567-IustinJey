from Domain.rezervare import creaza_rezervare, getId
from Tests.AllTests import runAllTests
from UserInterface.console import runMenu


def main():
    rezervare = creaza_rezervare(1, "Hociung Iustin", "Economy", 670, "Da")
    print(getId(rezervare))
    runAllTests()
    lista = []
    runMenu(lista)

if __name__ == "__main__":
    main()
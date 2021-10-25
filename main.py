from Tests.AllTests import runAllTests
from UserInterface.console import runMenu


def main():
    runAllTests()
    lista = []
    runMenu(lista)

if __name__ == "__main__":
    main()
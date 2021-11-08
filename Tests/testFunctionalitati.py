from Domain.rezervare import getPret
from Logic.CRUD import adauga_rezervare, getById
from Logic.functionalitati import ieftinireRezervare, pretMaximPerClasa, sortareDescrescatoarePret, sumaPretNume


def testIeftinireCuCheckin():
    lista = []
    lista = adauga_rezervare(1, "Acatrinei Amira", "Economy", 670, "Da",lista)
    lista = adauga_rezervare(2, "Hociung Iustin", "Economy" , 670, "Nu",lista)
    lista = ieftinireRezervare(lista, 100)

    assert getPret(getById(1,lista)) == 0
    assert getPret(getById(2,lista)) == 670

def testPretMaximPerClasa():
    lista = []
    lista = adauga_rezervare(1, "Acatrinei Amira", "Economy", 670, "Da",lista)
    lista = adauga_rezervare(2, "Hociung Iustin", "Economy Plus" , 800, "Nu",lista)
    rezultat1 = pretMaximPerClasa("Economy", lista)
    rezultat2 = pretMaximPerClasa("Economy Plus", lista)

    assert rezultat1 == 670
    assert rezultat2 == 800

def testSortareDescrescatoarePret():
    lista = []
    lista = adauga_rezervare(1, "Acatrinei Amira", "Economy", 670, "Da",lista)
    lista = adauga_rezervare(2, "Hociung Iustin", "Economy Plus" , 800, "Nu",lista)
    lista = sortareDescrescatoarePret(lista)

    assert getPret(lista[0]) == 800
    assert getPret(lista[1]) == 670

def testSumaPretNume():
    lista = []
    lista = adauga_rezervare(1, "Acatrinei Amira", "Economy", 670, "Da",lista)
    lista = adauga_rezervare(2, "Hociung Iustin", "Economy Plus" , 800, "Nu",lista)
    lista = adauga_rezervare(3, "Acatrinei Amira", "Economy", 670, "Da",lista)
    lista = adauga_rezervare(4, "Hociung Iustin", "Economy Plus" , 800, "Nu",lista)
    rezultat = sumaPretNume(lista)

    for nume in rezultat:
        if nume == "Acatrinei Amira":
            assert rezultat[nume] == 1340
        if nume == "Hociung Iustin":
            assert rezultat[nume] == 1600

from Logic.CRUD import adauga_rezervare, getById, modificaRezervare, sterge_rezervare
from Domain.rezervare import  getChecked,getPret,getClasa,getNume,getId


def testAdaugaRezervare():
    """testAdaugaRezervare testeaza functia de adauare a unei noi rezervari intr-o lista
    """
    lista = []
    lista = adauga_rezervare(1, "Hociung Iustin", "Economy", 670, "Da", lista)
    assert getId(lista[0]) == 1
    assert getNume(lista[0]) == "Hociung Iustin"
    assert getClasa(lista[0]) == "Economy"
    assert getPret(lista[0]) == 670
    assert getChecked(lista[0]) == "Da"


def testStergeRezervare():
    """testStergeRezervare testeaza functia de stergere a unei rezervari dintr-o lista
    """
    lista = []
    lista = adauga_rezervare(1, "Hociung Iustin", "Economy", 670, "Da",lista)
    lista = adauga_rezervare(2, "Acatrinei Amira", "Economy", 670, "Da",lista)

    lista = sterge_rezervare(1,lista)

    assert getById(1,lista) is None
    assert getById(2,lista) is not None
    

def testModificaRezervare():
    """testModificaRezervare tesetaza functia de modificare a unui parametru in lista
    """
    lista = []
    lista = adauga_rezervare(1, "Hociung Iustin", "Economy", 670, "Da",lista)

    lista = modificaRezervare(1, "JEY", "Economy Plus", 800, "Da", lista)

    assert getNume(getById(1,lista)) == "JEY"
    assert getClasa(getById(1,lista)) == "Economy Plus"
    assert getPret(getById(1, lista)) == 800
    assert getChecked(getById(1, lista)) == "Da"
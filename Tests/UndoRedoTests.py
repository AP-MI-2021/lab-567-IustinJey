from Domain.rezervare import getChecked, getClasa, getNume, getPret, toString
from Logic.CRUD import adauga_rezervare, getById, sterge_rezervare
from UserInterface.console import submenuCRUD, uiRedo, uiUndo


def TesteUndoRedo():
    lista = []
    undoOperations = []
    redoOperations = []

    lista1 = lista
    rezultat = adauga_rezervare(1,"Iustin", "Economy", 800, "Da", lista)
    undoOperations.append(
                [lambda : sterge_rezervare(1,rezultat),
                 lambda : adauga_rezervare(1,"Iustin", "Economy", 800, "Da", lista1)])

    
    lista = rezultat
    lista2 = lista
    rezultat = adauga_rezervare(2,"Iustin", "Economy", 800, "Da", lista)
    undoOperations.append(
                [lambda : sterge_rezervare(2,rezultat),
                 lambda : adauga_rezervare(2,"Iustin", "Economy", 800, "Da", lista2)])

    lista = rezultat
    lista3 = lista
    rezultat = adauga_rezervare(3,"Iustin", "Economy", 800, "Da", lista)
    undoOperations.append(
                [lambda : sterge_rezervare(3,rezultat),
                 lambda : adauga_rezervare(3,"Iustin", "Economy", 800, "Da", lista3)])

    lista = rezultat

 
    assert len(lista) == 3

    for x in lista:
        print(toString(x))
    print(" ")

    lista = uiUndo(lista, undoOperations, redoOperations)
    for x in lista:
        print(toString(x))
    print(" ")
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(2, lista) is not None
    assert getById(3, lista) is None

    lista = uiUndo(lista, undoOperations, redoOperations)
    for x in lista:
        print(toString(x))
    print(" ")
    assert len(lista) == 1
    assert getById(1, lista) is not None
    assert getById(2, lista) is None
    assert getById(3, lista) is None


    lista = uiUndo(lista, undoOperations, redoOperations)
    assert len(lista) == 0
    assert getById(1, lista) is None
    assert getById(2, lista) is None
    assert getById(3, lista) is None


    lista = uiUndo(lista, undoOperations, redoOperations)
    assert len(lista) == 0
    assert getById(1, lista) is None
    assert getById(2, lista) is None
    assert getById(3, lista) is None


    """    
    lista = adauga_rezervare(4,"Iustin", "Economy", 800, "Da", lista, undo_list, redo_list)

    lista = adauga_rezervare(5,"Iustin", "Economy", 800, "Da", lista, undo_list, redo_list)

    lista = adauga_rezervare(6,"Iustin", "Economy", 800, "Da", lista, undo_list, redo_list)

    assert len(lista) == 3


    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert getById(1, lista) is not None
    assert getById(2, lista) is not None
    assert getById(3, lista) is not None


    lista = uiUndo(lista, undo_list, redo_list)
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById(1, lista) is not None
    assert getById(2, lista) is None
    assert getById(3, lista) is None


    lista =uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(2, lista) is not None
    assert getById(3, lista) is None


    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert getById(1, lista) is not None
    assert getById(2, lista) is not None
    assert getById(3, lista) is not None


    lista = uiUndo(lista, undo_list, redo_list)
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById(1, lista) is not None
    assert getById(2, lista) is None
    assert getById(3, lista) is None


    lista = adauga_rezervare(7,"Iustin", "Economy", 800, "Da", lista, undo_list, redo_list)

    assert len(lista) == 2


    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(4, lista) is not None


    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById(1, lista) is not None
    assert getById(4, lista) is None


    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert getById(1, lista) is None
    assert getById(4, lista) is None


    lista = uiRedo(lista, undo_list, redo_list)
    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(2, lista) is None
    assert getById(3, lista) is None
    assert getById(4, lista) is not None


    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(2, lista) is None
    assert getById(3, lista) is None
    assert getById(4, lista) is not None   

    """
from Domain.rezervare import creaza_rezervare, getChecked, getClasa, getId, getNume, getPret


def modificaClasa(lista, substringName, stringClasa):
    """modificaClasa Modifica clasa tuturor rezervarilor pe un anumit nume, la una superioara

    Args:
        lista (list): Lista din care vom modifica rezervarile
        substringName (string): Numele a caror rezervari vor fi modificate
    Return:
        (list) : lista modificata
    """
    listaNoua = []
    for rezervare in lista:
        if substringName in getNume(rezervare):
            rezervareNoua = creaza_rezervare(
                getId(rezervare),
                getNume(rezervare),
                stringClasa,
                getPret(rezervare),
                getChecked(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    
    return listaNoua

def ieftinireRezervare(lista, procent):
    """ieftinireRezervare ieftineste toate rezervarile ce au checkin cu un procentaj anume

    Args:
        lista (list): lista folosita
        procent (int): procentul cu care se ieftinesc rezervarile
    Return: lista dupa ieftinire
    """
    listaNoua = []
    for rezervare in lista:
        if "Da" in getChecked(rezervare):
            rezervare_noua = creaza_rezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare) - (procent / 100) * getPret(rezervare),
                getChecked(rezervare)
            )
            listaNoua.append(rezervare_noua)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def pretMaximPerClasa(clasa, lista):
    """pretMaximPerClasa Calculeaza pretul o anume rezervare

    Args:
        clasa (string): Clasa utilizata in enunt
        lista (list): lista utilizata

    Returns:
        int: pretul maxim
    """
    pretMaxim = 0
    for rezervare in lista:
        if getClasa(rezervare) == clasa:
            if getPret(rezervare) > pretMaxim:
                pretMaxim = getPret(rezervare)
    return pretMaxim

def sortareDescrescatoarePret(lista):
    """sortareDescrescatoarePret sorteaza dupa parametrul pret lista 

    Args:
        lista (list): [lista folosita]
    Return:
        lista sortata
    """
    
    return sorted(lista, key = lambda rezervare: getPret(rezervare), reverse = True)


def sumaPretNume(lista):
    """sumaPretNume returneaza un dictionar cum suma preturilor pentru fiecare nume

    Args:
        lista (lista): lista utilizata

    Returns:
        dict: dictionarul cu cerinta din enunt
    """
    rezultat = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    
    return rezultat

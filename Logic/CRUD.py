from Domain.rezervare import creaza_rezervare, getId


def adauga_rezervare(id, nume, clasa, pret, checked,lista):
    """adauga_prajitura adauga o rezervare la lista curenta

    Args:
        id (int): id rezervare
        nume (string): NUmele pe acre s-a facut rezervarea
        clasa (string)): clasa rezervarii
        pret (float): pretul rezervarii
        checked (string): Verificarea rezervarii
        lista (list): lista curenta de rezervari
    Return: 
        lista curenta plus noua rezevare
    """
    rezervare_noua = creaza_rezervare(id, nume, clasa, pret, checked)
    return lista + [rezervare_noua]



def sterge_rezervare(id, lista):
    """sterge_rezervare sterge o rezervare dupa un id dat

    Args:
        id (int): id-ul dat
        lista (list): lista din care urmeaza a fi stearsa rezevarea cu id-ul dat
    Return:
        Lista curenta fara rezervare a carei id ii dat

    """
    return [rezervare for rezervare in lista if getId(rezervare) != id]


def getById(id, lista):
    """getById returneaza din lista rezervarea cu id-ul dat

    Args:
        id (int): id-ul rezervarii
        lista (list): lista rezervarilor
    """

    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None
    

def modificaRezervare(id, nume, clasa, pret, checked, lista):
    """modificaRezervare modifica o rezervare in lista dupa un id dat

    Args:
        id (int): id-ul rezervarii ce urmeaza a fi modificata
        nume (string): numele persoanei pe care rezervarea e facuta
        clasa (string): clasa rezervarii
        pret (float): pretul rezervarii
        checked (string): verifivcarea rezervarii
        lista (list): lista cu rezervarile ce urmeaza a fi modificata
    """
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creaza_rezervare(id, nume, clasa, pret, checked)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)

    return listaNoua

def creaza_rezervare(id, nume, clasa, pret, checked):
    """creaza_rezervare creaza o rezervare

    Args:
        id (int): id-ul rezerarii
        nume (string): numele persoanei pe care se face rezervarea
        clasa (string): clasa rezervarii
        pret (float): pretul rezervarii
        checked (string): checking facut(da/nu)
    Returns:
        Return: Un dictionar a unei rezervari

    """
    return [
        int(id),
        str(nume),
        str(clasa),
        float(pret),
        str(checked)
    ]




def getId(rezervare):
    """getId Returneaza Id-ul unei rezervari

    Args:
        rezervare (dictionar): dictionarul unei rezervari
    """
    return rezervare[0]





def getNume(rezervare):
    """getNume Returneaza numele pe care s-a facut o anume rezervare

    Args:
        rezervare(dictionar): dictionarul unei rezervari
    """
    return rezervare[1]




def getClasa(rezervare):
    """getClasa returneaza clasa rezervarii

    Args:
        rezervare (dictionar): dictionarul unei rezervari
    """
    return rezervare[2]




def getPret(rezervare):
    """getPret Returneaza pretul unei anume rezevari

    Args:
        rezeevare (dictionar): dictionarul unei rezervari
    """
    return rezervare[3]




def getChecked(rezervare):
    """getChecked Returneza daca o rezervare este checked

    Args:
        rezervare (dictionar): dictionarul unei rezervari`
    """
    return rezervare[4]



def toString(rezervare):
    """toString Returneza o lista cu toate elementele dintr-un dictionar

    Args:
        rezervare (dictionar): dictionarul unei rezervari
    """
    return "id: {} , nume: {}, clasa: {}, pret: {}, checked: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getChecked(rezervare)
    )

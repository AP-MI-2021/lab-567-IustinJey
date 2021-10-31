from Domain.rezervare import creaza_rezervare, getId, getChecked, getPret, getClasa, getNume


def test_rezervare():
    """test_rezervare testeza package-ul Domain
    """
    rezervare = creaza_rezervare(1, "Hociung Iustin", "Economy", 670, "Da")
    assert getId(rezervare) == 1
    assert getNume(rezervare) == "Hociung Iustin"
    assert getClasa(rezervare) == "Economy"
    assert getPret(rezervare) == 670
    assert getChecked(rezervare) == "Da"
    
    



from Logic.CRUD import modificaRezervare
from Tests.DomainTest import test_rezervare
from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare



def runAllTests():
    """Teste apeleaza toate testele
    """
    test_rezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()

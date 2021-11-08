from Logic.CRUD import modificaRezervare
from Tests.DomainTest import test_rezervare
from Tests.UndoRedoTests import TesteUndoRedo
from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare
from Tests.testFunctionalitati import *



def runAllTests():
    """Teste apeleaza toate testele
    """
    test_rezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testIeftinireCuCheckin()
    testPretMaximPerClasa()
    testSortareDescrescatoarePret()
    testSumaPretNume()
   # TesteUndoRedo()#

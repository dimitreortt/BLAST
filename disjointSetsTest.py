from disjointSets import doUnion
from disjointSetsUtils import *

testfamilies = {
  'uid1': ['uid2', 'uid4'],
  'uid2': ['uid3'],
  'uid3': ['uid2', 'uid4'],
  'uid4': ['uid1', 'uid3'],
  'uid5': ['uid6'],
  'uid6': ['uid5']
  }

def test1():
  # global testfamilies
  doUnion(testfamilies)
  showParentAndPiAB()

def test2():
  from families import createFamilies

  resultsFilename = 'Files/resultadoAllVsAll.txt'
  maxBsDictFilename = 'Files/maxBitscoresAllVsAll'

  families = createFamilies(resultsFilename, maxBsDictFilename)
  doUnion(families)
  # showParentAndPiAB()

  n = numberOfOrphansInOtherFamilies(families)
  print(numberOfOrphans(families), numberOfSetsOfSize1(), n)

  genomesNames = ['BuchAphi', 'Wglos', 'EscheColi', 'HaemoInfl', 'PasteMult', 'PseudAeru', 'SalmoEnte', 'VibriChol-I', 'VibriChol-II', 'XanthCamp', 'XanthCitr', 'XylelFast', 'YersiCO92', 'YersiKIM10+']

  doAssignment(genomesNames)

  print('Fim da criação de genomas finais.')

if __name__ == "__main__":
  test2()
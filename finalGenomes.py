from utils import removeExtension, addFilesPrefix
from read import readFileLines
from familiesUnion import doUnion, printFamilies, \
  findFamilyThatContainsUid

def removeGenomesNamesExtensions(genomesNames):
  return [removeExtension(name) for name in  genomesNames]

def readGenesUids(genomeName):
  genesUidsLines = readFileLines(genomeName + '.uids')
  return [uid.rstrip('\n') for uid in genesUidsLines]

uniqueInteger = 100000
def nextUniqueInteger():
  global uniqueInteger
  uniqueInteger += 1

  return uniqueInteger - 1

def getFamilyName(geneUid, unitedFamilies):
  response = findFamilyThatContainsUid(geneUid, unitedFamilies)
  if response:    
    uid, family = response
    return family.name

  # No family contains this uid, because it didn't have
  # a match inside blast's result file.
  return nextUniqueInteger()

def startFinalGenomeFile(genomeName):
  return open(genomeName + '.final')

def createFinalGenome(genomeName, unitedFamilies):
  genomeName = addFilesPrefix(genomeName)
  genesUids = readGenesUids(genomeName)  

  return [getFamilyName(geneUid, unitedFamilies) for geneUid in genesUids]  

def addFinalSuffix(filename):
  if '.final' not in filename:
    return filename + '.final'

  return filename

def writeFinalGenomeIntoFile(finalGenome, genomeName):
  genomeFileName = addFilesPrefix(genomeName)
  genomeFileName = addFinalSuffix(genomeFileName)

  gFile = open(genomeFileName, 'w')
  gFile.write('%r' % finalGenome)

# implementação ingênua, extremamente ineficiente
def createFinalFamilyAssignedGenomes(families, genomesNames):
  genomesNames = removeGenomesNamesExtensions(genomesNames) 
  unitedFamilies = doUnion(families)

  for genomeName in genomesNames:
    finalGenome = createFinalGenome(genomeName, unitedFamilies)
    writeFinalGenomeIntoFile(finalGenome, genomeName)

# implementação usando programação dinâmica,
# muito eficiente
def createFinalGenomes(families, genomesNames):
  from disjointSets import doUnion
  from disjointSetsUtils import doAssignment
  doUnion(families)
  doAssignment(genomesNames)

if __name__ == "__main__":

  from families import createFamilies

  genomesNames = ['BuchAphi', 'Wglos']

  resultsFilename = 'Files/resultadoAllVsAll.txt'
  maxBsDictFilename = 'Files/maxBitscoresAllVsAll'
  families = createFamilies(resultsFilename, maxBsDictFilename)
  # for f in families.items():
    # print(f)
  createFinalFamilyAssignedGenomes(families, genomesNames)
  
from convert import convertGBToFasta
from utils import addFastaExtensionAndFilesPrefix, \
  addFilesPrefix
from read import readFileLines

def fixSlashNs(line):
  return line.rstrip('\n') + '\n'

def appendFastaInBankOfGenes(genomeName, bankFile):
  genomeName = addFastaExtensionAndFilesPrefix(genomeName)

  lines = readFileLines(genomeName)
  for line in lines:
    bankFile.write(fixSlashNs(line))

  print('Appended %s to bankFile provided!' % (genomeName))

def createBankOfGenesFromGBFiles(genomesNames, \
  outputFilename='Files/bankOfGenes.fasta'):

  outputFilename = addFilesPrefix(outputFilename)

  bankOfGenesFile = open(outputFilename, 'w')

  for name in genomesNames:    
    # 1. convert name.gb to name.fasta
    convertGBToFasta(name)    
    # 2. append name.fasta in bankOfGenesFile
    appendFastaInBankOfGenes(name, bankOfGenesFile)
    pass

def createBankOfGenesFromFastaFiles(genomesNames, \
  outputFilename='Files/bankOfGenes.fasta'):

  bankOfGenesFile = open(outputFilename, 'w')

  for name in genomesNames:
    appendFastaInBankOfGenes(name, bankOfGenesFile)

if __name__ == "__main__":
  genomesNames = ['a', 'b']

  createBankOfGenesFromFastaFiles(genomesNames)
    
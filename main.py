from bankOfGenes import createBankOfGenesFromFastaFiles, \
  createBankOfGenesFromGBFiles
from geneRefs import createListOfGenesUids
from blast import blast
from bitScores import createMaxBitscoresDict
from families import createFamilies
from finalGenomes import createFinalGenomes

if __name__ == "__main__":
  # genomesNames = ['allgb', 'allgb2', 'all3']
  genomesNames = ['BuchAphi', 'Wglos', 'EscheColi', 'HaemoInfl', 'PasteMult', 'PseudAeru', 'SalmoEnte', 'VibriChol-I', 'VibriChol-II', 'XanthCamp', 'XanthCitr', 'XylelFast', 'YersiCO92', 'YersiKIM10+']

  # genomesNames = ['BuchAphi', 'Wglos', 'EscheColi', 'HaemoInfl']

  bankOfGenesFilename = 'Files/bankOfGenes.fasta'

  # Passo 1 + Passo 2
  createBankOfGenesFromGBFiles(genomesNames, bankOfGenesFilename)

  # Passo 3
  for genomeName in genomesNames:
    createListOfGenesUids(genomeName)

  resultsFilename = 'Files/resultadoAllVsAll.txt'

  # Passo 4
  print('executando o blast...')
  blast(bankOfGenesFilename, bankOfGenesFilename, 6, \
    resultsFilename)

  maxBsDictFilename = 'Files/maxBitscoresAllVsAll'

  # Passo 5
  createMaxBitscoresDict(resultsFilename, maxBsDictFilename)  

  # Passo 6
  families = createFamilies(resultsFilename, maxBsDictFilename)

  # Passo 7  
  createFinalGenomes(families, genomesNames)

  print('fim da main.')
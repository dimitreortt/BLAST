from clean import cleanResultText
from read import readFileLines

def buildMaxBitscoresDict(results):
  maxBitscoresDict = {}

  for result in results:
    qid, sid, pident, length, mismatch, gapopen, qstart, qend, sstart, send, evalue, bitscore = result.split()

    if qid == sid:
      if qid in maxBitscoresDict or pident != '100.000':
        # print('erro em bsdict', pident != '100.000')
        # print(result)
        pass
        # exit()

      maxBitscoresDict[qid] = bitscore

  return maxBitscoresDict

def writeMaxBitscoresInFile(scores, outputFilename='Files/maxBitscoresAllVsAll'):
  maxbsFile = open(outputFilename, 'w')

  for uid, score in list(scores.items()):
    maxbsFile.write('%s %s\n' % (uid, score))

  maxbsFile.close()

def readMaxBitscoresDict(maxBSDFilename='Files/maxBitscoresAllVsAll'):
  lines = readFileLines(maxBSDFilename)
  maxbsDict = {}

  for line in lines:
    uid, bitscore = line.rstrip('\n').split(' ')
    maxbsDict[uid] = bitscore
    # print(uid, bitscore)

  return maxbsDict
  pass

def readResultText(filename):
  cleanResultText(filename)
  return readFileLines(filename)

def extractResultLines(filename):
  results = [line.rstrip('\n') for line in open(filename).readlines() if line != '\n']
  return results

def readGenesUids(filename):
  return open(filename).readlines()

def addListOfGenesUidsPrefix(filename):
  return 'listOfGenesUids' + filename if 'listOfGenesUids' not in filename else filename

def removeListOfGenesUidsPrefix(string):
  return string.replace('listOfGenesUids', '')

def createMaxBitscoresDict(resultsFilename, outputFilename=''):
  results = readResultText(resultsFilename)
  maxbsDict = buildMaxBitscoresDict(results)
  writeMaxBitscoresInFile(maxbsDict, outputFilename)

  print('Created maxbitscoresDict for ' + resultsFilename)

if __name__ == "__main__":
  resultsFilename = 'Files/resultadoAllVsAll.txt'

  createMaxBitscoresDict(resultsFilename, 'Files/maxBitscoresAllVsAll')  
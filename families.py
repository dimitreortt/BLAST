from bitScores import readMaxBitscoresDict
from clean import cleanResultText
from read import readFileLines

def shortName(uid):
  if '|' not in uid:
    print('error in shortName')
    exit()

  if uid[0] == '>':
    uid = uid[1:]

  return uid.split(' ')[0]

def retrieveInfoFromResult(result):
  qid, sid, pident, length, mismatch, gapopen, qstart, qend, sstart, send, evalue, bitscore = result.split()
  return qid, sid, bitscore

def addToFamilyIfSimilarEnough(family, sid, bitscore):
  pass

maxBitscoresDict = {}
def similarEnough(qid, sid, bitscore):
  global maxBitscoresDict
  try:
    value = float(bitscore) >= 0.3 * float(maxBitscoresDict[qid])
    return value
  except KeyError as e:
    print(bitscore, qid)  
    return False

def addToFamily(qid, sid, families):
  if qid not in families:
    families[qid] = [sid]
  else:
    families[qid].append(sid)

def assignFamilies(results, maxBsDictFilename):
  global maxBitscoresDict
  maxBitscoresDict = readMaxBitscoresDict(maxBsDictFilename)
  
  families = {}

  count = 0
  for result in results:
    count += 1
    qid, sid, bitscore = retrieveInfoFromResult(result)
    # if qid != sid:
    if True:
      if similarEnough(qid, sid, bitscore):
        addToFamily(qid, sid, families)

  print(count)
  return families

def readCleanResultsLines(resultsFilename):
  cleanResultText(resultsFilename)
  return readFileLines(resultsFilename)

def createFamilies(resultsFilename, maxBsDictFilename):
  results = readCleanResultsLines(resultsFilename)

  return assignFamilies(results, maxBsDictFilename)

def getGeneShortName(geneUid):
  return geneUid.split()[0][1:]

def getNumberOfDuplicates(families):
  dups = 0
  for uid, similars in families.items():
    dups += len(similars) 

  return dups

def assignGenesAsDuplicated(families):
  duplicatedGenes = []

  for uid, similars in families.items():
    for similar in similars:
      if similar not in duplicatedGenes:
        duplicatedGenes.append(similar)
    
    # if uid not in duplicatedGenes:
    #   duplicatedGenes.append(uid)

  return duplicatedGenes

# http://www.metagenomics.wiki/tools/blast/blastn-output-format-6
if __name__ == "__main__":
  families = createFamilies('Files/resultadoAllVsAll.txt')

  hundredthOfFamilies = list(families.items())[::200]
  greaterThan1 = [item for item in hundredthOfFamilies if len(item[1]) > 1]
  for item in greaterThan1:
    print(item)
  pass



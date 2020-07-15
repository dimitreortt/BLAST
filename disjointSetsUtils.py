from finalGenomes import readGenesUids, \
  uniqueInteger, nextUniqueInteger

# Estruturas de dados de 
# programação dinâmica
parent = []
piAB = {}

def checkDuplicatesInPiAB():
  global piAB
  checked = []
  for f in piAB:
    assert f not in checked
    checked.append(f)

def verifyParentAndPiAB():
  global parent
  global piAB

  assert len(piAB.items()) == len(parent)
  checkDuplicatesInPiAB()

def buildParentAndPiAB(families):
  global parent
  global piAB

  count = 0
  for f in families:
    piAB[f] = count
    count += 1
    parent.append(-1)

  verifyParentAndPiAB()

def showParentAndPiAB():
  global parent
  global piAB

  print(parent)
  print(list(piAB.items()))

def root(idx):
  global parent
  if parent[idx] < 0:
    return idx

  # Criar atalho
  return root(parent[idx])
  # elif parent[parent[idx]] < 0:
  #   return parent[idx]

  # else:
  #   parent[idx] = parent[parent[idx]]

def getUidFamily(uid):
  global piAB

  try:
    return root(piAB[uid])
  except KeyError:
    return nextUniqueInteger()

def doAssignment(genomesNames):
  for name in genomesNames:
    finalGenome = createFinalGenome(name, 'Files/')
    writeFinalGenomeIntoFile(finalGenome, name)

def createFinalGenome(genomeName, inputFolder='SmallTestGenomes/'):
  genesUids = readGenesUids(inputFolder + genomeName)
  return [getUidFamily(geneUid) for geneUid in genesUids]  

def writeFinalGenomeIntoFile(finalGenome, genomeName):
  gfile = open('SmallTestGenomes/' + genomeName + '.final', 'w')
  finalGenome = [str(i) for i in finalGenome]
  gfile.write(' '.join(finalGenome))

def numberOfSetsOfSize1():
  global parent
  count = 0
  for value in parent:
    if value == -1:
      count += 1

  return count

def numberOfOrphans(families):
  count = 0
  for f in families:
    if len(families[f]) == 1:
      assert families[f][0] == f
      count += 1
  
  return count

def getOrphans(families):
  orphans = {}
  for f in families:
    if len(families[f]) == 1:
      assert families[f][0] == f
      orphans[f] = families[f]
  
  return orphans

def numberOfOrphansInOtherFamilies(families):
  orphans = getOrphans(families)

  presences = []
  for uid in orphans:
    count = 0
    for f in families:
      if uid in families[f]:
        count += 1
    presences.append(count)

  presences = [i for i in presences if i > 1]

  print(presences, len(presences))
  return len(presences)
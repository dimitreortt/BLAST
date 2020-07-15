def stringToList(string):
  return string.replace('[', '').replace(']', '').replace(' ', '').replace('\'', '').split(',')

count = 10000
def fixUids(uids):
  global count
  for idx, uid in enumerate(uids):
    if '|' in uid:
      uids[idx] = str(count)
      count += 1

  return uids

def coherseGenome(finalGenome):
  return [int(item) if '|' not in item else item for item in finalGenome]

def fixFinalGenomeString(finalGenomeString):
  finalGenome = stringToList(finalGenomeString)
  finalGenome = fixUids(finalGenome)
  finalGenome = coherseGenome(finalGenome)

  return finalGenome  

def writeFinalGenome(finalGenome, genomeName):
  gfile = open(genomeName + '.finalFixed', 'w')

  for uid in finalGenome:
    gfile.write('%s ' % uid)

  gfile.close()

def readFinalGenome(genomeName):
  return open(genomeName + '.final').read()

def fixFinalGenome(genomeName):
  genome = readFinalGenome(genomeName)
  genome = fixFinalGenomeString(genome)
  writeFinalGenome(genome, genomeName)

def fixFinalGenomes(genomesNames):
  for name in genomesNames:
    fixFinalGenome(name)

if __name__ == "__main__":
  genomesNames = ['BuchAphi', 'EscheColi']
  fixFinalGenomes(genomesNames)

  
  

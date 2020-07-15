class Family():
  def __init__(self, name, uid, similars = []):
    self.name = name
    self.uid = uid
    self.similars = similars

  def append(self, uid):
    self.uids.append(uid)

  def __contains__(self, uid):
    return uid in self.uids

  def __str__(self):
    return 'name: %s, uids: %r' % (self.name, self.uids) 

def searchDuplicatedLines(lines):
  for i, line in enumerate(lines):
    for j, line2 in enumerate(lines[i + 1:]):
      if line == line2:
        print(i, j, line, line2)

def searchDuplicatedUids(lines):
  print('Pesquisando uids duplicados...')
  searchDuplicatedLines(lines)

def printOneHundredthOfTheLines(lines):
  for line in lines[::100]:
    print(line.rstrip('\n'))

count = 0
def uidInMaxBitscoresList(bslist, uid):
  global count
  for bs in bslist:
    if uid in bs:
      return True

  return False

def checkGenomeUidsInMaxBitscoresList(bslist, genomeUids):
  global count
  for uid in genomeUids:
    if not uidInMaxBitscoresList(bslist, uid):
      count += 1
      print('%s is not in bslist!' % uid)

  print(count)

def readLinesWithoutSlashNs(filename):
  return [line.rstrip('\n') for line in open(filename).readlines()]

if __name__ == "__main__":
  maxBitscores = readLinesWithoutSlashNs('Files/maxBitscoresAllVsAll')
  buchAphiUids = readLinesWithoutSlashNs('Files/BuchAphi.uids')
  escheColiUids = readLinesWithoutSlashNs('Files/EscheColi.uids')

  # printOneHundredthOfTheLines(maxBitscores)

  checkGenomeUidsInMaxBitscoresList(maxBitscores, escheColiUids)
  checkGenomeUidsInMaxBitscoresList(maxBitscores, buchAphiUids)
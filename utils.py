def findOriginIdx(lines):
  for idx, line in enumerate(lines):
    if 'ORIGIN' in line:
      return idx

def startFastaFile(gbfilename):
  if '.gb' in gbfilename:
    fastaFilename = gbfilename.replace('.gb', '.fasta')
  else:
    fastaFilename = gbfilename + '.fasta'

  if 'Files/' not in fastaFilename:
    fastaFilename = 'Files/' + fastaFilename

  return open(fastaFilename, "w")

def getGeneStartingIndexes(lines):
  geneStartingIndexes = []
  for idx, line in enumerate(lines):
    if 'gene' in line and '..' in line:
      # print(line, lines[idx], idx) 
      geneStartingIndexes.append(idx)

  # print(geneStartingIndexes)
  return geneStartingIndexes

def addFastaExtension(filename):
  return filename + '.fasta' if '.fasta' not in filename else filename

def addGBExtension(filename):
  return filename + '.gb' if '.gb' not in filename else filename

def addFilesPrefix(filename):
  return 'Files/' + filename if 'Files/' not in filename else filename

def addFastaExtensionAndFilesPrefix(filename):
  filename = addFastaExtension(filename)
  return addFilesPrefix(filename)

def removeExtension(filename):
  return filename.split('.')[-2] if '.' in filename else filename

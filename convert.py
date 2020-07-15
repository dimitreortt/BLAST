from extract import extractTranslation, extractGeneUniqueIdentifier
from utils import startFastaFile, getGeneStartingIndexes, findOriginIdx,\
  addGBExtension, addFilesPrefix

def convertGeneMetadataFromGBToFasta(metadata, fastaFile, filename):
  geneTranslation = extractTranslation(metadata)
  
  if not geneTranslation:
    return

  geneUid = extractGeneUniqueIdentifier(metadata, filename)

  fastaFile.write(geneUid + '\n')
  fastaFile.write(geneTranslation + '\n')

def separateGenesMetadatas(filename):
  filename = addGBExtension(filename)
  filename = addFilesPrefix(filename)

  lines = open(filename).readlines()

  geneIndexes = getGeneStartingIndexes(lines)
  # Sign end of genes contents in gb file
  endOfGenesContentsIdx = findOriginIdx(lines)
  geneIndexes.append(endOfGenesContentsIdx)

  genesMetadatas = []
  for i in range(len(geneIndexes) - 1):
    start = geneIndexes[i]
    end = geneIndexes[i + 1]

    geneMetadata = lines[start: end]
    genesMetadatas.append(geneMetadata)

  return genesMetadatas    

def setupConversion(filename):
  genesMetadatas = separateGenesMetadatas(filename)  

  fastaFile = startFastaFile(filename)

  return fastaFile, genesMetadatas

def convertGBToFasta(filename='allgb.gb'):
  if 'Files/' not in filename:
    filename = 'Files/' + filename

  fastaFile, genesMetadatas = setupConversion(filename)

  for geneMetadata in genesMetadatas:
    convertGeneMetadataFromGBToFasta(geneMetadata, fastaFile, filename)  

  print('Conversion succeeded!')

if __name__ == "__main__":
  convertGBToFasta('BuchAphi.gb')
  pass
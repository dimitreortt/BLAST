from convert import separateGenesMetadatas
from extract import extractGeneUniqueIdentifier
from utils import addGBExtension, addFilesPrefix, removeExtension

def shortUid(uid):
  return uid.split(' ')[0].replace('>', '')

def appendUidToFile(file, uid):
  file.write(shortUid(uid) + '\n')

def getGenesMetadatasFromRawFilename(gbFilename):
  gbFilename = addFilesPrefix(gbFilename)
  gbFilename = addGBExtension(gbFilename)

  return separateGenesMetadatas(gbFilename)

def startOutputFile(gbFilename, outputFilename):
  if not outputFilename:
    outputFilename = removeExtension(gbFilename) + '.uids'

  outputFilename = addFilesPrefix(outputFilename)

  return open(outputFilename, 'w')

def createListOfGenesUids(gbFilename, outputFilename=''):  
  listFile = startOutputFile(gbFilename, outputFilename)
  genesMetadatas = getGenesMetadatasFromRawFilename(gbFilename)

  for geneMetadata in genesMetadatas:
    uid = extractGeneUniqueIdentifier(geneMetadata, gbFilename)
    if uid:
      appendUidToFile(listFile, uid)

  listFile.close()
  print('Fim de create list of genes uids! Filename: %s' % gbFilename)

if __name__ == "__main__":
  createListOfGenesUids('EscheColi')
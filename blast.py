from convert import convertGBToFasta
from geneRefs import createListOfGenesUids
from utils import addFastaExtensionAndFilesPrefix
import os

def blast(query = 'Files/a', subject = 'Files/b', outfmt = 6, \
  outFilename = 'Files/resultado.txt'):

  query = addFastaExtensionAndFilesPrefix(query)
  subject = addFastaExtensionAndFilesPrefix(subject)

  os.system('blastp -query %s -subject %s -outfmt %d > %s' % \
    (query, subject, outfmt, outFilename))

if __name__ == "__main__":
  # convertGBToFasta('Files/EscheColi.gb')
  # createListOfGeneRefs('Files/EscheColi.gb')

  blast('EscheColi', 'EscheColi', 6, 'Files/resultado3.txt')
  pass

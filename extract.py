'''
gene unique identifier:
>sp|<swiss_prot>|LPT_<NOME> </product> OS=<genome string> OX=83333 GN=</gene> PE=3 SV=1
>sp|P0AD86|LPT_ECOLI thr operon leader peptide OS=Escherichia coli (strain K12) OX=83333 GN=thrL PE=3 SV=1

'''

from extractUtils import *
import time

def extractFromQuotes(line):
  s = line.split('"')
  if len(s) == 3:
    return s[-2]
  
  elif len(s) == 2:
    return s[-1][:-1]

  else:
    print('Error in extract from quotes')
    exit()

def extractSwissProt(metadata):
  swiss_prot = ''
  for line in metadata:
    if '/db_xref=' in line and 'Swiss-Prot:' in line:
      text = line.split('"')[-2]
      swiss_prot = text.split(':')[-1]
      return swiss_prot
  
  if swiss_prot == '':
    for line in metadata:
      if '/protein_id="' in line:
        text = line.split('"')[-2]
        swiss_prot = text.split(':')[-1]
        return swiss_prot

  for line in metadata:
    pass
    # print(line) 
  return None

def extractProduct(metadata):
  for line in metadata:
    if '/product=' in line:
      a = extractFromQuotes(line)
      if '/product' in a:
        print(line)
        print(a)
        exit()
      return extractFromQuotes(line)

def extractGN(metadata):
  for line in metadata:
    if '/gene="' in line:
      return line.split('"')[-2]

def extractTranslation(metadata):
  for idx, line in enumerate(metadata):
    if '/translation="' in line:
      if(translationInsideOnlyOneLine(line)):
        return extractFromQuotes(line)

      return gatherTranslationFromManyLines(metadata[idx:])

def extractShortName(filename):
  if filename == 'Escherichia coli (strain K12)':
    return 'ECOLI'
  
  elif filename == 'allgb':
    return 'allgb'
  
  return filename.split(' ')[0]

def extractGeneUniqueIdentifier(geneMetadada, filename):  
  # filename = filename.replace('.gb', '')
  swissProt = extractSwissProt(geneMetadada)

  if not swissProt:
    return None

  # This is an important trick to prevent genes that do not
  # have encoding translation to be considered anywhere else
  # in the implementation of the families assignment
  if not extractTranslation(geneMetadada):
    return None

  product = extractProduct(geneMetadada)
  gn = extractGN(geneMetadada)
  filename = removeExtensionAndFolderPrefix(filename)
  shortName = extractShortName(filename)

  return '>sp|%s|LPT_%s %s OS=%s OX=83333 GN=%s PE=3 SV=1' % \
  (swissProt, shortName, product, filename.replace('.fasta', ''), gn)
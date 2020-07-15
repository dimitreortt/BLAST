def removeSpaces(line):
  return line.replace(' ', '')
  
def lastTranslationLine(line):
  return '"' in line

def endOfTranslation(lastMetadataLine):
  return removeSpaces(lastMetadataLine.split('"')[-2])

def seekEndOfTranslation(metadata):
  translation = ''
  for line in metadata:
    if lastTranslationLine(line):
      return translation + endOfTranslation(line)
    
    translation += removeSpaces(line)
      
def translationInsideOnlyOneLine(line):
  return len(line.split('"')) == 3

def begginingOfTranslation(firstMetadataLine):
  return firstMetadataLine.split('"')[-1]  

def gatherTranslationFromManyLines(translationMetadata):
  # Beggining of the translation  
  firstLine = begginingOfTranslation(translationMetadata[0])
  otherLines = seekEndOfTranslation(translationMetadata[1:])

  return firstLine + otherLines

def removeExtensionAndFolderPrefix(filename):
  filename = filename.replace('Files/', '')
  return filename.split('.')[0]
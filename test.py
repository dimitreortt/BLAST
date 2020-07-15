from families import createFamilies

if __name__ == "__main__":
  resultsFilename = 'Files/resultadoAllVsAll.txt'
  maxBsDictFilename = 'Files/maxBitscoresAllVsAll'

  families = createFamilies(resultsFilename, maxBsDictFilename)

  for key, value in families.items():
    if len(value) > 2:
      print(key, value)
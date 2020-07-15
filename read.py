def readFileLines(filename):
  resultfile = open(filename, 'r')
  lines = resultfile.readlines()
  resultfile.close()
  return lines

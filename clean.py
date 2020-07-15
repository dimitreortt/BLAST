from read import readFileLines

def cleanLine(line):
  allowed = '1234567890qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM|-_ \t\n.'
  cleaned = []
  for letter in line:
    if letter in allowed:      
      cleaned.append(letter)

  return ''.join(cleaned).replace('\t', ' ')

def overwriteFileLines(lines, filename):
  resultfile = open(filename, 'w')

  for line in lines:
    if line != '\n':
      resultfile.write(line.rstrip('\n') + '\n')

  resultfile.close()

def cleanLines(lines):
  return [cleanLine(line) for line in lines]

def cleanResultText(filename):
  lines = readFileLines(filename)    
  overwriteFileLines(cleanLines(lines), filename)

if __name__ == "__main__":
  cleanResultText('Files/resultado.txt')

  lines = open('Files/resultado.txt').readlines()
  print(lines[0])
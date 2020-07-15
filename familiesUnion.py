class Family():
  def __init__(self, uid, similars = [], name=''):
    self.name = name
    self.uid = uid
    self.similars = similars

  def append(self, uid):
    self.uids.append(uid)

  def __eq__(self, family2):
    return self.name == family2.name and self.uid == family2.uid

  def size(self):
    return len(self.similars)

  def extendFamily(self, otherFamily):
    otherSimilars = otherFamily.similars
    changesMade = False

    for similar in otherSimilars:
      if similar not in self.similars:
        self.similars.append(similar)
        changesMade = True

    return changesMade

  def __contains__(self, uid):
    return uid in self.similars

  def __str__(self):
    return 'name: %s, uids: %r' % (self.name, self.similars)      

def startUnitedFamilies(families):
  unitedFamilies = []

  for uid, similars in families.items():
    unitedFamilies.append(Family(uid, similars))
  
  return unitedFamilies

def printUnitedFamilies(unitedFamilies):
  for f in unitedFamilies:
    print(f)

def extendFamily(similar, similars, family, families):
  changesMade = False

  # Extend similars to family
  for uid in similars:
    if uid not in family:
      family.append(uid)  
      changesMade = True

  return changesMade

# families é um dicionário {'uid' : Family('uid')}
def findFamilyThatContainsUid(uid, families):
  for uid2, family in families.items():
    if uid in family:
      return uid2, family

  # exit('Erro em findFamily!')
  # print(uid)

def uniteTwoFamilies(f1, f2, uid2, families):
  # print('in uniteTwoFamilies')
  # printFamilies(families)

  changesMade = f1.extendFamily(f2)
  # if not changesMade:
    # exit('Erro em uniteTwoFamilies!')

  families.pop(uid2)

def familyIsTheOnlyOneContainingUid(uid, family, families):
  count = 0
  for uid2, family2 in families.items():
    if family2 == family:
      count += 1
      if count != 1:
        exit('Erro em familyistheonlyonecontaininguid.....')
      continue

    if uid in family2:
      return False

  return True

def unionFamily(family, families):
  similars = family.similars
  changesMade = False

  for uid in similars:
    if uid in families:
      if families[uid] == family:
        continue

      family2 = families[uid] # -> Potencial erro nessa linha, 
                              #     gene sem maxBitscore entra em outra familia...
      uid2 = uid
      # print('uf if', uid)

    elif familyIsTheOnlyOneContainingUid(uid, family, families):
      continue

    else:
      uid2, family2 = findFamilyThatContainsUid(uid, families)

    uniteTwoFamilies(family, family2, uid2, families)
    changesMade = True

  return changesMade

def convertFamiliesDictToSecondFormat(families):
  newFamiliesDict = {}
  count = 0

  for uid, similars in families.items():
    newFamiliesDict[uid] = Family(uid, similars, count)
    count += 1

  return newFamiliesDict

def printFamilies(families):
  for item in families.items():
    print(item[0], item[1])
  print('\n')

def doUnion(families):
  families = convertFamiliesDictToSecondFormat(families)
  
  count = 0
  changesMadeList = []
  print(len(families.items()))
  while True:
    count += 1
    if count % 50 == 0:
      print(count, 'new fmlies size: ', len(families.items()))
    
    for f in families:
      changesMade = unionFamily(families[f], families)      
      if changesMade:
        break
    if not changesMade:
      break

  return families

    

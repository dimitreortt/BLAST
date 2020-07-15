class VerifiedFamily():
  def __init__(self, name):
    self.name = name
    self.uids = []

  def append(self, uid):
    self.uids.append(uid)

  def __contains__(self, uid):
    return uid in self.uids

  def __str__(self):
    return 'name: %s, uids: %r' % (self.name, self.uids)

class VerifiedFamilies():
  def __init__(self, name):
    self.families = []

  def __contains__(self, uid):
    for family in self.families:
      if uid in family:
        return True
    
    return False
  

def verifyFamilies(families):
  verifiedFamilies = []
  

  # Union-Find
  for family in families:

    for uid in families[family]:
      pass


  for family in families:
    print(family)

  return verifiedFamilies
from disjointSetsUtils import parent, piAB, \
  verifyParentAndPiAB, buildParentAndPiAB, root

from finalGenomes import readGenesUids

def hasSameRoot(uid1, uid2):
  global piAB

  return root(piAB[uid1]) == root(piAB[uid2])

# hook second in the first
def hook(uid1, uid2):
  global parent
  global piAB

  parent[piAB[uid2]] = root(piAB[uid1])
  parent[root(piAB[uid1])] -= 1

def merge(uid1, uid2, families):
  if uid1 == uid2:
    return
  # piAB
  elif hasSameRoot(uid1, uid2):
    return
  
  hook(uid1, uid2)
  # for s in families[uid2]:
    # merge(uid1, s)

def doUnion(families):
  buildParentAndPiAB(families)
  for uid in families:
    # for s in uid.similars:
    for s in families[uid]:
      merge(uid, s, families)


if __name__ == "__main__":  
  pass


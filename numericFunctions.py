def listTotal(xList):
  pos = 0
  total = 0
  while pos < len(xList):
    total += xList[pos]
    pos += 1
  print(total)

def countEvens(xList):
  pos = 0
  evens = 0
  while pos < len(xList):
    if xList[pos]%2 == 0:
      evens += 1
    pos += 1
  print(evens)

def countOdds(xList):
  pos = 0
  odds = 0
  while pos < len(xList):
    if xList[pos]%2 != 0:
      odds += 1
    pos += 1
  print(odds)

def sequentialSearch(xList, target):
  pos = 0
  if target in xList:
    while xList[pos] != target:
      pos += 1
  else:
    pos = -1
  print(pos)

def revSequentialSearch(xList, target):
  pos = 0
  targetPos = -1
  while pos < len(xList):
    if xList[pos] == target:
      targetPos = pos
    pos += 1
  print(targetPos)

def valueCount(xList, target):
  pos = 0
  targetCount = 0
  while pos < len(xList):
    if xList[pos] == target:
      targetCount += 1
    pos += 1
  print(targetCount)

def replaceValue(xList, oldVal, newVal):
  while sequentialSearch(xList, oldVal) != -1:
    oldValPos = sequentialSearch(xList, oldVal)
    xList.remove(oldVal)
    xList.insert(oldValPos, newVal)
  print(xList)

def replaceValue(xList, oldVal, newVal):
  index = 0;
  while index < len(xList):
    if xList[index] == oldVal:
      xList[index] = newVal;
    index += 1
  print(xList)
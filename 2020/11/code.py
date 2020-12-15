from os import read
import time
import copy

def readInputFile(fileName) :
  with open(f"{__file__.rstrip('code.py')}{fileName}",'r') as f :
    return [list(line.strip()) for line in f.read().splitlines()]



def replaceCharAdjacenctAtleastOne(xpos, ypos, char, inList):
  skipU = True if ypos == 0 else False
  skipD = True if ypos == len(inList) - 1 else False
  skipL = True if xpos == 0 else False
  skipR = True if xpos == len(inList[ypos]) - 1 else False

  count = 0

  # dir - left
  if not(skipL) :
    for x in range(xpos-1, -1, -1 ):
      y = ypos
      if (not(y == ypos and x == xpos) and inList[y][x] != '.' ):
        count += 1 if inList[y][x] == char else 0
        break


  # dir - right
  if not(skipR):
    for x in range(xpos, len(inList[ypos])):
      y = ypos
      if (not(y == ypos and x == xpos) and inList[y][x] != '.'):
        count += 1 if inList[y][x] == char else 0
        break


  # dir - up
  if not(skipU):
    for y in range(ypos-1, -1, -1):
      x = xpos
      if (not(y == ypos and x == xpos) and inList[y][x] != '.'):
        count += 1 if inList[y][x] == char else 0
        break


  # dir - down
  if not(skipD):
    for y in range(ypos, len(inList)):
      x = xpos
      if (not(y == ypos and x == xpos) and inList[y][x] != '.'):
        count += 1 if inList[y][x] == char else 0
        break


  # dir - up left
  if not(skipL) :
    x = xpos
    for y in range(ypos-1, -1, -1):
      x = x - 1
      if x >= 0 :
        if (not(y == ypos and x == xpos) and inList[y][x] != '.'):
          count += 1 if inList[y][x] == char else 0
          break
      else:
        break


  # dir - up right
  traverseUpR = 0
  if not(skipR):
    x = xpos
    for y in range(ypos-1, -1, -1 ):
      x = x + 1
      if x <= len(inList[y]) - 1:
        if (not(y == ypos and x == xpos) and inList[y][x] != '.'):
          count += 1 if inList[y][x] == char else 0
          break
      else:
        break


  # dir - bottom left
  if not(skipL):
    x = xpos
    for y in range(ypos + 1, len(inList)):
      x = x - 1
      if x >= 0:
        if (not(y == ypos and x == xpos) and inList[y][x] != '.'):
          count += 1 if inList[y][x] == char else 0
          break
      else:
        break


  # dir - bottom right
  if not(skipR):
    x = xpos
    for y in range(ypos + 1, len(inList)):
      x = x + 1
      if x <= len(inList[y]) - 1:
        if (not(y == ypos and x == xpos) and inList[y][x] != '.'):
          count += 1 if inList[y][x] == char else 0
          break
      else:
        break

  return count

def replaceCharImmediateAdjacency(xpos, ypos, char, inList):
  yrange = [0, 1]
  xrange = [0, 1]

  if len(inList) > 1 :
    if 0 < ypos < (len(inList) - 1):
      yrange = ypos - 1, ypos + 2
    elif ypos == 0 :
      yrange = ypos, ypos + 2
    else :
      yrange = ypos - 1, ypos + 1

    if 0 < xpos < (len(inList[ypos]) - 1):
      xrange = xpos - 1, xpos + 2
    elif xpos == 0:
      xrange = xpos, xpos + 2
    else:
      xrange = xpos - 1, xpos + 1

  return sum(inList[y][x] == char and (not(y == ypos and x == xpos)) for y in range(yrange[0], yrange[1]) for x in range(xrange[0], xrange[1]))


def returnSeatList(inputList, iterate, immediateAdjacent):
  tempList = copy.deepcopy(inputList)
  iterate = False

  for y, line in enumerate(inputList) :
    for x, char in enumerate(line) :
      if immediateAdjacent :
        if char == 'L' and replaceCharImmediateAdjacency(x, y, '#', inputList) == 0:
          tempList[y][x] = '#'
          iterate = True

        if char == '#' and replaceCharImmediateAdjacency(x, y, '#', inputList) >= 4:
          tempList[y][x] = 'L'
          iterate = True
      else :
        if char == 'L' and replaceCharAdjacenctAtleastOne(x, y, '#', inputList) == 0:
          tempList[y][x] = '#'
          iterate = True

        if char == '#' and replaceCharAdjacenctAtleastOne(x, y, '#', inputList) >= 5:
          tempList[y][x] = 'L'
          iterate = True

  return tempList, iterate


def countOccupiedSeats(inputList, immediateAdjacent):
  iterate = True
  while iterate :
    inputList, iterate = returnSeatList(inputList, iterate, immediateAdjacent)
  return sum(line.count('#') for line in inputList)

def test():
  inputlist = readInputFile("example.txt")

  assert countOccupiedSeats(inputlist, True) == 37
  assert countOccupiedSeats(inputlist, False) == 26

def main():
  inputlist = readInputFile("input.txt")
  print("Total No. Of Occupied Seats - ", countOccupiedSeats(inputlist, True))
  print("Total No. Of Occupied Seats Not Immediate Adjaceny- ", countOccupiedSeats(inputlist, False))


if __name__ == "__main__" :
  test_start_time = time.time()
  test()
  print("Total Execution Time [{}] seconds for Test".format(time.time() - test_start_time))
  main_start_time = time.time()
  main()
  print("Total Execution Time [{}] seconds for Test".format(time.time() - main_start_time))

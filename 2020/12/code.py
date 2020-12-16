from os import read
import time

dirList = ['N', 'E', 'S', 'W']

def readInputFile(fileName) :
  with open(f"{__file__.rstrip('code.py')}{fileName}",'r') as f :
    return [line.strip() for line in f.read().splitlines()]


def getNewDir(currdirection, instruction, instructionVal):
  idxincr = 0
  idx = -1 if dirList.index(currdirection) + 1 == len(dirList) else dirList.index(currdirection)
  if instructionVal == 180 :
    idxincr = 2
    idxincr *= -1 if idx+idxincr >= len(dirList) else 1
  elif ((instruction == 'R' and instructionVal == 90) or (instruction == 'L' and instructionVal == 270)) :
    idxincr = 1
  else:
    idxincr = -1

  return dirList[idx+idxincr]

def findManhattanDistance(inputList):
  east, north = 0 ,0
  currdirection = 'E'

  for line in inputList :
    instruction = line[0:1].strip()
    instructionVal = int(line[1:].strip())

    if instruction in ['L', 'R'] :
      currdirection = getNewDir(currdirection, instruction, instructionVal)
    else :
      if instruction == 'F' :
        compareDir = currdirection
      else :
        compareDir = instruction

      if compareDir in dirList:
        instructionVal = instructionVal * (1 if dirList.index(compareDir)//2 == 0 else -1)

        if dirList.index(compareDir) % 2 == 0:
          north += instructionVal
        else :
          east += instructionVal
  return abs(east) + abs(north)


def findManhattanDistance2(inputList):
  east, north = 0, 0
  waypointE, waypointN = 10, 1
  currdirection = 'E'

  for line in inputList :
    instruction = line[0:1].strip()
    instructionVal = int(line[1:].strip())

    if instruction in ['L', 'R'] :

      currdirection = getNewDir(currdirection, instruction, instructionVal)

      mulX = 1 if instruction == "R" else -1
      mulY = 1 if instruction == "L" else -1

      for _ in range(instructionVal // 90):
        twayPointN = waypointN
        twayPointE = waypointE
        waypointN = twayPointE * mulY
        waypointE = twayPointN * mulX


    elif instruction in dirList:
      instructionVal = instructionVal * (1 if dirList.index(instruction)//2 == 0 else -1)
      if dirList.index(instruction) % 2 == 0:
        waypointN += instructionVal
      else :
        waypointE += instructionVal
    else:
      east += instructionVal*waypointE
      north += instructionVal*waypointN
  return abs(east) + abs(north)

def test():
  inputlist = readInputFile("example.txt")
  # print(findManhattanDistance(inputlist, dirList))
  assert findManhattanDistance(inputlist) == 25
  assert findManhattanDistance2(inputlist) == 286
  # print(findManhattanDistance2(inputlist))

def main():
  inputlist = readInputFile("input.txt")
  print("Manhattan Distance Between that Location and Ship's Starting Position Part 1 - ", findManhattanDistance(inputlist))
  print("Manhattan Distance Between that Location and Ship's Starting Position Part 2 - ", findManhattanDistance2(inputlist))


if __name__ == "__main__" :
  test_start_time = time.time()
  test()
  print("Total Execution Time [{}] seconds for Test".format(time.time() - test_start_time))
  main_start_time = time.time()
  main()
  print("Total Execution Time [{}] seconds for Main".format(time.time() - main_start_time))

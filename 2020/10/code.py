from os import read
import time

def readInputFile(fileName) :
  with open(f"{__file__.rstrip('code.py')}{fileName}",'r') as f :
    return [int(line.strip()) for line in f.read().splitlines()]


def diffCombinations(inputList):
  numcombinations = {0:1}

  for volt in inputList :
    numcombinations[volt] = 0
    if volt - 1 in numcombinations:
      numcombinations[volt] += numcombinations[volt-1]
    if volt - 2 in numcombinations:
      numcombinations[volt] += numcombinations[volt-2]
    if volt - 3 in numcombinations:
      numcombinations[volt] += numcombinations[volt-3]

  return numcombinations[max(inputList)]

def getVolts(inputList) :
  volt1Count, volt3Count = 1 , 1
  currentVoltage = inputList[0]

  for index in range(len(inputList)) :
    if (currentVoltage + 1) in inputList :
      volt1Count += 1
      currentVoltage += 1
    elif (currentVoltage + 3) in inputList :
      volt3Count += 1
      currentVoltage += 3
    else :
      return volt1Count * volt3Count

def test():
  inputlist = sorted(readInputFile("example.txt"))
  inputlist2 = sorted(readInputFile("example2.txt"))
  assert getVolts(inputlist) == 35
  assert getVolts(inputlist2) == 220
  assert diffCombinations(inputlist) == 8
  assert diffCombinations(inputlist2) == 19208

def main():
  inputlist = sorted(readInputFile("input.txt"))
  print("Multiply of 1-volt and 3-volt - ", getVolts(inputlist))
  print("Total no. of Combinations - ", diffCombinations(inputlist))

if __name__ == "__main__" :
  test_start_time = time.time()
  test()
  print("Total Execution Time [{}] seconds for Test".format(time.time() - test_start_time))
  main_start_time = time.time()
  main()
  print("Total Execution Time [{}] seconds for Test".format(time.time() - main_start_time))

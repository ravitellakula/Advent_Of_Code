import time

def readInputFile(fileName) :
  with open(f"{__file__.rstrip('code.py')}{fileName}", "r") as f:
    return [int(line.strip()) for line in f.read().splitlines()]


def isNumSumOfOthers(inputList, number, preamble):
  return any(num1 + num2 == number for num1 in inputList for num2 in inputList if num1 != num2)

def findStandoutNumber(inputList , preamble) :
  return [inputList[index] for index in range(preamble, len(inputList)) if not(isNumSumOfOthers(inputList[index-preamble: index], inputList[index], preamble))]

def findSumofMinMaxRange (inputList, number) :
  for i in range (len(inputList)) :
    for j in range(i+2, len(inputList)):
      if (inputList[i] + sum(inputList[i+1:j]) == number) :
        sortedList = sorted(inputList[i:j])
        return(int(sortedList[0]) + int(sortedList[len(sortedList)-1]))

def test() :
  inputList = readInputFile('example.txt')
  num = findStandoutNumber(inputList, 5)[0]
  assert num == 127
  assert findSumofMinMaxRange(inputList, num) == 62

def main() :
  inputList = readInputFile('input.txt')
  num = findStandoutNumber(inputList, 25)[0]
  print ("First Number in the list that is not the sum of two of the 25 numbers before - ", num)
  print ("Encryption Weakness - ", findSumofMinMaxRange(inputList, num))

if __name__ == '__main__' :
  test_start_time = time.time()
  test()
  print("Total Execution Time [{}] seconds for Test".format (time.time() - test_start_time))
  test_main_time = time.time()
  main()
  print("Total Execution Time [{}] seconds for Actual".format(time.time() - test_main_time))

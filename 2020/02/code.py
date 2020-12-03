class Day2:

  @staticmethod
  def splitLine(inputvalue: str):
    valuelist = inputvalue.split()
    rangelist = valuelist[0].split("-")
    return ([int(rangelist[0]), int(rangelist[1]), valuelist[1][:1], valuelist[2]])


  @staticmethod
  def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [(line[:-1]) for line in f.readlines()]

  @staticmethod
  def validPasswordCount(inputvalues: list):
    validCount = 0;
    for inputval in inputvalues:
      inputValList = Day2.splitLine(inputval)
      if (inputValList[0] <= inputValList[3].count(inputValList[2]) <= inputValList[1]) :
          validCount+=1
    return validCount

  @staticmethod
  def validPasswordIndex(inputvalues: list):
    validCount = 0
    for inputval in inputvalues:
      inputValList = Day2.splitLine(inputval)
      # if ((inputValList[3].count(inputValList[2]) == 1) and ((inputValList[3][inputValList[0]-1] == inputValList[2]) or (inputValList[3][inputValList[1]-1] == inputValList[2]))):
      if (inputValList[2] == inputValList[3][inputValList[0] - 1]) ^ (inputValList[2] == inputValList[3][inputValList[1] - 1]):
          validCount +=1
    return validCount


  @staticmethod
  def test():
    inputvalues = ["1-3 a: abcde", "1-3 inputvalues: cdefg", "2-9 c: ccccccccc"]
    assert Day2.validPasswordCount(inputvalues) == 2
    assert Day2.validPasswordIndex(inputvalues) == 1

if __name__ == '__main__':
  Day2.test()
  inputvalues = Day2.readFile()
  print(f"Number Of Valid Passwords with Count:  {Day2.validPasswordCount(inputvalues)}")
  print(f"Number Of Valid Passwords with Index :  {Day2.validPasswordIndex(inputvalues)}")

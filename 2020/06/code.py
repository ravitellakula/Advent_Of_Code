import enum


class Day6:

  def readInputFile(fileName) :
    inputList = list()
    with open(f"{__file__.rstrip('code.py')}{fileName}", "r") as f:
      fileInput = f.read().splitlines()
      uniquestr = ''
      commonstr = ''

      for index, line in enumerate(fileInput):
        uniquestr += line

        if (index == 0 or (index < len(fileInput) and len(fileInput[index-1]) == 0)):
          commonstr = line

        if len(line.strip()) == 0 or len(fileInput)-1 == index :
          inputList.append((set(uniquestr), set(commonstr)))
          uniquestr = ''
          commonstr = ''
        else :
          commonstr = ''.join(set(line) & set(commonstr))


    return inputList

  def calculateSumCorrectAnswers(inputList):
    return sum(len(correntansset[0]) for correntansset in inputList)

  def calculateSumCorrectAnswersEveryone(inputList):
    return sum(len(correntansset[1]) for correntansset in inputList)

  def test() :
    assert Day6.calculateSumCorrectAnswers(Day6.readInputFile("example.txt")) == 11
    assert Day6.calculateSumCorrectAnswersEveryone(Day6.readInputFile("example.txt")) == 6

if __name__ == "__main__":
    Day6.test()
    inputList = Day6.readInputFile("input.txt")
    print("Sum Of Correct Answers - ", Day6.calculateSumCorrectAnswers(inputList))
    print("Sum Of Correct Answers For Everyone - ",
          Day6.calculateSumCorrectAnswersEveryone(inputList))

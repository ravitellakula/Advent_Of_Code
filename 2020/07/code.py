import time
import re

class Day7:

  @staticmethod
  def bagParser(contents):
    bagexp = re.compile("^(\d+) ([a-z ]+) bags?\.?$")
    count, description = bagexp.match(contents).groups()
    return (int(count), description)

  @staticmethod
  def lineParser(line):
    main_bag, contents = line.split(" bags contain ")
    if contents == "no other bags.":
        return main_bag, []
    return main_bag, [Day7.bagParser(bag) for bag in contents.split(', ')]

  @staticmethod
  def readInputFile(fileName) :
    with open(f"{__file__.rstrip('code.py')}{fileName}", "r") as f:
      return dict(Day7.lineParser(line) for line in f.read().splitlines())

  @staticmethod
  def containsBagColor(inputDict, colortocompare, colortomatch):
    if colortocompare == "shiny gold":
      return True
    return any(Day7.containsBagColor(inputDict,  dictkeyvalcolor, colortomatch) for _, dictkeyvalcolor in inputDict[colortocompare])

  @staticmethod
  def getMatchingBagCount(inputDict, colortomatch):
    return(sum((Day7.containsBagColor(inputDict,  dictkeycolor, colortomatch) and 1 or 0) for dictkeycolor in inputDict if dictkeycolor != colortomatch and len(inputDict[dictkeycolor]) > 0))

  @staticmethod
  def totalRequiredBags(inputDict, colortomatch):
    return 1 + sum(count * Day7.totalRequiredBags(inputDict, subcolor) for count, subcolor in inputDict[colortomatch])

  def test():
    inputDict = Day7.readInputFile("example.txt")
    inputDict2 = Day7.readInputFile("example2.txt")
    assert Day7.getMatchingBagCount(inputDict,"shiny gold") == 4
    assert Day7.totalRequiredBags(inputDict, "shiny gold")-1 == 32
    assert Day7.totalRequiredBags(inputDict2, "shiny gold")-1 == 126

  def main():
    inputDict = Day7.readInputFile("input.txt")
    print(f"Total Number of Matching Bags: ", Day7.getMatchingBagCount(inputDict, "shiny gold"))
    print(f"Total Number of Required Bags: ", Day7.totalRequiredBags(inputDict, "shiny gold")-1)

if __name__ == "__main__":
  test_start_time = time.time()
  Day7.test()
  print("Test --- %s seconds ---" % (time.time() - test_start_time))
  main_start_time = time.time()
  Day7.main()
  print("Main --- %s seconds ---" % (time.time() - main_start_time))

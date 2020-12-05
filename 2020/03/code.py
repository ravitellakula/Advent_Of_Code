class Day3:

  @staticmethod
  def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        # return [(line[:-1]) for line in f.readlines()]
        return f.read().splitlines()

  @staticmethod
  def countTreesSlope(inputlist:list, xaxis:int, yaxis:int) :
    treeCount = 0
    xpos = xaxis
    ypos = yaxis

    while ypos < len(inputlist):
      while len(inputlist[ypos]) < xpos+1:
        inputlist[ypos] += inputlist[ypos]
      # print(f"xpos:", xpos, "ypos", ypos, "len", len(inputlist[ypos]))
      # print(f"text:", {inputlist[ypos]})
      # print(f"character:", {inputlist[ypos][xpos]})
      if inputlist[ypos][xpos] == '#':
        treeCount +=1
      ypos += yaxis
      xpos += xaxis
    # print(treeCount)
    return treeCount

  @staticmethod
  def countandmultiplyTreesSlopes(inputList:list, slopeList:list) :
    treeCount = 1
    for slope in slopeList :
      # print(f"xaxis:", slope[0], "yaxis", slope[1], "count", Day3.countTreesSlope(inputList, slope[0], slope[1]))
      treeCount *= Day3.countTreesSlope(inputList, slope[0], slope[1])
    return treeCount

  @staticmethod
  def test():
    print('in test');
    testinput = ["..##.......", "#...#...#..", ".#....#..#.",
                 "..#.#...#.#", ".#...##..#.", "..#.##.....", ".#.#.#....#",
                 ".#........#", "#.##...#...", "#...##....#", ".#..#...#.#"]
    slopelist = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    assert(Day3.countTreesSlope(testinput,3,1)) == 7
    assert(Day3.countandmultiplyTreesSlopes(testinput, slopelist)) == 336


if __name__ == '__main__':
  Day3.test()
  inputvalues = Day3.readFile()
  slopelist = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  print(f"treeCount", Day3.countTreesSlope(inputvalues,1,1))
  print(f"treeCount Multiplied for slopelist", Day3.countandmultiplyTreesSlopes(inputvalues, slopelist))

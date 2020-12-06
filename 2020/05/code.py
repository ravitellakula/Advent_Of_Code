class Day5:
  @staticmethod
  def readInputFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
      return f.read().splitlines()

  @staticmethod
  def calculateSeatRange(seatchar, rangeList):
    midNum = (rangeList[0] + rangeList[1]) // 2

    if (seatchar in ('F','L')) :
      rangeList[1] = midNum
    else :
      rangeList[0] = midNum + 1

    return rangeList

  @staticmethod
  def calculateSeatId(seat) :
    seatNumberList = [0, 127]
    seatColList = [0, 7]

    for i, seatChar in enumerate(seat):
      if i < 7 :
        seatNumberList = Day5.calculateSeatRange(seatChar, seatNumberList)
      else :
        seatColList = Day5.calculateSeatRange(seatChar, seatColList)

    return ((seatNumberList[0] * 8 ) + seatColList[0])

  @staticmethod
  def retrieveSeatList(inputSeatList):
    seatIdList = list()
    for seat in inputSeatList:
      seatIdList.append(Day5.calculateSeatId(seat))
    return (sorted(seatIdList))

  @staticmethod
  def calculateMaxSeatId(seatIdList):
    return (seatIdList[len(seatIdList)-1])

  @staticmethod
  def findMySeatId(seatIdList):
    seatId = 0
    return [x for x in range(seatIdList[0], seatIdList[-1]+1) if x not in seatIdList]

  @staticmethod
  def test():
    testInputList = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
    seatIdList = Day5.retrieveSeatList(testInputList)
    assert Day5.calculateSeatId(testInputList[0]) == 357
    assert Day5.calculateSeatId(testInputList[1]) == 567
    assert Day5.calculateSeatId(testInputList[2]) == 119
    assert Day5.calculateSeatId(testInputList[3]) == 820
    assert Day5.calculateMaxSeatId(seatIdList) == 820

if __name__ == "__main__":
  Day5.test()
  inputList = Day5.readInputFile()
  seatIdList = Day5.retrieveSeatList(inputList)
  print("Maximum SeatId : ", Day5.calculateMaxSeatId(seatIdList))
  print("My SeatId : ", Day5.findMySeatId(seatIdList))

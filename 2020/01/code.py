class Day1:

  @staticmethod
  def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(line[:-1]) for line in f.readlines()]

  @staticmethod
  def sum2numbers(inputvalues: list):
    for inputval in inputvalues:
      if (2020 - inputval) in inputvalues:
        return (2020 - inputval) * inputval

  @staticmethod
  def sum3numbers(inputvalues: list):
    for val1index in range(len(inputvalues)):
      for val2index in range(val1index, len(inputvalues)):
        if (2020 - inputvalues[val1index] - inputvalues[val2index]) in inputvalues:
          return ((2020 - inputvalues[val1index] - inputvalues[val2index]) * inputvalues[val1index] * inputvalues[val2index])

  @staticmethod
  def test() :
    inputValues = [1721, 979, 366, 299, 675, 1456]
    assert Day1.sum2numbers(inputValues) == 514579
    assert Day1.sum3numbers(inputValues) == 241861950


if __name__ == '__main__':
  Day1.test()
  inputValues = Day1.readFile()
  print(f"Sum of 2 numbers :  {Day1.sum2numbers(inputValues)}")
  print(f"Sum of 3 numbers :  {Day1.sum3numbers(inputValues)}")

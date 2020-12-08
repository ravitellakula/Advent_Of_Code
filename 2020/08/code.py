import time
class Day8:

  @staticmethod
  def readInputFile(fileName):
    with open(f"{__file__.rstrip('code.py')}{fileName}","r") as f:
      return [line.split(" ") for line in f.read().splitlines()]


  @staticmethod
  def findAccumulatorValue(instructions) :
    pointer = 0
    accValue = 0
    processedList = list()

    while (pointer not in processedList and pointer < len(instructions)):
      processedList.append(pointer)
      instructionText, instructionVal = instructions[pointer][0], instructions[pointer][1]

      if (instructionText.strip() == "acc"):
        accValue += int(instructionVal)

      if (instructionText.strip() == "jmp"):
        pointer = pointer + int(instructionVal)
      else :
        pointer = pointer + 1
    return pointer, accValue

  @staticmethod
  def findAccumulatorTotalVal(instructions):

    pointer, accValue = 0 , 0

    for index in range(len(instructions)) :
      if instructions[index][0] == 'jmp' :
        instructions[index][0] = instructions[index][0].replace('jmp', 'nop')
        pointer, accValue = Day8.findAccumulatorValue(instructions)
        instructions[index][0] = instructions[index][0].replace('nop', 'jmp')
      elif instructions[index][0] == 'nop' :
        instructions[index][0] =  instructions[index][0].replace('nop', 'jmp')
        pointer, accValue = Day8.findAccumulatorValue(instructions)
        instructions[index][0] = instructions[index][0].replace('jmp', 'nop')
      else :
        continue

      if pointer == len(instructions) :
        return accValue


  @staticmethod
  def test():
    inputList = Day8.readInputFile('example.txt')
    assert Day8.findAccumulatorValue(inputList)[0] == 1
    assert Day8.findAccumulatorTotalVal(inputList) == 8

  @staticmethod
  def main() :
    inputList = Day8.readInputFile('input.txt')
    print(f"Accumulator Value by identifying the infinite loop - ", Day8.findAccumulatorValue(inputList)[1])
    print(f"Accumulator Value after fixing the infinite loop -", Day8.findAccumulatorTotalVal(inputList))



if __name__ == '__main__':
    test_start_time = time.time()
    Day8.test()
    print("Test --- {} seconds ---".format((time.time() - test_start_time)))
    main_start_time = time.time()
    Day8.main()
    print("Main --- {} seconds ---".format((time.time() - main_start_time)))

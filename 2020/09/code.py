import time

def readInputFile(fileName) :
  with open(f"{__file__.rstrip('code.py')}{fileName}", "r") as f:
    return [line for line in f.read().splitlines()]

def test() :
  inputList = readInputFile('example.txt')

def main() :
  inputList = readInputFile('input.txt')

if __name__ == '__main__' :
  test_start_time = time.time()
  test()
  print("Total Execution Time [{}] seconds for Test".format (time.time() - test_start_time))
  test_main_time = time.time()
  main()
  print("Total Execution Time [{}] seconds for Actual".format(time.time() - test_main_time))

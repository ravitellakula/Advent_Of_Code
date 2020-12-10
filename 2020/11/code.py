from os import read
import time

def readInputFile(fileName) :
  with open(f"{__file__.rstrip('code.py')}{fileName}",'r') as f :
    return [int(line.strip()) for line in f.read().splitlines()]


def test():
  inputlist = readInputFile("example.txt")


def main():
  inputlist = readInputFile("input.txt")


if __name__ == "__main__" :
  test_start_time = time.time()
  test()
  print("Total Execution Time [{}] seconds for Test".format(time.time() - test_start_time))
  main_start_time = time.time()
  main()
  print("Total Execution Time [{}] seconds for Test".format(time.time() - main_start_time))

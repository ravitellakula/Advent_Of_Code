from os import read
import time

def readInputFile(fileName) :
  with open(f"{__file__.rstrip('code.py')}{fileName}",'r') as f :
    return [line.strip().replace('x','0').split(",") for line in f.read().splitlines()]

def findIDOfEarliestBus(inputlist) :
  estTimestamp = int(inputlist[0][0])
  earlTimeStamp = estTimestamp
  earlbus = 0

  for bus in list(map(int, inputlist[1])):
    if bus > 0:
      bus = int(bus)
      bustime = bus * (estTimestamp//bus + 1)

      if earlbus == 0:
        earlTimeStamp = bustime
        earlbus = bus
      elif bustime < earlTimeStamp :
        earlTimeStamp = bustime
        earlbus = bus

  # print(earlTimeStamp, earlbus)
  return earlbus * (earlTimeStamp - estTimestamp)


def findTimestampForSubsequent(inputlist):
  earlTimeStamp, increment = int(inputlist[0][0]), 1

  for i, bus in enumerate(list(map(int, inputlist[1]))):
    if bus > 0 :
      while (earlTimeStamp + i) % bus != 0:
          earlTimeStamp += increment
      increment *= bus

  return earlTimeStamp

def test():
  inputlist = readInputFile("example.txt")
  assert findIDOfEarliestBus(inputlist) == 295
  assert findTimestampForSubsequent(inputlist) == 1068781

def main():
  inputlist = readInputFile("input.txt")
  print("Earliest Bus ID * Wait Time - [" ,findIDOfEarliestBus(inputlist),"]")
  print("Earliest Timestamp for all buses to depart Subsequently - [",findTimestampForSubsequent(inputlist),"]")

if __name__ == "__main__" :
  test_start_time = time.time()
  test()
  print("Total Execution Time [{}] seconds for Test".format(time.time() - test_start_time))
  main_start_time = time.time()
  main()
  print("Total Execution Time [{}] seconds for Main".format(time.time() - main_start_time))

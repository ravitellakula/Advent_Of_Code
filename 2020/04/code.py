import re
class Day4:

  @staticmethod
  def readFile(fileName):
    with open(f"{__file__.rstrip('code.py')}{fileName}", "r") as f:
      return f.read().splitlines()

  @staticmethod
  def convertStringToDict(inputString):
    return (dict((key.strip(), value.strip()) for key, value in (element.split(':') for element in inputString.split(' '))) if inputString and inputString.strip() else "")

  @staticmethod
  def checkIfAllFieldsPresent(inputDict) :
    passportfields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    return (all(key in inputDict for key in (passportfields)))

  @staticmethod
  def checkIfAllFieldsPresentAndValidWithPatterns(inputDict):
    fieldValidationPatterns = {
      "byr" :"19[2-9][0-9]|200[0-2]",
      "iyr": "20(1[0-9]|20)",
      "eyr": "20(2[0-9]|30)",
      "hgt": "(1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in)",
      "hcl": "#[0-9a-f]{6}",
      "ecl": "amb|blu|brn|gry|grn|hzl|oth",
      "pid": "[0-9]{9}"
    }
    return (all(re.fullmatch(fieldValidationPatterns[key], inputDict[key] if key in inputDict else '') for key in (fieldValidationPatterns)))

  @staticmethod
  def checkIfAllFieldsPresentAndValid(inputDict):
    passportfields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    validecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    validPassport = False
    if all(key in inputDict for key in (passportfields)) :
      if 1920 <= int(inputDict["byr"]) <= 2002 :
        if 2010 <= int(inputDict["iyr"]) <= 2020 :
          if 2020 <= int(inputDict["eyr"]) <= 2030 :
            if ((inputDict["hgt"][len(inputDict["hgt"]) - 2:] == "cm") and (150 <= int(inputDict["hgt"][: len(inputDict["hgt"]) - 2]) <= 193)
                or (inputDict["hgt"][len(inputDict["hgt"]) - 2:] == "in") and (59 <= int(inputDict["hgt"][: len(inputDict["hgt"]) - 2]) <= 76)) :
                if re.match("^#[0-9a-f]{6}$", inputDict["hcl"]):
                  if inputDict["ecl"] in validecls :
                    if re.match("^[0-9]{9}$", inputDict["pid"]):
                      validPassport = True
    return validPassport

  @staticmethod
  def countValidPassports(inputvalues):
    validCount = 0
    passportDict = {}
    for index,inputval in enumerate(inputvalues):
      passportDict.update(Day4.convertStringToDict(inputval))
      if (len(inputval) ==  0 or index == len(inputvalues)-1) :
        validCount += 1 if Day4.checkIfAllFieldsPresent(passportDict) else 0
        passportDict = {}
    return validCount

  @staticmethod
  def countValidPassportsAdvanced(inputvalues):
    validCount = 0
    passportDict = {}
    for index, inputval in enumerate(inputvalues):
      passportDict.update(Day4.convertStringToDict(inputval))
      if (len(inputval) == 0 or index == len(inputvalues)-1) :
        validCount += 1 if Day4.checkIfAllFieldsPresentAndValid(passportDict) else 0
        passportDict = {}
    return validCount


  @staticmethod
  def test():
    assert Day4.countValidPassports(Day4.readFile("example.txt")) == 2
    assert Day4.countValidPassportsAdvanced(Day4.readFile("example2.txt")) == 4

if __name__ == '__main__':
  Day4.test()
  print(f"Count of Valid Passports:",Day4.countValidPassports(Day4.readFile("input.txt")))
  print(f"Count of Valid Passports with field validations:",Day4.countValidPassportsAdvanced(Day4.readFile("input.txt")))

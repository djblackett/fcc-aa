import re

def arithmetic_arranger(problems):
  individualExpressions = []
  parsedDigits = [] 
  for problem in problems:
    parsedDigits.append(re.split(r" [+-] ", problem))
  firstLine = ""
  secondLine = ""
  thirdLine = ""
  
  #Error Checking
  if len(problems) > 5:
    return "Error: Too many problems."

  for string in problems:
    if "*" in string or "/" in string:
      return "Error: Operator must be '+' or '-'."
    
  for expression in parsedDigits:
    for i in expression:
      if re.search(r"\D", i) != None:
        return "Error: Numbers must only contain digits."
      if len(i) >= 5 or len(i) < 1:
        return "Error: Numbers cannot be more than four digits."

  #Program Logic
  for i in problems:
    individualExpressions.append(i.split(" "))
  
  for expression in individualExpressions:
    topLength = len(expression[0])
    bottomLength = len(expression[2])
    maximum = 0
    if topLength >= bottomLength:
      maximum = topLength
    else:
       maximum = bottomLength
    dashes = maximum + 2

    firstLine += "{:{align}{width}}    ".format(expression[0], align='>', width=(maximum + 2))
    secondLine += "{}{:{align}{width}}    ".format(expression[1], expression[2], align='>', width=(maximum + 1))
    thirdLine += "{}    ".format("-"*dashes)
  
  finalString = "{}\n{}\n{}".format(firstLine[:-4] ,secondLine[:-4] , thirdLine[:-4])
  
  arranged_problems = finalString
  return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

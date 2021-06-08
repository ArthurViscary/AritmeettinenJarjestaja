import re

def arithmetic_arranger(problems, showAnswers = False):


    #Error check : too many problems
    if len(problems) > 5:
        return ("Error: too many problems")

    #Error check : operators and digits
    for problem in problems:
      if(re.search("[^\s0-9.+-]", problem)):
        if(re.search("[/]", problem) or re.search("[*]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
            
    #Error check: too long numbers
    for problem in problems:
        if len(problem.split(" ")[0]) > 4 or len(problem.split(" ")[2]) > 4:
            return "Error: Numbers cannot be more than four digits."



    #setting up the variables needed for printing the answers as strings
    firstRow = ""
    bottomRow = ""
    lineRow = ""
    answerRow = ""

    #calculation phase
    for problem in problems:
        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        bottomNumber = problem.split(" ")[2]
        #which number is longer
        maxLength = max(len(firstNumber), len(bottomNumber)) + 2 

        #setting up the rows for formatting later
        firstRow += str(firstNumber.rjust(maxLength)) + "    "
        bottomRow += operator + str(bottomNumber.rjust(maxLength - 1)) + "    "
        lineRow += ("-" * maxLength) + "    "
        if operator == "+":
            answerRow += str((int(firstNumber) + int(bottomNumber))).rjust(maxLength) + "    "
        elif operator == "-":
            answerRow += str((int(firstNumber) - int(bottomNumber))).rjust(maxLength) + "    "

    if showAnswers:
        arranged_problems = firstRow + "\n" + bottomRow + "\n" + lineRow + "\n" + answerRow
    else:
        arranged_problems = firstRow + "\n" + bottomRow + "\n" + lineRow

    return arranged_problems

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))

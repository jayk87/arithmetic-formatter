def arithmetic_arranger(problems, answers = False):
  firstline = ''
  thirdline = ''
  secondline = ''
  answerline = ''

  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    for problem in problems:
      number = problem.split()
      if number[1] == "*" or number[1] == "/":
        return "Error: Operator must be '+' or '-'."
      elif max(len(x) for x in number) > 4:
        return "Error: Numbers cannot be more than four digits."
      try:
        x = int(number[0])
      except:
        return "Error: Numbers must only contain digits."
      try:
        y = int(number[2])
      except:
        return "Error: Numbers must only contain digits."
      else:
        maxlength = int(max(len(x) for x in number))
        firstline += (number[0].rjust(maxlength + 2) + "    ")
        secondline += (number[1] + number[2].rjust(maxlength +1) + "    ")
        thirdline += "-" * (maxlength + 2) + "    "
        answerline += str(eval(problem)).rjust(maxlength + 2) + "    "

    if answers == True:
      arranged_problems = [firstline.rstrip(), secondline.rstrip(), thirdline.rstrip(), answerline.rstrip()]
      arranged_problems = "\n".join(arranged_problems)

    else:
      arranged_problems = [firstline.rstrip(), secondline.rstrip(), thirdline.rstrip()]
      arranged_problems = "\n".join(arranged_problems)
    return arranged_problems
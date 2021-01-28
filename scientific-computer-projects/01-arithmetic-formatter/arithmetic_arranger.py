def valid_problems_quantity(problems):
  return len(problems) <= 5

def valid_operators(problems):
  valid = True
  for op in problems:
    if '-' in op or '+' in op:
      pass
    else:
      valid = False
      break
  return valid

def valid_numbers(problems):
  valid = True
  for op in problems:
    char = '-' if '-' in op else '+'
    numbers = op.split(char)
    if not numbers[0].strip().isnumeric() or not numbers[1].strip().isnumeric():
      valid = False
      break
  return valid


def valid_digits(problems):
  valid = True
  for op in problems:
    char = '-' if '-' in op else '+'
    numbers = op.split(char)
    if len(numbers[0].strip()) > 4 or len(numbers[1].strip()) > 4:
      valid = False
      break
  return valid

def arithmetic_arranger(problems, showAnswer=False):
  if not valid_problems_quantity(problems):
    return "Error: Too many problems."

  if not valid_operators(problems):
    return "Error: Operator must be '+' or '-'."

  if not valid_numbers(problems):
    return "Error: Numbers must only contain digits."

  if not valid_digits(problems):
    return "Error: Numbers cannot be more than four digits."

  line1 = ''
  line2 = ''
  divLine = ''
  answersLine = ''
  for p in problems:
    op = '-' if '-' in p else '+'
    numbers = p.split(op)
    a = numbers[0].strip()
    b = numbers[1].strip()
    answer = str(int(a) + int(b) if op == '+' else int(a) - int(b))
    length = (len(a) if len(a) > len(b) else len(b)) + 2

    line1 += (' ' * (length - len(a))) + a + (' ' * 4)
    line2 += op + (' ' * (length - len(b) - 1)) + b + (' ' * 4)
    divLine += ('-' * length) + (' ' * 4)
    if showAnswer == True:
      answersLine += (' ' * (length - len(answer))) + answer + (' ' * 4)

  # print("ANSWERS => ", showAnswer, answersLine)
  return f"""{line1.rstrip()}\n{line2.rstrip()}\n{divLine.rstrip()}\n{answersLine.rstrip() if showAnswer == True else ''}""".rstrip()


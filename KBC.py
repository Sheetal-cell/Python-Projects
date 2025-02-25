questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  ["Which keyword is used to define a function in Python?", "func", "define", "def", "function", "None", 3],
    ["What will be the output of print(5 + 3)?", "53", "8", "35", "Error", "None", 2],
    ["Which data type is used to store a sequence of characters?", "int", "float", "str", "bool", "None", 3],
    ["Which operator is used to check if two values are equal?", "=", "==", "!=", "<>", "None", 2],
    ["What is the result of len('Hello')?", "4", "5", "6", "Error", "None", 2],
    ["Which function is used to take user input?", "get()", "scan()", "input()", "read()", "None", 3],
    ["Which loop is used when the number of iterations is unknown?", "for", "while", "do-while", "foreach", "None", 2],
    ["What will be the output of print(10 // 3)?", "3.33", "3", "4", "Error", "None", 2],
    ["Which symbol is used for comments in Python?", "//", "/* */", "#", "--", "None", 3],
    ["What is the output of bool([])?", "True", "False", "Error", "None", "None", 2],
    ["Which data structure is used to store key-value pairs?", "List", "Tuple", "Dictionary", "Set", "None", 3],
    ["Which module is used for generating random numbers?", "math", "random", "numpy", "sys", "None", 2],
    ["Which function is used to find the maximum value in a list?", "max()", "min()", "sum()", "len()", "None", 1]
  
]
print(len(questions))

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000,1280000,2500000,5000000,10000000]
money = 0
print("Welcome to Kaun Banega Crorepati-PYTHON Version😉")
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"{question[0]}")
  print(f"1. {question[1]}          2. {question[2]} ")
  print(f"3. {question[3]}          4. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i<4):
      money=0
    elif(i >= 4 and i<9):
      money = 10000
    elif(i >= 9 and i<14):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")
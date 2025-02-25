questions = [
  ["Which Indian state has the highest GDP?", "Maharashtra", "Tamil Nadu", "Uttar Pradesh", "Gujarat", "None", 1],
    ["What was the code name for India's first nuclear test in 1974?", "Operation Vijay", "Smiling Buddha", "Agni Pariksha", "Mission Shakti", "None", 2],
    ["Which Indian economist won the Nobel Prize in Economic Sciences?", "Raghuram Rajan", "Amartya Sen", "Manmohan Singh", "Arvind Subramanian", "None", 2],
    ["Who was the first Indian to receive a Nobel Prize?", "C.V. Raman", "Mother Teresa", "Rabindranath Tagore", "Dr. B.R. Ambedkar", "None", 3],
    ["Which state in India has the largest coastline?", "Tamil Nadu", "Gujarat", "Andhra Pradesh", "Maharashtra", "None", 2],
    ["Which war led to the creation of Bangladesh in 1971?", "Indo-Pak War", "Kargil War", "Sino-Indian War", "Operation Vijay", "None", 1],
    ["Which Indian city is home to the world's largest diamond cutting and polishing industry?", "Jaipur", "Surat", "Mumbai", "Kolkata", "None", 2],
    ["Who was the first Indian to travel to space?", "Rakesh Sharma", "Kalpana Chawla", "Sunita Williams", "Vikram Sarabhai", "None", 1],
    ["Which Indian mathematician is known for his contributions to number theory and infinite series?", "C.V. Raman", "Srinivasa Ramanujan", "Aryabhata", "Bhaskara I", "None", 2]
    ["Which Indian city is home to the largest number of billionaires?", "Delhi", "Mumbai", "Bangalore", "Hyderabad", "None", 2],
    ["Which ancient university in India was one of the world's first residential universities?", "Nalanda", "Takshashila", "Vikramshila", "Banaras Hindu University", "None", 1],
    ["Who was the first woman to become the President of India?", "Indira Gandhi", "Pratibha Patil", "Sarojini Naidu", "Sushma Swaraj", "None", 2],
    ["Which Indian state has the highest literacy rate?", "Kerala", "Tamil Nadu", "Goa", "Himachal Pradesh", "None", 1],
    ["Which Indian sportsperson has won the most Olympic medals?", "Sachin Tendulkar", "Sushil Kumar", "P.V. Sindhu", "Abhinav Bindra", "None", 3],
  
]


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
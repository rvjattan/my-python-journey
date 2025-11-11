# A python program that can answer any yes or no question with a different fortune each time it executes

# format: [Name] asks: [Question]
#         Magic 8-Ball’s answer: [Answer]

# Write code below:

# Step 1: Import random module
import random

# Step 2: declare a variable "name":
name = "Ryan"

# Step 3: decalre a variable "question" and assign it a "Yes" or "No" question:
question = "Is it going to rain today?"

#Step 4: declare a variable "answer" that will hold the answer:
answer = ""

#Step 5: declare a variable that can store randomly generated number
random_number = random.randint(1, 9)

#Step 6, 7 & 8: write the if/elif/else statements for the program:
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not to tell you"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

#Step 9: print the question statement:
print(name + " asks: " + question)

#Step 10: print the Magic 8-Ball answer:
print("Magic 8-Ball's answer: " + answer)

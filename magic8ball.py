#This is a virtual Magic 8-Ball (TM don't sue me) program
from random import randint
from time import sleep

print("Welcome To the Virtual Magic 8-Ball!")
print("What is your name?")
name = input()
print("What is your question?")
question = input()
print(name + " asks: " + question)
print("Shaking the 8-Ball....")
sleep(1)
print("...")
sleep(2)
print("........")
answer = ""
random_number = randint(1, 11)

if random_number == 1:
  answer = "Yes - definitely!"
elif random_number == 2:
  answer = "It is decidedly so. You are now the Archmage."
elif random_number == 3:
  answer = "Without a doubt!"
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later, I'm sleepy peepy."
elif random_number == 6:
  answer = "Better not to tell you now (oooooh mysterious)"
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful. Like really bad."
elif random_number == 10:
  answer = "Absolutely not, you insufferable fool."
elif random_number == 11:
  answer = "Unsure, but your question pleases the Ball."
else:
  answer = "Error, you fucked up somehow."
print("Magic 8-Ball's answer: " + answer)

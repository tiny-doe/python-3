#i fucked up and forgot the rest of the exercises

#calculate the remainder of 2 numbers when divided
def remainder(num1, num2):
  return (num1 * 2) % (num2 * .5)
#Question: ok so originally I wrote "return (num1 * 2) % (num2 / 2)", why didn't that work? Isn't num2/2 = num2*.5?
#testing
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0


#take a given number to the 10th power
def tenth_power(num):
  return num ** 10
#testing
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024


#calculate the square root (pretending it's not a function in the math module)
def square_root(num):
  return num ** (1/2)
#testing
print(int(square_root(16)))
# should print 4
print(int(square_root(100)))
# should print 10


#calculate the win percentage of a fictional sports team
def win_percentage(wins, losses):
  total = wins + losses
  winning_ratio = wins / total
  percentage_win = winning_ratio * 100
  return percentage_win
#testing
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


#calculate the average between 2 numbers ( think there's also a function for that in the math module but whatever)
#i fucking hate calculating average and median and mean and shit UGH
def average(num1, num2):
  return (num1 + num2) / 2
#testing
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0


#find the remainder after 2 numbers are divided
def remainder(num1, num2):
  return (num1 * 2) % (num2 * .5)
#testing
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0


#what are the first 3 multiples of a given number? return the 3rd multiple
def first_three_multiples(num):
  print(num * 1)
  print(num * 2)
  print(num * 3)
  return num * 3
#testing
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0


#calculate the tip
#the percentage value is given as an integer despite it being technically a float by virtue of being a percentage just fyi
def tip(total, percentage):
  total_with_tip = (total * percentage) / 100
  return total_with_tip
#testing
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0


#let's say our names like we're james bond
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name
#testing
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou


#how old are you in dog years?
def dog_years(name, age):
  dog_age = age * 7
  return name + ", you are " + str(dog_age) + " years old in dog years"
#testing
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

#a clusterfuck of math equations
#oh fuck
def lots_of_math(a, b, c, d):
  a_plus_b = a + b
  print(a_plus_b)
  c_minus_d = c - d
  print(c_minus_d)
  equation = a_plus_b * c_minus_d
  print(equation)
  return equation % a
#training
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print()
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
#Question: Is there a more efficient way to do this?

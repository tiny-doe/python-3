#if you take a number and to another number's degree, is it less than 5000?
def large_power(base, exponent):
  if (base ** exponent) > 5000:
    return True
  else:
    return False
#testing
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

#Budget vs expenditures
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget < (food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False
#testing
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# is a number doubled than another number, not doubled?
def twice_as_large(num1, num2):
  if num1 > (num2 * 2):
    return True
  else:
    return False
#testing
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

#is it divisible by 10?
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False
#testing
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

# Do 2 numbers added together NOT equal 10?
def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False
#testing
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False

#Does the number equal the upper or lower limits?
def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False
#Testing
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

#Are the names the same?
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False
#testing
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

#Make a function that will ALWAYS be false (must include a number and > or <:
def always_false(num):
  if num < 0 and num > 0:
    return True
  else:
    return False
#testing
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

#Rating movies
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating > 5 and rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"
#testing
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

#Which number is the biggest of the 3?
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"
#testing
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

#Add the value of the length of the list to the end of the list
def append_size(lst):
  lst.append(len(lst))
  return lst
#testing
print(append_size([23, 42, 108]))

#Calculate the last 2 elements of a list, sum them, and add that value to the end of the list
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst
#testing
print(append_sum([1, 1, 2]))

#Which list is larger?
def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst2) > len(lst1):
    return lst2[-1]
  else:
    return lst1[-1]
#testing
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#Are there more items in a list than n?
def more_than_n(lst, item, n):
  item_count = lst.count(item)
  if item_count > n:
    return True
  else:
    return False
#testing
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#Combine, then sort the combined list
def combine_sort(lst1, lst2):
  combined_list = lst1 + lst2
  sorted_combined_list = sorted(combined_list)
  return sorted_combined_list
#testing
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#every 3 numbers from 0-100 (inclusive)
def every_three_nums(start):
  return list(range(start, 101, 3))
#testing
print(every_three_nums(91))

#remove middle slice from a list using a function
def remove_middle(lst, start, end):
  return lst[:start] + lst[end + 1:]
#testing
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#which item is more frequent in a list?
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item1) < lst.count(item2):
    return item2
  else:
    return item1
#testing
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#Double a specific integer index
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else: 
    new_lst = lst[:index]
    new_lst.append(lst[index] * 2)
    #this method adds the index without deleting the old one, despite it "editing" it
    #using the [index + 1:] deletes the old index
    new_lst2 = lst[index + 1:]
    final_lst = new_lst + new_lst2
    return final_lst
#testing
print(double_index([3, 8, -10, 12], 2))

#My favorite, find the median! /s
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]
#testing
print(middle_element([5, 2, -10, -4, 4, 5]))

#how many numbers in the list are divisible by 10?
def divisible_by_ten(nums):
  counter = 0
  for i in nums:
    if i % 10 == 0:
      counter += 1
  return counter
#testing
print(divisible_by_ten([20, 25, 30, 35, 40]))

#How to greet people
def add_greetings(names):
  greeting = []
  for name in names:
    greeting.append("Hello, " + name)
  return greeting
#testing
print(add_greetings(["Owen", "Max", "Sophie"]))

#remove initial even numbers, before hitting an odd number, then the list proceeds as normal
def delete_starting_evens(lst):
# the len(lst) > 0 bit is to tell the program to stop when there's no more numbers
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst
#no need to include a break bc it's inherent in the while loop
#testing
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#remove numbers with odd indices
def odd_indices(lst):
  new_list = []
#don't forget to be consistent in loops with your temporary variables
  for i in range(1, len(lst), 2):
    new_list.append(lst[i])
  return new_list
#testing
print(odd_indices([4, 3, 7, 10, 11, -2]))

#exponents challenge
def exponents(bases, powers):
  new_lst = []
  for i in bases:
    for num in powers:
      new_lst.append(i ** num)
  return new_lst
#testing
print(exponents([2, 3, 4], [1, 2, 3]))

#i could swear i did this one already but yolo
def larger_sum(lst1, lst2):
  if lst1 > lst2:
    return lst1
  elif lst1 < lst2:
    return lst2
  else: 
    return lst1
#testing
print(larger_sum([1, 9, 5], [2, 3, 7]))

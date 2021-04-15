#tells you if the numbers in the list are higher than 9000 powerlevels
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum
#fun fact! apparently naming your temporary variables whatever is different than naming them sum! it means something !*!*specific
print(over_nine_thousand([8000, 900, 120, 5000]))

#calculate the maximum number in a list without using max()
def max_num(nums):
  maximum = nums[0]
  for num in nums:
    if num > maximum:
      maximum = num
  return maximum
#testing
print(max_num([50, -10, 0, 75, 20]))

#Given an index in 2 lists, aggregate a new list made of the values ascribed to the matching indices (why is this so hard to explain jfc)
def same_values(lst1, lst2):
  matching_indices = []
#to iterate through indices themselves as opposed to the actual element, use range(len(list))
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      matching_indices.append(index)
  return matching_indices
#testing
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Check if 2 lists are reciprocal of one another
def reversed_list(lst1, lst2):
  #iterate thru each index 
  for index in range(len(lst1)):
    #checks if the element at a given index is the same as the element in another list at a given index
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#testing
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

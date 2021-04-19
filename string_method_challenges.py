#make a function unique_english_letters that counts how many unique letters (upper and lower case count as 2 separate letters) there are in a given word
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  total_unique_letters = 0
  for letter in letters:
    if letter in word:
      total_unique_letters += 1
  return total_unique_letters
# Uncomment these function calls to test your function:
#print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))
# should print 4
#print(unique_english_letters("booobooobooobobobobobobobobBBBoooOOOooobbbbOOOOOBOBOBOB"))


#Write a function that takes a word and a single character & returns the number of times that character appears in the word
def count_char_x(word, x):
  count_x = 0
  for letter in word:
    if letter == x in word:
      count_x += 1
  return count_x
# Uncomment these function calls to test your tip function:
#print(count_char_x("mississippi", "s"))
# should print 4
#print(count_char_x("mississippi", "m"))
# should print 1


#Write a function that counts how many times x (can be multiple characters long) appears in a given string
#The count should equal the number of elements in the split word list, minus 1
def count_multi_char_x(word, x):
  return len(word.split(x)) - 1
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "s"))
# should print 4
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


#Write a function that returns a substring starting and ending at the indices of the string. If the starting and ending indices are not in the word, or if one index is -1, return the word itself.
def substring_between_letters(word, start, end):
  word_start = word.find(start)
  if word_start < 0:
    return word
  word_end = word[word_start + 1:].find(end)
  #don't forget to add 1 to word_start when using it as an index
  if word_end < 0 or (word_start + 1 + word_end) <= word_start:
    return word
  return word[word_start + 1:word_start + 1 + word_end]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
print(substring_between_letters("mountain", "n", "n"))
#SHOULD print "tai" (it does now!)


#Write a function that takes a string and returns a Boolean depending on if every word in the sentence is greater or equal in length than x or not
def x_length_words(sentence, x):
  #x is an integer
  split_sentence = sentence.split()
  for word in split_sentence:
    if len(word) >= x:
      return True
    else:
      return False
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


#Write a function that checks if a given name is in a string, irrelevent of upper case or lower case
def check_for_name(sentence, name):
  lower_sentence = sentence.lower()
  lower_name = name.lower()
  #no need for an if/else statement for the boolean- by using return with in, it results in a boolean automatically
  return lower_name in lower_sentence
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


def every_other_letter(word):
  empty_string = ""
  for letter in range(0, len(word), 2):
    empty_string += word[letter]
  return empty_string
# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 


#Write a function that reverses a given string
def reverse_string(word):
  empty_string = ""
  #use range to access the indices of the letters in word
  #use -1 for the step value to go backwards
  #have to use len(word) - 1 to stay in range bc len(word) by itself isn't a valid index #
  for letter in range(len(word) - 1, -1, -1):
    empty_string += word[letter]
  return empty_string
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print 


#Isn't spoonerism like cockney slang?
#Anyway write a function that takes 2 strings and switch the first letters of the two words and return the new words
def make_spoonerism(word1, word2):
  return (word2[0] + word1[1:]) + " " + (word1[0] + word2[1:])

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

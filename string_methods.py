authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
#remove the commas between the names
author_names = authors.split(",")
print(author_names)
print()
#make a new list that only lists the last names of the authors
#recall in for loops acting on a list, the temporary variable represents each element, which is name here
author_last_names = []
for name in author_names:
  #use [-1] instead of [1] in case an author has a middle name or additional family names
  #while .split() automatically creates a new list, .append() does not, it just adds onto a preexisting list, so don't forget to make an empty list first to append the last names onto
  author_last_names.append(name.split()[-1])
print(author_last_names)

print()
print()

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for element in love_maybe_lines:
  #the argument for .append() needs to be the stripped list, which is element.strip()
  #redundant to make element.strip() a variable first before using .append() but it works
  love_maybe_lines_stripped.append(element.strip())
love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

print()
print()

god_wills_it_line_one = "The very earth will disown you"
#when finding the index of a multi-letter string within the given string, it will return the index of the first letter of the multi-letter string being searched for
disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)
#this outputs 20 because "d" is at god_wills_it_line_one[20]
print(god_wills_it_line_one[20])
#proof, outputs "d"

print()
print()

#.format() seems pretty rad not gonna lie
def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)
#for when you want to format but don't want to think about the order of the paramaters & arguments, define the arguments with keywords
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem \"{title}\" by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"
my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)

#OVERALL STRING METHOD REVIEW:
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
#messy
#split the string up into a list separated by commas
highlighted_poems_list = highlighted_poems.split(",")

#clean it up
highlighted_poems_stripped = []
for element in highlighted_poems_list:
  highlighted_poems_stripped.append(element.strip())

#separate out list again, separated out by colons
highlighted_poems_details = []
for element in highlighted_poems_stripped:
  highlighted_poems_details.append(element.split(":"))

#categorize the elements from the lists into their proper category
titles = []
poets = []
dates = []
#remember, i here is describing an element within a sublist of the list
for i in highlighted_poems_details:
  titles.append(i[0])
  poets.append(i[1])
  dates.append(i[2])

#print out a nice string about each poem
#use a loop to match the titles with the appropriate poets and dates
#assign the called index to variables to use them in .format()
for i in range(len(titles)):
  title, poet, date = titles[i], poets[i], dates[i]
  print("The poem \'{}\' was published by {} in {}".format(title, poet, date))

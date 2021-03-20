last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
#fucking overachiever

gradebook = [
  ["Physics", 98],
  ["Calculus", 97],
  ["Poetry", 85],
  ["History", 88]
]
#lets try the annoying way
gradebook2 = [
  [subjects[0], grades[0]],
  [subjects[1], grades[1]],
  [subjects[2], grades[2]],
  [subjects[3], grades[3]]
]
#classic STEM nerd grades can't bother w the humanities
print(gradebook)
print(gradebook2)
#cool so both methods to print these 2D lists work

#lmao of course you got a 100% in CS nerd
gradebook.append(["Computer Science", 100])
#i bet you draw like really scratchy dragons and knights or like joker faces
gradebook.append(["Visual Arts", 93])
print(gradebook)

#art teacher fucked up and is giving EVERYONE bonus points? lol sounds like an art teacher
gradebook[-1][-1] += 5
print(gradebook)

#classic STEM nerd pass/fails his poetry class
gradebook[2].remove(85)
gradebook[2].append("Pass")

#I fixed that last_semester_gradebook coding for you
print()
print("The first 4 grades are last semester, the rest are from this semester. Just FYI because it'll look confusing.")
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
print()
print("Congrats! You should probably not be a poet or an architect!")

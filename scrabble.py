letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key:value for key, value in zip(letters, points)}
#add blank tiles to letters
letters_to_points[""] = 0
#make a function that takes a word and returns the point value
def score_word(word):
  point_total = 0
  #make sure the word is converted to all-caps just in case
  word = word.upper()
  for letter in word:
    point_total += letters_to_points.get(letter, 0)
  return point_total

#testing score_word()
#brownie_points = score_word("BROWNIE")
#print(brownie_points)
#B(3) + R(1) + O(1) + W(4) + N(4) + I(1) + E(1) = 15
#prints 15

#check that .upper() works
#brownie_points_lower = score_word("brownie")
#print(brownie_points_lower)
#should also print 15

player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
  }
#map players' words to points
player_to_points = {}
#recall .items() returns both keys and values in a dict_list obj
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)
#prints {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31} therefore wordNerd wins by a point
print("The winner of the Scrabble game is " + "wordNerd" + " with " + str(player_to_points.get("wordNerd")) + " points!")
print()

#what if a player plays another word?
def play_word(player, word):
  player_to_words[player].append(word)
#testing play_word()
#play_word("player1", "brownie")
#print(player_to_words)
#should add "brownie" to player1's words

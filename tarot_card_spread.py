import random

tarot = {
  1:	"The Magician",
  2:	"The High Priestess",
  3:	"The Empress",
  4:	"The Emperor",
  5:	"The Hierophant",
  6:	"The Lovers",
  7:	"The Chariot",
  8:	"Strength",
  9:	"The Hermit",
  10:	"Wheel of Fortune",
  11:	"Justice",
  12:	"The Hanged Man",
  13:	"Death",
  14:	"Temperance",
  15:	"The Devil",
  16:	"The Tower",
  17:	"The Star",
  18:	"The Moon",
  19:	"The Sun",
  20:	"Judgement",
  21:	"The World",
  22: "The Fool"
}
#do a 3 card spread of past, present and future
spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, card in spread.items():
  print("Your " + str(key) + " is the " + str(card) + " card.")
print()
#Your past is the Death card.
#Your present is the The Fool card.
#Your future is the Wheel of Fortune card.
#all right side up? sorry about your life of chaos lol


#hey let's make this a little more accurate and fun with randint()
#it's ZOE TIME
#randomize the cards pulled!! add orientation and randomize that too!
tarot2 = {
  1:	"The Magician",
  2:	"The High Priestess",
  3:	"The Empress",
  4:	"The Emperor",
  5:	"The Hierophant",
  6:	"The Lovers",
  7:	"The Chariot",
  8:	"Strength",
  9:	"The Hermit",
  10:	"Wheel of Fortune",
  11:	"Justice",
  12:	"The Hanged Man",
  13:	"Death",
  14:	"Temperance",
  15:	"The Devil",
  16:	"The Tower",
  17:	"The Star",
  18:	"The Moon",
  19:	"The Sun",
  20:	"Judgement",
  21:	"The World",
  22: "The Fool"
}

#find the keys of the cards pulled
spread_random = random.sample(range(1, 23), 3)

#which cards were pulled?
spread2 = {}
spread2_past_number = spread_random[0]
spread2_present_number = spread_random[1]
spread2_future_number = spread_random[2]

#map the key numbers to the name of the cards pulled
spread2["past"] = tarot2.pop(spread2_past_number)
spread2["present"] = tarot2.pop(spread2_present_number)
spread2["future"] = tarot2.pop(spread2_future_number)

#random 3 card spread
for key, card in spread2.items():
    print("Your " + str(key) + " is the " + str(card) + " card.")

#what orientation were the cards?
orientation_spread = [random.randrange(2) for i in range(3)]
#find the keys of the card orientations
orientation_spread_past = orientation_spread[0]
orientation_spread_present = orientation_spread[1]
orientation_spread_future = orientation_spread[2]

#map the key numbers to the name of the orientation (right side up or upside down)
orientation = {0: "right-side up", 1: "upside-down"}
orientation2 = {}
orientation2["past"] = orientation[orientation_spread_past]
orientation2["present"] = orientation[orientation_spread_present]
orientation2["future"] = orientation[orientation_spread_future]

for key, orientation in orientation2.items():
  print("The " + str(key) + " card is orientated " + str(orientation) + ".")
#it's not 100% perfect but IT WORKS!!!!

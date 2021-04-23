#Caesar Cipher: Take a message and shift all of the letters by a certain offset to produce the coded message
#Decode a message with an offset of 10
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!?.,' "
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
new_message = ""
for letter in message:
    #punctuation isn't shifted
    if letter not in punctuation:
        #find the index of the given letter in the alphabet
        alphabet_index = alphabet.find(letter)
        #account for the text shift using % 26
        #the letter added is from alphabet, NOT message!
        new_message += alphabet[(alphabet_index + 10) % 26]
    else:
        new_message += letter
print(new_message)
print()

#my turn
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!?., '"
message = "you stupid bitch we aren't even spies or anything. have you been reading q anon or something? i think you need a social media break."
new_message = ""
for letter in message:
    if letter not in punctuation:
        alphabet_index = alphabet.find(letter)
        new_message += alphabet[(alphabet_index - 10) % 26]
    else:
        new_message += letter
print(new_message)
#eat shit nerd
#prints "oek ijkfyt ryjsx mu qhud'j ulud ifyui eh qdojxydw. xqlu oek ruud huqtydw g qded eh iecujxydw? y jxyda oek duut q iesyqb cutyq rhuqa."

#testing
my_message = "oek ijkfyt ryjsx mu qhud'j ulud ifyui eh qdojxydw. xqlu oek ruud huqtydw g qded eh iecujxydw? y jxyda oek duut q iesyqb cutyq rhuqa."
new_message2 = ""
for letter in my_message:
    #punctuation isn't shifted
    if letter not in punctuation:
        #find the index of the given letter in the alphabet
        alphabet_index = alphabet.find(letter)
        #account for the text shift using % 26
        #the letter added is from alphabet, NOT message!
        new_message2 += alphabet[(alphabet_index + 10) % 26]
    else:
        new_message2 += letter
print(new_message2)
#prints "you stupid bitch we aren't even spies or anything. have you been reading q anon or something? i think you need a social media break."
print()

#2 more messages to decode
#YOU ARE SO ANNOOOYYYINNNGGG
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!?.,' "
message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
new_message = ""
for letter in message:
    if letter not in punctuation:
        alphabet_index = alphabet.find(letter)
        new_message += alphabet[(alphabet_index + 10) % 26]
    else:
        new_message += letter
print(new_message)
#prints "the offset for the second message is fourteen."

#offset is 14 this time
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!?.,' "
message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
new_message = ""
for letter in message:
    if letter not in punctuation:
        alphabet_index = alphabet.find(letter)
        new_message += alphabet[(alphabet_index + 14) % 26]
    else:
        new_message += letter
print(new_message)
#prints "performing multiple caesar ciphers to code your messages is even more secure!"
print()

#figure out the message without being given the offset. you have a 1/26 chance!
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!?.,' "
message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
new_message = ""
for letter in message:
    if letter not in punctuation:
        alphabet_index = alphabet.find(letter)
        #apparently the offset 7 after trial and error
        new_message += alphabet[(alphabet_index + 7) % 26]
    else:
        new_message += letter
print(new_message)
#prints "computers have rendered all of these old ciphers as obsolete. we'll have to really step up our game if we want to keep our messages safe."
print()

#Vigenère Cipher: A horrible cypher where you make a second alphabet using a keyword repeated over and over as many characters as the original message is long. 
#Add the indices of the characters between the message and the keyword alphabet at a given position. That's your new letter.
#hey Vigenère Cipher people? fuck you
def decode_message(coded_message, key):
    #generate keyword phrase
    letter_index = 0
    keyword_final = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "!?.,' "
    for i in range(0, len(coded_message)):
        #include punctuation as-is like before
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        #Map keyword phrase to coded message
        else:
            keyword_final += key[letter_index]
            letter_index = (letter_index + 1) % len(key)
    #decode the message
    translated_message = ""
    for i in range(0, len(coded_message)):
        #again, include punctuation as-is
        if coded_message[i] in punctuation:
            translated_message += coded_message[i]
        #find index of decoded character
        else:
            place_value = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[place_value % 26]
    return translated_message

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"
print(decode_message(message, keyword))
#prints "you were able to decode this? nice work! you are becoming quite the expert at crytography!"
print()

#my turn bitch
def vigenere_cipher(message, key):
    letter_index = 0
    keyword_final = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "!?.,' "
    for i in range(0, len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += key[letter_index]
            letter_index = (letter_index + 1) % len(key)
    translated_message = ""
    for i in range(0, len(message)):
        if message[i] in punctuation:
            translated_message += message[i]
        else:
            place_value = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[place_value % 26]
    return translated_message

message = "eat shit you garbage fuck! if you send me a message like this again, i'm going to show up at your house, break your computer then kick your ass. god damn"
keyword = "fuck"
print(vigenere_cipher(message, keyword))

#now lemme make sure you can read my horrible message
def decode_message(coded_message, key):
    letter_index = 0
    keyword_final = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "!?.,' "
    for i in range(0, len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += key[letter_index]
            letter_index = (letter_index + 1) % len(key)
    translated_message = ""
    for i in range(0, len(coded_message)):
        if coded_message[i] in punctuation:
            translated_message += coded_message[i]
        else:
            place_value = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[place_value % 26]
    return translated_message

message = "juv cmcv ito ikwvcqj zwmp! ch ito uosx oo f ggcxuio qcmo ybkc facss, c'o qtcpq yi urtq wz fn ayzl jyzmg, lwycu diwb hiozzngb ybgx pceu diwb fmu. qtx fkrh"
keyword = "fuck"
print(decode_message(message, keyword))
#good

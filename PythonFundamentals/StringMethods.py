# There are many String Methods

greeting = "Hey, I'm Joey Tribbiani"
how_u_doin = "How u doin?"

# upper(), lower(), title()
# all methods return a string, so you must save it to
# a variable
# upper() turns all characters in string to upper case
upper_greeting = greeting.upper()
# I'M JOEY TRIBBIANI
print(upper_greeting)
# lower() opposite of upper()
# i'm joey tribbiani
lower_greeting = upper_greeting.lower()
print(lower_greeting)
# title() first character of every word is capital
# How U Doin?
capital_greeting = how_u_doin.title()
print(capital_greeting)


# split() or split(delimiter)
# splits the string based on the parameter
# if there is no parameter delimiter the strings
# are split at spaces. 
# returns an array of strings
greeting_list = greeting.split()
# ['Hey,', "I'm", 'Joey', 'Tribbiani']
print(greeting_list)
greeting_list_i = greeting.split("i")
# ["Hey, I'm Joey Tr", 'bb', 'an', '']
print(greeting_list_i)
# Notice how the I wasn't split, this method is case 
# sensitive. Also if the parameter exists at the end
# a empty string is added to the returned list.
greeting_lines = """Hello
These
are 
newlines""".split('\n')
# ['Hello', 'These', 'are ', 'newlines']
print(greeting_lines)


# 'delimiter'.join(list)
# takes a list and joins it through the delimiter
greeting_new = ", ".join(greeting_list)
greeting_newline_string = "\n".join(greeting_list)
print(greeting_newline_string)
print(greeting_new)

def unique_english_letters(letters):
  unique = []
  for letter in letters: # iterate through list
    if (letter in unique):
      continue
    unique.append(letter)
  return len(unique)


def count_char_X(word, x):
    count = 0
    for letter in word:
        if (letter == x):
            count += 1
    return count

def count_multi_char_x(word, x):
  return len(word.split(x)) - 1 

def substring_between_letters(word, start, end):
  if (contains_end(word, end) and contains_start(word, start)):
    print(word.find(end))
    return word[word.find(start) + 1:word.find(end)]
  else:
    return word

def contains_end(word, end):
  return word.find(end) != -1

def contains_start(word, start):
  return word.find(start) != -1

def x_length_words(sentence, x):
  words = sentence.split()
  count = 0
  for word in words:
    if (x <= len(word)):
      count += 1
  return count >= len(words)

def check_for_name(sentence, name):
  if (sentence.upper().find(name) != -1):
    return True
  elif (sentence.lower().find(name) != -1):
    return True
  elif (sentence.title().find(name) != -1):
    return True
  else:
    return False

def every_other_letter(word):
  letters = ""
  for letter in range(0, len(word), 2):
    letters += word[letter]
  return letters

def reverse_string(word):
  return_string = ""
  for i in range(len(word) - 1, -1, -1):
     return_string += word[i]
  return return_string

def make_spoonerism(word1, word2):
  return word2[0] + word1[1:] + " " + word1[0] + word2[1:]

def add_exclamation(word):
  if (len(word) <= 20):
    for i in range(len(word), 20):
      word += "!"
    return word
  return word

import json
# import _pickle as pickle
# Use json for dicts and sets creation to files.
# Use pickle fo serialization, but couldn't make it work.


new_text = "This is a new line of text.\n"
text2 = "Another line of text to append.\n"

l = ["Line 1", "Line 2", "Line 3"]
family = {"Claudia": "wife",
          "Caricia": "daughter",
          "Franz-Che": "daughter",
          "Cesarito": "son",
          "Julito": "son",
          "Lucien": "son",
          "Brigitte": "daughter",
          "Michele": "daughter",
          "Benito": "son",
          "Jesusito": "son"}

file = open("text.txt", 'w')
file.write(new_text + text2) # it worked

# to append is 'a'
# with open('text.txt', 'w') as file:
#     file.write(json.dumps(family)) # use json loads to do reverse.

# since file is already open:
file.write(json.dumps(family) + "\n")
for item in l:
    file.write(item + "\n")

content = file.read()




# file.write(pickle.dumps(family)) # Use pickle 'loads' to do reverse.
# Couldn't use it
file.close()

# Appending lines

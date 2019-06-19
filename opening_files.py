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
for item, relationship  in family:
    file.write(item + relationship + "\n")
for item in l:
    file.write(item + "\n")

file.close()
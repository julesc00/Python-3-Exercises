import  re

text_to_reach = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123456789

Ha Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinsons
Mr. T
"""

sentence = "Start a sentence and then bing it to an end."

pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d")


matches = pattern.finditer(text_to_reach)
#
# for match in matches:
#     print(match)

with open('fake_contacts.txt', 'r+', encoding='utf-8') as f:
    contents = f.read()

    pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d")
    matches2 = pattern.finditer(contents)

    for match in matches2:
        print(match)


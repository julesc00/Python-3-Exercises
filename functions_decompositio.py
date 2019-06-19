def returning():
    return "I'm a result."

result = returning()
print(result) # This is the best way; clean.

def multival():
    return "this is another result, ", 2

print(multival())
# Write a function that checks if a sentence is a pangram.

def pangram_check(text):
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    result = True
    for n in sentence:
        if n not in text:
            result = False
    return result

a = pangram_check("abcdefghijklmnopqrstuvwxyz")
print(a)

# Write a function that counts the number of words in a sentence

def count_words(sentence):
    new_sentence = sentence.replace(" ","")
    return len(new_sentence)
sent = count_words("Hello   World")
print(sent)

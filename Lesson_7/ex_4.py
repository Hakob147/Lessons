text = "The Quick Brown Fox"
text_2 = text.replace(" ","")
count = 0
for n in text_2:
    if n.isupper():
        count = count+1
print(count) #uppercase
print(len(text_2)-count)  #lowercase
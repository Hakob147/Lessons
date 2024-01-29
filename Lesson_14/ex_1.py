# Write a function in python to read the content from a text file "example.txt" line by line
# and display the same on screen.

text = open("sample1.txt")
for i in text.readlines():
    print(i)
text.close()
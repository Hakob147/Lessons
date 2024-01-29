# Write a function display_words() in python to read text from a text file "example.txt",
# and display those words, which are less than 4 characters.
#
text = open("C:\\Users\\DELL\\Desktop\\pythonProject1\\Lesson_14\\sample1.txt")
# print(text.read())

splitted = text.read().split()
for n in splitted:
    if len(n) < 4:
        print(n)
# print(splitted)



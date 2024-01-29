# Write a function in Python to count and display the total number of words in a text file

text = open("C:\\Users\\DELL\\Desktop\\pythonProject1\\Lesson_14\\sample1.txt")
# print(text.read())
print(len(text.read()))
text.close()

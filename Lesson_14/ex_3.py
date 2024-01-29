# Write a python program to add text to a file and display the text in python.txt

text = open("C:\\Users\\DELL\\Desktop\\pythonProject1\\Lesson_14\\sample1.txt", "a")
text.write("\nHow do you do")
text.close()

text = open("C:\\Users\\DELL\\Desktop\\pythonProject1\\Lesson_14\\sample1.txt")
updated = text.read()
print(updated)

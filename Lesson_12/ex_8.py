# Write a function that takes a dictionary with information about students. Return info
# about the highest average student

students_info = {
'student1': {
'name': 'John Doe',
'age': 20,
'subjects': ['Math', 'Physics', 'English'],
'scores': [7, 9, 9, 6],
},
'student2': {
'name': 'Jane Smith',
'age': 19,
'subjects': ['Chemistry', 'Biology', 'History'],
'scores': [5, 6, 8, 10],
},
'student3': {
'name': 'Bob Johnson',
'age': 21,
'subjects': ['Computer Science', 'Statistics', 'Psychology'],
'scores': [8, 8, 9, 9, 9],
},
}

def highest_average(std):
    if sum(students_info['student1']["scores"]) / len(students_info['student1']["scores"]) > sum(students_info['student2']["scores"]) / len(students_info['student2']["scores"]) and sum(students_info['student1']["scores"]) / len(students_info['student1']["scores"]) > sum(students_info['student3']["scores"]) / len(students_info['student3']["scores"]):
        highest = students_info['student1']
    elif sum(students_info['student2']["scores"]) / len(students_info['student2']["scores"]) > sum(students_info['student1']["scores"]) / len(students_info['student1']["scores"]) and sum(students_info['student2']["scores"]) / len(students_info['student2']["scores"]) > sum(students_info['student3']["scores"]) / len(students_info['student3']["scores"]):
        highest = students_info['student2']
    else:
        highest = students_info['student3']
    return highest

name = highest_average("name")
print(name)
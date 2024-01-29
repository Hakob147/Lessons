# Write a function that takes a dictionary with information about students. Return info
# about the youngest student

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

def youngest_student(std):
    if students_info['student1']["age"] < students_info['student2']["age"] and students_info['student1']["age"] < students_info['student3']["age"]:
       smallest =  students_info['student1']
    elif students_info['student2']["age"] < students_info['student1']["age"] and students_info['student2']["age"] < students_info['student3']["age"]:
        smallest = students_info['student2']
    else:
        smallest = students_info['student3']
    return smallest

name = youngest_student("name")
print(name)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_grades={}
for index, student in enumerate(students):
    avg_grade = sum(grades[index]) / len(grades[index])
    student_grades[student] = avg_grade
print(student_grades)
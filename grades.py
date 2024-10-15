#Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
#Например: 'Aaron' - [5, 3, 3, 5, 4]
#Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print("students =", students)
sort_students = sorted(list(students))#отсортировали студентов
print("sort_students =", sort_students)
average_grades=[sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])] #корявое решение, но ничего лучше не придумал(((
print(average_grades)
dictionary_average_grades=dict(zip(sort_students,average_grades))
print(dictionary_average_grades)

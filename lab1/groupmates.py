groupmates = [
    {
        "name": "Максим",
        "group": "2254",
        "age": 18,
        "marks": [4, 3, 4, 5, 4]
    },
    {
        "name": "Андрей",
        "group": "2253",
        "age": 20,
        "marks": [3, 2, 3, 2, 2]
    },
    {
        "name": "Екатерина",
        "group": "2254",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Артем",
        "group": "2253",
        "age": 20,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Елена",
        "group": "2253",
        "age": 21,
        "marks": [5, 5, 4, 4, 5]
    }
]

def print_students(students):
    print("Имя".ljust(15), "Группа".ljust(10), "Возраст".ljust(10), "Оценки")
    for student in students:
        print(
            student["name"].ljust(15),
            student["group"].ljust(10),
            str(student["age"]).ljust(10),
            str(student["marks"])
        )
    print()

def filter_students(students, average_mark):
    result = []

    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > average_mark:
            result.append(student)

    return result

print("Все студенты:")
print_students(groupmates)

print("Студенты со средним баллом выше 4.0:")
filtered_students = filter_students(groupmates, 4.0)
print_students(filtered_students)
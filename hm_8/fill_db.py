from datetime import date
from faker import Faker
from random import randint, choice
from sqlite3 import connect

STUDENTS_AMOUNT = 30
GROUPS_AMOUNT = 3
DISCIPLINES_AMOUNT = 5
TEACHERS_AMOUNT = 3
EACH_STUDENT_MARKS_AMOUNT = 20
choose_discipline = [
    'Physics',
    'English',
    'Programming',
    'Data Structures and Algorithms',
    'Computer Logic',
    'Math Analysis',
    'History of science and technology',
    'Discrete Math',
    'Analytical geometry and linear algebra',
]


def generate_data() -> tuple[list, list, list, list, list[list, list]]:
    student_names = []
    group_names = []
    discipline_names = []
    teachers_names = []
    marks_and_dates = [[], []]
    fake_data = Faker('uk_UA')

    for _ in range(STUDENTS_AMOUNT):
        student_names.append(fake_data.name())

    for _ in range(TEACHERS_AMOUNT):
        teachers_names.append(fake_data.name())

    for _ in range(GROUPS_AMOUNT):
        group_names.append(fake_data.bothify(text='??-##'))

    for _ in range(DISCIPLINES_AMOUNT):
        discipline = choice(choose_discipline)
        discipline_names.append(discipline)
        choose_discipline.remove(discipline)

    for _ in range(EACH_STUDENT_MARKS_AMOUNT * STUDENTS_AMOUNT):
        marks_and_dates[0].append(randint(1, 12))
        marks_and_dates[1].append(
            fake_data.date_between(
                start_date=date(year=2022, month=1, day=1)
            )
        )

    return student_names, group_names, discipline_names, teachers_names, marks_and_dates


def prepare_data(student_names, group_names, discipline_names, teachers_names, marks_and_dates) -> tuple:
    prepared_groups = []
    for group in group_names:
        prepared_groups.append((group,))

    prepared_students = []
    for student in student_names:
        prepared_students.append((student, randint(1, GROUPS_AMOUNT)))

    prepared_disciplines = []
    for discipline in discipline_names:
        prepared_disciplines.append((discipline, choice(teachers_names)))

    prepared_discipline_student_relationships = []
    for student_id in range(1, STUDENTS_AMOUNT + 1):
        disciplines_ids = list(range(1, DISCIPLINES_AMOUNT + 1))
        for _ in range(randint(1, DISCIPLINES_AMOUNT)):
            chosen_discipline = choice(disciplines_ids)
            prepared_discipline_student_relationships.append(
                (student_id, chosen_discipline)
            )
            disciplines_ids.remove(chosen_discipline)

    prepared_marks = []
    discipline_student_marks_relationships_dict = {}
    for student_id in range(1, STUDENTS_AMOUNT + 1):
        discipline_student_marks_relationships_dict[student_id] = [[], []]
    for student_discipline_ids in prepared_discipline_student_relationships:
        discipline_student_marks_relationships_dict[
            student_discipline_ids[0]
        ][0].append(student_discipline_ids)
    for mark, mark_date in zip(marks_and_dates[0], marks_and_dates[1]):
        chosen_student = randint(1, STUDENTS_AMOUNT)
        if len(discipline_student_marks_relationships_dict[chosen_student][1]) >= EACH_STUDENT_MARKS_AMOUNT:
            continue
        chosen_discipline = choice(discipline_student_marks_relationships_dict[chosen_student][0])[1]
        prepared_marks.append(
            (
                mark,
                chosen_discipline,
                chosen_student,
                mark_date,
            )
        )

    return (
        prepared_students,
        prepared_groups,
        prepared_disciplines,
        prepared_discipline_student_relationships,
        prepared_marks,
    )


def insert_data_to_db(
        students_table,
        groups_table,
        disciplines_table,
        student_disciplines_table,
        marks_table
) -> None:
    with connect('all_marks.db') as connection:
        cur = connection.cursor()

        sql_to_groups = """INSERT INTO groups(name)
                            VALUES (?)"""
        cur.executemany(sql_to_groups, groups_table)

        sql_to_students = """INSERT INTO students(name, group_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_students, students_table)

        sql_to_disciplines = """INSERT INTO disciplines(name, teacher_name) 
                                 VALUES (?, ?)"""
        cur.executemany(sql_to_disciplines, disciplines_table)

        sql_to_student_disciplines = """INSERT INTO student_disciplines(student_id, discipline_id) 
                                         VALUES (?, ?)"""
        cur.executemany(sql_to_student_disciplines, student_disciplines_table)

        sql_to_marks = """INSERT INTO marks(value, discipline_id, student_id, when_received) 
                           VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_marks, marks_table)

        connection.commit()


if __name__ == "__main__":
    students, groups, disciplines, teachers, marks = generate_data()
    for_students, for_groups, for_disciplines, for_student_disciplines, for_marks = prepare_data(
        students,
        groups,
        disciplines,
        teachers,
        marks
    )
    insert_data_to_db(for_students, for_groups, for_disciplines, for_student_disciplines, for_marks)

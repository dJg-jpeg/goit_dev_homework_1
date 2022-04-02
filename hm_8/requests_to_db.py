from sqlite3 import connect


def execute_request(request: str) -> list:
    with connect('all_marks.db') as connection:
        cur = connection.cursor()
        cur.execute(request)
        return cur.fetchall()


if __name__ == "__main__":
    requests_to_db = []

    first_request = """SELECT ROUND(AVG(m.value), 2), m.when_received, m.student_id, s.name
                        FROM marks as m 
                        JOIN students as s ON m.student_id = s.id
                        GROUP BY m.student_id
                        ORDER BY ROUND(AVG(m.value), 2) DESC 
                        LIMIT 5"""
    requests_to_db.append(first_request)

    second_request = """SELECT ROUND(AVG(m.value), 2) as average_mark, s.name as student_name, d.name as discipline_name
                        FROM marks as m 
                        INNER JOIN students as s ON m.student_id = s.id
                        INNER JOIN disciplines as d ON m.discipline_id = d.id
                        GROUP BY s.name, d.name 
                        ORDER BY average_mark DESC
                        LIMIT 1"""
    requests_to_db.append(second_request)

    third_request = """SELECT ROUND(AVG(m.value), 2) as average_mark, g.name as group_name, d.name as discipline_name
                        FROM marks as m 
                        INNER JOIN students as s ON m.student_id = s.id
                        INNER JOIN disciplines as d ON m.discipline_id = d.id
                        INNER JOIN groups as g ON s.group_id = g.id 
                        GROUP BY d.name, g.name
                        ORDER BY g.name"""
    requests_to_db.append(third_request)

    fourth_request = """SELECT ROUND(AVG(m.value), 2) as average_mark
                        FROM marks as m"""
    requests_to_db.append(fourth_request)

    fifth_request = """SELECT name, teacher_name 
                        FROM disciplines 
                        ORDER BY teacher_name"""
    requests_to_db.append(fifth_request)

    sixth_request = """SELECT s.name as student_name, g.name as group_name
                        FROM students as s
                        INNER JOIN groups as g ON s.group_id = g.id
                        WHERE g.id = 2
                        ORDER BY group_name"""
    requests_to_db.append(sixth_request)

    seventh_request = """SELECT s.name as student, m.value as mark, d.name as discipline, g.name as group_name
                            FROM students as s
                            INNER JOIN marks as m ON s.id = m.student_id
                            INNER JOIN disciplines as d ON m.discipline_id = d.id
                            INNER JOIN groups as g ON s.group_id = g.id
                            WHERE g.id = 1 AND m.discipline_id = 4
                            ORDER BY student"""
    requests_to_db.append(seventh_request)

    eighth_request = """SELECT s.name as student, m.value as mark, m.when_received, d.name as discipline, g.name as group_name
                            FROM students as s
                            INNER JOIN marks as m ON s.id = m.student_id
                            INNER JOIN disciplines as d ON m.discipline_id = d.id
                            INNER JOIN groups as g ON s.group_id = g.id
                            WHERE g.id = 2 AND m.discipline_id = 4 AND m.when_received = (
                            SELECT MAX(m.when_received)
                            FROM marks as m
                            )
                            ORDER BY student"""
    requests_to_db.append(eighth_request)

    ninth_request = """SELECT s.name as student, d.name as discipline
                        FROM students as s
                        INNER JOIN student_disciplines as sd ON s.id = sd.student_id
                        INNER JOIN disciplines as d ON sd.discipline_id = d.id
                        WHERE s.id = 15
                        ORDER BY s.name"""
    requests_to_db.append(ninth_request)

    tenth_request = """SELECT s.name as student, d.name as discipline, d.teacher_name
                        FROM students as s
                        INNER JOIN student_disciplines as sd ON s.id = sd.student_id
                        INNER JOIN disciplines as d ON sd.discipline_id = d.id
                        WHERE s.id = 14
                        ORDER BY d.teacher_name """
    requests_to_db.append(tenth_request)

    eleventh_request = """SELECT ROUND(AVG(m.value), 2) as average_mark, s.name as student_name, d.teacher_name 
                            FROM marks as m 
                            INNER JOIN students as s ON m.student_id = s.id
                            INNER JOIN disciplines as d ON m.discipline_id = d.id
                            WHERE s.id = 14
                            GROUP BY d.teacher_name"""
    requests_to_db.append(eleventh_request)

    twelve_request = """SELECT ROUND(AVG(m.value), 2) as average_mark, d.teacher_name
                            FROM marks as m
                            INNER JOIN disciplines as d ON m.discipline_id = d.id
                            GROUP BY d.teacher_name """
    requests_to_db.append(twelve_request)

    for this_request in requests_to_db:
        print(execute_request(this_request))
        print('\n\n\n')

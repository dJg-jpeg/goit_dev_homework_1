DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(50) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
);

DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(20) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(30) UNIQUE NOT NULL,
    teacher_name CHAR(50) NOT NULL
);

DROP TABLE IF EXISTS student_disciplines;
CREATE TABLE student_disciplines (
    student_id INTEGER,
    discipline_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (discipline_id) REFERENCES disciplines (id)
);

DROP TABLE IF EXISTS marks;
CREATE TABLE marks (
    value TINYINT UNSIGNED NOT NULL,
    discipline_id INTEGER,
    student_id INTEGER,
    when_received DATE NOT NULL,
    FOREIGN KEY(discipline_id) REFERENCES disciplines (id),
    FOREIGN KEY(student_id) REFERENCES students (id)
);

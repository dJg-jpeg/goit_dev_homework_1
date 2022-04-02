from sqlite3 import connect

with open('all_marks.sql', 'r') as file:
    scrypt = file.read()

with connect('all_marks.db') as connection:
    cur = connection.cursor()
    cur.executescript(scrypt)

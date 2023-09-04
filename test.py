# Створити нову таблицю з полями id_subject, subject_name, subject_description, hours, semester_number;
# заповнитити її даними (мінімум 8 записів);
# прочитати дані з колонок subject_name, semester_number.

import sqlite3

with sqlite3.connect('subject.db') as db:
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subject(
        id_subject INTEGER PRIMARY KEY,
        subject_name VARCHAR(255),
        subject_description VARCHAR(255),
        hours TIMESTAMP,
        semester_number INTEGER
    )          
    """)

    cursor.execute("""
        INSERT INTO subject VALUES
            (1, 'Math', 'This is a hard subject', 60, 1),
            (2, 'English', 'Many people can speak english', 60, 1),
            (3, 'History', 'This is a interesting subject', 30, 2),
            (4, 'Geografy', 'In this subject we study the world.', 30, 1),
            (5, 'Music', 'In this subject we study play some musical instruments', 30, 1),
            (6, 'Art', 'We paint in this subject', 30, 2),
            (7, 'Science', 'In this subject we study how the world is built', 30, 1),
            (8, 'PE', 'We do exercise ih this subject', 30, 2)
    """)

    cursor.execute("""
        SELECT subject_name, semester_number
        FROM subject
    """)
    result = cursor.fetchall()
    for row in result:
        print(row)

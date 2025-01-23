import sqlite3
conection = sqlite3.connect('book_club_db.db')
cursor = conection.cursor()
cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        id_club INTEGER
    )
    '''
)
conection.commit()
conection.close()
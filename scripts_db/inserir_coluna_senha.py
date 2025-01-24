import sqlite3
conection = sqlite3.connect('book_club_db.db')
cursor = conection.cursor()
cursor.execute('''
       ALTER TABLE users ADD COLUMN password varchar(50)
               '''
    )
conection.commit()
conection.close()
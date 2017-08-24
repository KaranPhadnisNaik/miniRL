import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_links = "CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY, hash text, full_url text, visits text)"
cursor.execute(create_links)

connection.commit()
connection.close()

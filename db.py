import sqlite3

conn = sqlite3.connect('library.sqlite')
cursor = conn.cursor()

sql_query = """CREATE TABLE IF NOT EXISTS books (
id INTEGER NOT NULL,
title VARCHAR,
author VARCHAR,
language VARCHAR,
PRIMARY KEY (id AUTOINCREMENT));"""

conn.execute(sql_query)
conn.commit()

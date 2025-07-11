import sqlite3

# 建立database 
conn = sqlite3.connect('database.db')

# 建立客人表
conn.execute('CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY , name TEXT, surname TEXT)')


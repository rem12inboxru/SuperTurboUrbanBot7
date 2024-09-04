import sqlite3
from sqlite3 import Cursor


def initiate_db():
    connection = sqlite3.Connection('Products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)''')

    for i in range(1, 5):
        cursor.execute("INSERT OR IGNORE INTO Products(id, title, description, price) VALUES(?,?,?,?)",
                       (i, f'Название: Продукт{i}', f'Описание: Описание{i}', f'Цена {i * 100}'))

    connection.commit()
    connection.close()


def get_all_produkts():
    initiate_db()
    connection = sqlite3.Connection('Products.db')
    cursor = connection.cursor()
    y = [0]
    cursor.execute("SELECT title, description, price FROM Products")

    for i in cursor.fetchall():
        y.append(f' {i[0]} | {i[1]} | {i[2]}')
    return y




import sqlite3


def connect():
    return sqlite3.connect('erp.db')


def execute(query: str, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

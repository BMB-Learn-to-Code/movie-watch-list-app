import sqlite3
from queries import CREATE_TABLE, DROP_TABLE, INSERT_MOVIE, GET_ALL_MOVIES

def create_table():
    conn = sqlite3.connect("database.db")
    with conn:
        conn.execute(CREATE_TABLE)

def drop_table():
    conn = sqlite3.connect("database.db")
    with conn:
        conn.execute(DROP_TABLE)


def add_movie():
    conn = sqlite3.connect("database.db")
    with conn:
        conn.execute(INSERT_MOVIE,("", 0,0))

def get_all_movies():
    conn = sqlite3.connect("database.db")
    with conn:
        return conn.execute(GET_ALL_MOVIES).fetchall()

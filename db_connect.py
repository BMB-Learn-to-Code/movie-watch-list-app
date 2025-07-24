import sqlite3
import time
from queries import CREATE_TABLE, DROP_TABLE, INSERT_MOVIE, GET_ALL_MOVIES, GET_ALL_WATCHED_MOVIES, SELECT_UPCOMING_MOVIES, SET_WATCHED_MOVIES

def connect():
    return sqlite3.connect("database.db")
def create_table():
    conn = connect()
    with conn:
        conn.execute(CREATE_TABLE)

def drop_table():
    conn = connect()
    with conn:
        conn.execute(DROP_TABLE)


def add_movie(data):
    conn = connect()
    with conn:
        conn.execute(INSERT_MOVIE,(data[0], data[1], 0))

def get_all_movies():
    conn = connect()
    with conn:
        return conn.execute(GET_ALL_MOVIES).fetchall()

def get_all_watched_movies():
    conn = connect()
    with conn:
        return conn.execute(GET_ALL_WATCHED_MOVIES).fetchall()

def get_all_upcoming_movies():
    conn = connect()
    with conn:
        return conn.execute(SELECT_UPCOMING_MOVIES, (int(time.time()),)).fetchall()

def update_watched_movies(title):
    conn = connect()
    with conn:
        conn.execute(SET_WATCHED_MOVIES, (title))

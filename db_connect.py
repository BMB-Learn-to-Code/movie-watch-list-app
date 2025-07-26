import sqlite3
from datetime import datetime
from queries import CREATE_TABLE, DROP_TABLE, INSERT_MOVIE, GET_ALL_MOVIES, GET_ALL_WATCHED_MOVIES, SELECT_UPCOMING_MOVIES, INSERT_WATCHED_MOVIES, DELETE_MOVIE, DELETE_WATCHED_MOVIE

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
        return conn.execute(SELECT_UPCOMING_MOVIES, (datetime.now(),)).fetchall()

def update_watched_movies(title, watcher_name):
    conn = connect()
    print("Updating status...")
    with conn:
        conn.execute(INSERT_WATCHED_MOVIES, (title, watcher_name))

def delete_movie(title):
    conn = connect()
    print("Deleting movie...")
    with conn:
        conn.execute(DELETE_MOVIE, (title,))

def delete_watched(title):
    conn = connect()
    print("Removing movie from watch_list...")
    with conn:
        conn.execute(DELETE_WATCHED_MOVIE, (title,))

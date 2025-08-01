import sqlite3
from datetime import datetime
from queries import CREATE_MOVIES_TABLE,CREATE_USERS_TABLE, DROP_MOVIES_TABLE, INSERT_MOVIE, GET_ALL_MOVIES, GET_ALL_WATCHED_MOVIES, SELECT_UPCOMING_MOVIES, INSERT_WATCHED_MOVIES, DELETE_MOVIE, DELETE_WATCHED_MOVIE, INSERT_USER, CREATE_WATCHED_TABLE

def connect():
    return sqlite3.connect("database.db")

def create_table():
    conn = connect()
    with conn:
        conn.execute(CREATE_MOVIES_TABLE)
        conn.execute(CREATE_USERS_TABLE)
        conn.execute(CREATE_WATCHED_TABLE)

def drop_table():
    conn = connect()
    with conn:
        conn.execute(DROP_MOVIES_TABLE)

def insert_user(name):
    conn = connect()
    with conn:
        conn.execute(
           INSERT_USER, (name,)
        )

def add_movie(data):
    conn = connect()
    with conn:
        conn.execute(INSERT_MOVIE,(data[0], data[1]))

def get_all_movies():
    conn = connect()
    with conn:
        return conn.execute(GET_ALL_MOVIES).fetchall()

def get_all_watched_movies(user_username):
    conn = connect()
    with conn:
        return conn.execute(GET_ALL_WATCHED_MOVIES, (user_username,)).fetchall()

def get_all_upcoming_movies():
    conn = connect()
    with conn:
        return conn.execute(SELECT_UPCOMING_MOVIES, (datetime.now(),)).fetchall()

def update_watched_movies(title, user_username):
    conn = connect()
    print("Updating status...")
    with conn:
        conn.execute(INSERT_WATCHED_MOVIES, (title, user_username))

def delete_movie(title):
    conn = connect()
    print("Deleting movie...")
    with conn:
        conn.execute(DELETE_MOVIE, (title,))

def delete_watched(title, user_username):
    conn = connect()
    print("Removing movie from watch_list...")
    with conn:
        conn.execute(DELETE_WATCHED_MOVIE, (title,user_username))

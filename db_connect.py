import sqlite3
from datetime import datetime
from queries import (
    CREATE_MOVIES_TABLE, CREATE_USERS_TABLE, CREATE_WATCHED_TABLE,
    DROP_MOVIES_TABLE,INSERT_MOVIE, INSERT_USER, INSERT_WATCHED_MOVIES,
    GET_ALL_MOVIES, GET_ALL_WATCHED_MOVIES, SELECT_UPCOMING_MOVIES,
    DELETE_MOVIE, DELETE_USER, DELETE_WATCHED_MOVIE, GET_ALL_USERS,
    DELETE_ALL_WATCHED_MOVIES_FROM_USER
)

def normalize_date(date_obj):
    """Convert datetime object to Unix timestamp for consistent storage."""
    return date_obj.timestamp()

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
        conn.execute(INSERT_MOVIE,(data[0], normalize_date(data[1])))

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
        return conn.execute(SELECT_UPCOMING_MOVIES, (normalize_date(datetime.now()),)).fetchall()

def update_watched_movies(user_username,movie_id):
    conn = connect()
    print("Updating status...")
    with conn:
        conn.execute(INSERT_WATCHED_MOVIES, (user_username, movie_id))

def delete_movie(id):
    conn = connect()
    print("Deleting movie...")
    with conn:
        conn.execute(DELETE_MOVIE, (id,))

def delete_watched(user_username, movie_id):
    conn = connect()
    print("Removing movie from watch_list...")
    with conn:
        conn.execute(DELETE_WATCHED_MOVIE, (user_username, movie_id))

def create_new_user(name):
    conn = connect()
    print("Creating new user...")
    with conn:
        conn.execute(INSERT_USER, (name,))

def delete_user(name):
    conn = connect()
    print("Deleting user...")
    with conn:
        conn.execute(DELETE_USER, (name,))

def get_all_users():
    conn = connect()
    with conn:
        return conn.execute(GET_ALL_USERS).fetchall()

def delete_all_movies_from_user(username):
    conn = connect()
    with conn:
        return conn.execute(DELETE_ALL_WATCHED_MOVIES_FROM_USER, (username,))

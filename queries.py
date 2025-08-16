CREATE_MOVIES_TABLE = """
       CREATE TABLE IF NOT EXISTS movies (
           id int PRIMARY KEY AUTOINCREMENT,
           title TEXT,
           release_timestamp REAL
        );

    """
CREATE_USERS_TABLE = """
    CREATE TABLE IF NOT EXISTS users (
        name TEXT PRIMARY KEY
        );
    """

CREATE_WATCHED_TABLE = """
    CREATE TABLE IF NOT EXISTS watched (
        user_username TEXT PRIMARY KEY,
        movie_id INTEGER,
        FOREIGN KEY(user_username) REFERENCES user(username)
        FOREIGN KEY(movie_id) REFEERNCES movies(id)
    );
"""

INSERT_WATCHED_MOVIE = """
    INSERT INTO watched (user_username, movie_id)
    VALUES(?,?)
"""

DROP_MOVIES_TABLE = """
       DROP TABLE IF EXISTS movies;
    """

INSERT_USER = """
       INSERT INTO users (name)
       VALUES (?);
    """

INSERT_MOVIE = """
       INSERT INTO movies (title, release_timestamp)
       VALUES (?, ?);
    """
GET_ALL_MOVIES = """
       SELECT * FROM movies;
    """

GET_ALL_WATCHED_MOVIES = """
    SELECT * FROM watched WHERE user_username = ?;
"""

SELECT_UPCOMING_MOVIES = """
    SELECT * FROM movies WHERE release_timestamp > ?;
"""

# TODO: Filter upcoming movies since they cannot be watched
INSERT_WATCHED_MOVIES = """
    INSERT INTO watched (title,user_username)
    VALUES(?,?);
"""

DELETE_MOVIE = """
    DELETE FROM movies WHERE id = ?;
"""

DELETE_WATCHED_MOVIE = """
    DELETE FROM watched WHERE title = ? AND user_username = ?;
"""

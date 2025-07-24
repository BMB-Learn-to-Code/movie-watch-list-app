CREATE_TABLE = """
       CREATE TABLE IF NOT EXISTS movies (
           title TEXT,
           release_timestamp REAL,
           watched INTEGER DEFAULT 0
        );
    """
DROP_TABLE = """
       DROP TABLE IF EXISTS movies;
    """

INSERT_MOVIE = """
       INSERT INTO movies (title, release_timestamp, watched)
       VALUES (?, ?, ?);
    """
GET_ALL_MOVIES = """
       SELECT * FROM movies;
    """

GET_ALL_WATCHED_MOVIES = """
    SELECT * FROM movies WHERE watched = 1;
"""

SELECT_UPCOMING_MOVIES = """
    SELECT * FROM movies WHERE release_timestamp > ?;
"""

SET_WATCHED_MOVIES = """
    UPDATE movies SET watched = 1 WHERE title = ?;
"""

CREATE_TABLE = """
       CREATE TABLE IF NOT EXISTS movies (
           title TEXT,
           release_timestamp REAL,
        );
        CREATE TABLE IF NOT EXISTS watch_list (
            title TEXT, watcher_name TEXT
        )
    """
DROP_TABLE = """
       DROP TABLE IF EXISTS movies;
    """

INSERT_MOVIE = """
       INSERT INTO movies (title, release_timestamp)
       VALUES (?, ?)
    """
GET_ALL_MOVIES = """
       SELECT * FROM movies;
    """

# TODO: Change the queries to instead of set movie as watched, add it to the watched table
GET_ALL_WATCHED_MOVIES = """
    SELECT * FROM watch_list WHERE watcher_name = ?;
"""

SELECT_UPCOMING_MOVIES = """
    SELECT * FROM movies WHERE release_timestamp > ?;
"""

# Filter upcoming movies since they cannot be watched
INSERT_WATCHED_MOVIES = """
    INSERT INTO watch_list (title,watcher_name)
    VALUES(?,?)
"""

DELETE_MOVIE = """
    DELETE FROM movies WHERE title = ?;
"""

DELETE_WATCHED_MOVIE = """
    DELETE FROM watch_list WHERE title = ? AND watcher_name = ?;
"""

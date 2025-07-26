CREATE_TABLE = """
       CREATE TABLE IF NOT EXISTS movies (
           title TEXT,
           release_timestamp REAL
        );

    """
CREATE_WATCHED_TABLE= """
        CREATE TABLE IF NOT EXISTS watched (
            title TEXT, watcher_name TEXT
        );
"""
DROP_TABLE = """
       DROP TABLE IF EXISTS movies;
    """

INSERT_MOVIE = """
       INSERT INTO movies (title, release_timestamp)
       VALUES (?, ?);
    """
GET_ALL_MOVIES = """
       SELECT * FROM movies;
    """

# TODO: Change the queries to instead of set movie as watched, add it to the watched table
GET_ALL_WATCHED_MOVIES = """
    SELECT * FROM watched WHERE watcher_name = ?;
"""

SELECT_UPCOMING_MOVIES = """
    SELECT * FROM movies WHERE release_timestamp > ?;
"""

# Filter upcoming movies since they cannot be watched
INSERT_WATCHED_MOVIES = """
    INSERT INTO watched (title,watcher_name)
    VALUES(?,?);
"""

DELETE_MOVIE = """
    DELETE FROM movies WHERE title = ?;
"""

DELETE_WATCHED_MOVIE = """
    DELETE FROM watched WHERE title = ? AND watcher_name = ?;
"""

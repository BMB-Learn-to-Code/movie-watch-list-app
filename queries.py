CREATE_TABLE = """
       CREATE TABLE IF NOT EXISTS movies (
           title TEXT,
           release_timestamp REAL,
           watched INTEGER DEFAULT 0
        )
    """
DROP_TABLE = """
       DROP TABLE IF EXISTS movies
    """

INSERT_MOVIE = """
       INSERT INTO movies (title, release_timestamp, watched)
       VALUES (?, ?, ?)
    """
GET_ALL_MOVIES = """
       SELECT * FROM movies
    """

Summary of the project:
This project creates a database with a star schema of multiple tables related to song data and log data related to those songs. The database consists of 5 tables (songplays, song, artist, user, time) which link together through the fact table (songplays) and their associated ID values.

How to run the Python scripts:
In order to run the python scripts, open the terminal and enter the following commands:
        >>> python create_tables.py
        >>> python etl.py
These commands will create the database and tables and insert the values for each table.

An explanation of the files in the repository:
The files in the repository consist of song data and log data.
        >>> song data consists of artist information and song information.
        >>> log data consists of song play timestamp, geographical location, level, and user information.
# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABlE IF EXISTS times;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL PRIMARY KEY, start_time TIMESTAMP NOT NULL, user_id INT NOT NULL, level VARCHAR(50) NOT NULL, song_id VARCHAR(255) NOT NULL, artist_id VARCHAR(255) NOT NULL, session_id VARCHAR(255) NOT NULL, location VARCHAR(255) NOT NULL, user_agent VARCHAR(255) NOT NULL);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id INT PRIMARY KEY, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, gender VARCHAR(50) NOT NULL, level VARCHAR(50) NOT NULL);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id VARCHAR(255) PRIMARY KEY, title VARCHAR(255) NOT NULL, artist_id VARCHAR(255) NOT NULL, year INT NOT NULL, duration NUMERIC NOT NULL);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id VARCHAR(255) PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL, location VARCHAR(255) NOT NULL, latitude FLOAT NOT NULL, longitude FLOAT NOT NULL);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time TIME, hour INT, day INT, week INT, month INT, year INT, weekday INT);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday) VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = """SELECT song_id, artist_id FROM songs"""

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
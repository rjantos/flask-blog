import sqlite3


# create a new database if the database doesnt already exist
with sqlite3.connect("blog.db") as connection:
    # get a cursor object used to execute SQL
    c = connection.cursor()
    # create the table
    c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

    # create dummy data into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')

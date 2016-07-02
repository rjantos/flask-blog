# blog.py - controller

#imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g

# config
DATABASE = 'blog.db'

app = Flask(__name__)

# pulls in app config by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used fro connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run(debug=True)
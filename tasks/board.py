#!/usr/bin/env python3

import sqlite3
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def main():

    output = """
    
    <head><style>body {font-family: Arial, sans-serif;}</style></head><body>
    
    Welcome to our free flat bulletin board. 
    Use this website to stay in touch with other people. <br>
    Feel free to enter a message:

    <form action='new_message' method="post">
        <textarea name="message"> </textarea>
        <input type="submit">
    </form>

    <br>
    Messages:
    <br>
    """


    conn = sqlite3.connect("database/server.db")
    cur = conn.cursor()

    # TODO: Execute SQL statement to fetch the content field of all messages from the database

    conn.commit()
    conn.close()

    # Format and display output
    output = ""
    for row in cur:
        output = output + "<font color=\"blue\"> {0} </font> <br>".format(row[0])

    return output


@app.route('/new_message', methods=['POST'])
def new_message():

    # TODO: Parse form data 'message' from POST request and store it in this variable 'message'
    message = ""

    conn = sqlite3.connect("database/server.db")
    cur = conn.cursor()

    # TODO: Execute SQL statement to store the content of 'message' variable in the database

    conn.commit()
    conn.close()

    return redirect('/')


app.run(host='0.0.0.0', port=8000)

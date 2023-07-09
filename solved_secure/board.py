#!/usr/bin/env python3

import sqlite3
import html
from flask import Flask, redirect, request

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
    cur.execute("SELECT content FROM messages ORDER BY id DESC ")

    # Format and display output
    for row in cur:
        output = output + "<font color=\"blue\"> {0} </font> <br>".format(row[0])

    conn.commit()
    conn.close()

    return output


@app.route('/new_message', methods=['POST'])
def new_message():

    # TODO: Parse form data 'message' from POST request and store it in this variable 'message'
    message = request.form['message']

    conn = sqlite3.connect("database/server.db")
    cur = conn.cursor()

    # TODO: Execute SQL statement to store the content of 'message' variable in the database
    sanitized_input = html.escape(message)
    cur.execute("INSERT INTO messages (content) VALUES (?)", (sanitized_input, ))

    conn.commit()
    conn.close()

    return redirect('/')


app.run(host='0.0.0.0', port=8000)

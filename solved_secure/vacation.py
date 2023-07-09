#!/usr/bin/env python3

import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():

    output = """
    
    <head><style>body {font-family: Arial, sans-serif;}</style></head><body>
    
    Calculate cost of vacation days:

    <form method="post">
        <input type="text" placeholder="Employee ID" name="employee_id" required>
        <input type="number" placeholder="Number of vacation days" name="days" required>

        <input type="submit">
    </form>
    """

    if request.method == 'GET':
        return output

    if request.method == 'POST':

        # TODO: Parse form data 'employee_id' from POST request and store it in this variable 'employee_id'
        employee_id = request.form['employee_id']

        # TODO: Parse form data 'days' from POST request and store it in this variable 'days'
        days = request.form['days']

        return output + str(do_employee(employee_id, days))


def do_employee(employee_id, vacation_days):

    vacation_days = int(vacation_days)

    conn = sqlite3.connect("database/server.db")
    cur = conn.cursor()

    # TODO: Execute SQL statement to fetch 'name' and 'hourly_wage' of the employee based on the given 'employee_id' from the database.
    cur.execute("SELECT name, hourly_wage FROM employees WHERE e_id = ?", (employee_id,))

    # Format and display output
    output = ""
    for row in cur:
        cost = calculate_cost_of_vacation_days(row[1], vacation_days)
        output = output + "Cost of vacation for {0} is {1:.2f} USD <br>".format(row[0], cost)

    conn.commit()
    conn.close()

    return output


def calculate_cost_of_vacation_days(hourly_wage, number_of_days):

    cost = 0 

    # TODO: Calculate cost of vacation based on employees hourly wage.
    cost = number_of_days * 8 * hourly_wage
    if hourly_wage < 0:
        cost = 0

    return cost


app.run(host='0.0.0.0', port=8000)

#!/usr/bin/env python3

import shlex, subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():

    output = """
    <head><style>body {font-family: Arial, sans-serif;}</style></head><body>

    Find the records for a domain name using this online tool by providing the domain name as a GET parameter in this websites URL. 
    <br>
    For example, try <p style="font-family:'Lucida Console', monospace">http://127.0.0.1:8000?domain_name=wikipedia.com</p>
    to view their DNS records. <br> <br> 

    """

    get_parameter_name = 'domain_name'

    # TODO: Parse GET parameter 'domain_name' from query string and store it in this variable 'domain_name'
    domain_name = request.args.get(get_parameter_name)

    # If GET parameter is not empty, call lookup(), otherwise do nothing
    if domain_name:
        return output + lookup(domain_name) 
    else:
        return output 


def lookup(destination):


    # TODO: Let the server perform a DNS lookup for the domain name in 'destination'
    cmd = 'nslookup ' + destination

    sanitized_destination = ''.join(c for c in destination if c.isalnum() or c in ['.', '-'])

    cmd = "nslookup {}".format(sanitized_destination)
    args = shlex.split(cmd)

    # TODO: Return the output of the command as a string to be displayed on the page
    output = ""

    try:
        output = subprocess.check_output(args, shell=False).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()


    return " Result: <p><span style=\"color: #ff00ff; font-family:'Lucida Console', monospace\">{}</span></p>".format(output)


app.run(host='0.0.0.0', port=8000)

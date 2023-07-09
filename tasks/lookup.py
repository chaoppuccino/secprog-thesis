#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():

    output = """
    <head><style>body {font-family: Arial, sans-serif;}</style></head><body>

    Find the records for a domain name using this online tool by providing the domain name as a GET parameter in this websites URL. 
    <br>
    For example, try wikipedia.com
    to view their DNS records. <br> <br> 

    """

    get_parameter_name = 'domain_name'

    # TODO: Parse GET parameter 'domain_name' from query string and store it in this variable 'domain_name'
    domain_name = ""

    # If GET parameter is not empty, call lookup(), otherwise do nothing
    if domain_name:
        return output + lookup(domain_name) 
    else:
        return output 


def lookup(destination):


    # TODO: Let the server perform a DNS lookup for the domain name in 'destination'
    cmd = 'nslookup ' + destination

    # TODO: Return the output of the command as a string to be displayed on the page
    output = ""

    return " Result: <font color=\"purple\"> {} </font>".format(output)


app.run(host='0.0.0.0', port=8000)

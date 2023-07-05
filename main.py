# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import http.client
import json
import requests
import pandas as pd

def add_credentials():
    # load API token username and password
    # Please input your own credentials which you can make at https://www.ravelry.com/groups/ravelry-api
    authUsername = '<your credentials>'
    authPassword = '<your credentials>'

    # define URL for the API request
    url = 'https://api.ravelry.com/color_families.json'
    # make the request
    r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(authUsername, authPassword))
    # close the connection
    r1.close()

    print("response code: {}".format(r1))  # tells me the response code
    print("response code Details: {}".format(r1.iter_lines()))  # tells me details about the response code
    print("response output:")
    print(r1.text)  # tells me the

    
def call_api():
    # Use a breakpoint in the code line below to debug your script.
    r = requests.get('https://www.office.com')  # how to make the request
    print(r)  # to see if we get a valid output code
    print(r.iter_lines())  # what the output code means
    # print(r.text) # what the output of the request is.  This is commented out becuase it is very long
    r.close()  # closes the request.  Best practice.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call_api()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

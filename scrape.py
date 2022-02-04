# import necessary modules
from bs4 import BeautifulSoup
import requests
import json


# get the URL in a useable form
url = "https://www.w3schools.com/cssref/css_selectors.asp"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# select your objects
selectors = [elem.string for elem in soup.select('td.notranslate')]


# define filter function
"""
def filter_func(elem):
    if elem == None:
        return False
    if ' ' in elem:
        return True
    return False
"""

# apply filter function
#selectors = list(filter(filter_func, selectors))


# output
print(selectors)




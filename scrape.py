# import necessary modules
from bs4 import BeautifulSoup
import requests
import json


# get the URL in a useable form
url = "https://www.w3schools.com/cssref/css_selectors.asp"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# select your objects
table_rows = [elem for elem in soup.select('.ws-table-all tr')]


# define filter function
def filter_func(elem):
    return True

# apply filter function
table_rows = list(filter(filter_func, table_rows))


# organize and output to json
selectors = []

# output
for row in table_rows:
    cells = list(row.select('td'))
    if cells:
        entry = {
            'example': cells[1].text,
            'explanation': cells[2].text,
        }
        if cells[0].a:
            entry['selector'] = cells[0].a.text
        else:
            entry['selector'] = cells[0].text

        selectors.append(entry)
        

with open("selectors.json", 'w') as f:
    json.dump(selectors, f)

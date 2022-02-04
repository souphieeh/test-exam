# import necessary modules
from bs4 import BeautifulSoup
import requests


# get the URL in a useable form
url = "https://en.wikipedia.org/wiki/List_of_ursids"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# select your objects
bears = [elem.string for elem in soup.select('th[scope=row] a')]


# define filter function
def filter_func(elem):
    if elem == None:
        return False
    if ' ' in elem:
        return True
    return False


# apply filter function
bears = list(filter(filter_func, bears))


# output
print(bears)